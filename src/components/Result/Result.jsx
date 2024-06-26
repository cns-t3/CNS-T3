'use client';

import React, { useState, useEffect } from 'react';
import ResultHeader from './ResultHeader';
import ResultsViewer from './ResultsViewer';

function Result({ data }) {
  const [filterNow, setFilterNow] = useState(false);
  const [defaultCategoryOptions, setCategories] = useState([]);

  useEffect(() => {
    fetch('/categories.json')
      .then((response) => response.json())
      .then((categoryData) => {
        const categoryNames = Object.keys(categoryData.categories).map((cat) => cat.toLowerCase());
        setCategories(categoryNames);
      });
  }, []);

  const [selectedFilterOptions, setSelectedFilterOptions] = useState({
    riskRating: ['low', 'medium', 'high'],
    category: defaultCategoryOptions,
    identityMatch: 0,
    date: 'all time',
  });
  const [filteredData, setFilteredData] = useState(data);
  const [selectedSortOption, setSelectedSortOption] = useState('High to Low Risk');

  useEffect(() => {
    setSelectedFilterOptions((prevOptions) => ({
      ...prevOptions,
      category: defaultCategoryOptions,
    }));
  }, [defaultCategoryOptions]);

  const riskRankingOrder = ['High', 'Medium', 'Low'];

  const sortArticlesByRiskRating = (asc = true) => {
    setFilteredData((prevData) => {
      const sortedArticles = [...prevData.newsArticles].sort((a, b) => {
        if (asc) {
          return (
            riskRankingOrder.indexOf(a.risk_rating) - riskRankingOrder.indexOf(b.risk_rating)
          );
        }
        return (
          riskRankingOrder.indexOf(b.risk_rating) - riskRankingOrder.indexOf(a.risk_rating)
        );
      });
      return { ...prevData, newsArticles: sortedArticles };
    });
  };

  // Sort articles by descending date
  const sortArticlesByDescendingDate = () => {
    setFilteredData((prevData) => {
      const sortedArticles = [...prevData.newsArticles].sort(
        (a, b) => new Date(a.publishedAt) - new Date(b.publishedAt),
      );
      return { ...prevData, newsArticles: sortedArticles };
    });
  };

  // Sort articles by ascending date
  const sortArticlesByAscendingDate = () => {
    setFilteredData((prevData) => {
      const sortedArticles = [...prevData.newsArticles].sort(
        (a, b) => new Date(b.publishedAt) - new Date(a.publishedAt),
      );
      return { ...prevData, newsArticles: sortedArticles };
    });
  };

  // Sort articles by identity match
  const sortArticlesByIdentityMatch = (asc = true) => {
    setFilteredData((prevData) => {
      const sortedArticles = [...prevData.newsArticles].sort((a, b) => {
        if (asc) {
          return a.score - b.score;
        }

        return b.score - a.score;
      });
      return { ...prevData, newsArticles: sortedArticles };
    });
  };

  const sortArticles = () => {
    if (selectedSortOption === 'Newest to Oldest') {
      sortArticlesByAscendingDate();
    } else if (selectedSortOption === 'Oldest to Newest') {
      sortArticlesByDescendingDate();
    } else if (selectedSortOption.includes('Identity Match')) {
      sortArticlesByIdentityMatch(selectedSortOption === 'Low to High Identity Match');
    } else {
      // Added this line to call the sortArticlesByRiskRating function
      sortArticlesByRiskRating(selectedSortOption === 'High to Low Risk');
    }
  };

  // process date option
  const processDateOption = (dateOption) => {
    let startDate = new Date();
    let endDate = new Date();

    switch (dateOption) {
      case 'today':
        // No change needed; start and end date are both today.
        break;
      case 'past 7 days':
        startDate.setDate(startDate.getDate() - 7);
        break;
      case 'past 30 days':
        startDate.setDate(startDate.getDate() - 30);
        break;
      case 'past 60 days':
        startDate.setDate(startDate.getDate() - 60);
        break;
      case 'past 90 days':
        startDate.setDate(startDate.getDate() - 90);
        break;
      case 'past 180 days':
        startDate.setDate(startDate.getDate() - 180);
        break;
      case 'past year':
        startDate.setFullYear(startDate.getFullYear() - 1);
        break;
      case 'all time':
        startDate = '';
        endDate = '';
        break;
      default:
    }

    return [startDate, endDate];
  };

  const filterData = (inputData, inputSelectedFilterOptions) => {
    const riskRatingOptions = inputSelectedFilterOptions.riskRating;
    const categoryOptions = inputSelectedFilterOptions.category;
    const dateOption = inputSelectedFilterOptions.date;
    const identityMatchScore = inputSelectedFilterOptions.identityMatch;

    const dates = processDateOption(dateOption);

    if (
      riskRatingOptions.length === 3 && categoryOptions.length === 5 && dateOption === 'all time' && identityMatchScore === 0
    ) {
      return inputData;
    }
    let filteredArticles = inputData;
    if (dateOption === 'all time') {
      filteredArticles = data.newsArticles.filter(
        (article) => riskRatingOptions.includes(article.risk_rating.toLowerCase())
        && categoryOptions.includes(article.category.toLowerCase())
        && article.score >= identityMatchScore,
      );
    } else {
      filteredArticles = inputData.newsArticles.filter(
        (article) => riskRatingOptions.includes(article.risk_rating.toLowerCase())
        && categoryOptions.includes(article.category.toLowerCase())
        && new Date(article.publishedAt) > dates[0]
        && new Date(article.publishedAt) < dates[1]
        && article.score >= identityMatchScore,
      );
    }
    return {
      ...inputData,
      newsArticles: filteredArticles,
    };
  };

  useEffect(() => {
    if (filterNow) {
      const newFilteredData = filterData(data, selectedFilterOptions);
      setFilteredData(newFilteredData);
      sortArticles();
      setFilterNow(false);
    }
  }, [filterNow]);

  useEffect(() => {
    sortArticles();
  }, [selectedSortOption]);

  return (
    <>
      <ResultHeader
        dateModified={data.lastUpdated}
        selectedFilterOptions={selectedFilterOptions}
        setSelectedFilterOptions={setSelectedFilterOptions}
        setFilterNow={setFilterNow}
        selectedSortOption={selectedSortOption}
        setSelectedSortOption={setSelectedSortOption}
        categoryOptions={defaultCategoryOptions}
      />
      <ResultsViewer data={filteredData} />
    </>
  );
}

export default Result;
