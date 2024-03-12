'use client';

import { React, useState, useEffect } from 'react';
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
    date: 'all time',
  });
  const [filteredData, setFilteredData] = useState(data);
  const [selectedSortOption, setSelectedSortOption] = useState('Newest to Oldest');

  useEffect(() => {
    setSelectedFilterOptions((prevOptions) => ({
      ...prevOptions,
      category: defaultCategoryOptions,
    }));
  }, [defaultCategoryOptions]);

  // Sort by descending date
  const sortArticlesByDescendingDate = () => {
    setFilteredData((prevData) => {
      const sortedArticles = [...prevData.newsArticles].sort(
        (a, b) => new Date(a.publishedAt) - new Date(b.publishedAt),
      );
      return { ...prevData, newsArticles: sortedArticles };
    });
  };

  const sortArticlesByAscendingDate = () => {
    setFilteredData((prevData) => {
      const sortedArticles = [...prevData.newsArticles].sort(
        (a, b) => new Date(b.publishedAt) - new Date(a.publishedAt),
      );
      return { ...prevData, newsArticles: sortedArticles };
    });
  };

  const sortArticles = () => {
    if (selectedSortOption === 'Newest to Oldest') {
      sortArticlesByAscendingDate();
    } else {
      sortArticlesByDescendingDate();
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

    const dates = processDateOption(dateOption);

    if (
      riskRatingOptions.length === 3
      && categoryOptions.length === 5
      && dateOption === 'all time'
    ) {
      return inputData;
    }
    let filteredArticles = inputData;
    if (dateOption === 'all time') {
      filteredArticles = data.newsArticles.filter(
        (article) => riskRatingOptions.includes(article.risk_rating.toLowerCase())
          && categoryOptions.includes(article.category.toLowerCase()),
      );
    } else {
      filteredArticles = inputData.newsArticles.filter(
        (article) => riskRatingOptions.includes(article.risk_rating.toLowerCase())
          && categoryOptions.includes(article.category.toLowerCase())
          && new Date(article.publishedAt) > dates[0]
          && new Date(article.publishedAt) < dates[1],
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
        selectedFilterOptions={selectedFilterOptions}
        setSelectedFilterOptions={setSelectedFilterOptions}
        setFilterNow={setFilterNow}
        selectedSortOption={selectedSortOption}
        setSelectedSortOption={setSelectedSortOption}
      />
      <ResultsViewer data={filteredData} />
    </>
  );
}

export default Result;
