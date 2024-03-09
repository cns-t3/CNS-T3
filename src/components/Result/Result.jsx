'use client';

import React, { useState, useEffect } from 'react';
import ResultHeader from './ResultHeader';
import ResultsViewer from './ResultsViewer';

function Result({ data }) {
  const [filterNow, setFilterNow] = useState(false);
  const [selectedFilterOptions, setSelectedFilterOptions] = useState({
    riskRating: ['low', 'medium', 'high'],
    category: [
      'source of wealth',
      'family circumstances',
      'sanctioned countries',
      'sensitive industries',
      'others',
    ],
    date: 'all time',
    identityMatch: 0,
  });

  const [filteredData, setFilteredData] = useState(data);

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
        return [];
      default:
        return [];
    }

    return [startDate, endDate];
  };

  useEffect(() => {
    const filterData = (currentData, filterOptions) => {
      const riskRatingOptions = filterOptions.riskRating;
      const categoryOptions = filterOptions.category;
      const dateOption = filterOptions.date;
      const identityMatchOption = selectedFilterOptions.identityMatch;

      const dates = processDateOption(dateOption);

      let filteredArticles;

      if (
        riskRatingOptions.length === 3
        && categoryOptions.length === 5
        && dateOption === 'all time'
        && identityMatchOption === 0
      ) {
        return currentData;
      }
      // var filteredArticles = data;
      if (dateOption === 'all time') {
        filteredArticles = data.newsArticles.filter(
          (article) => riskRatingOptions.includes(article.risk_rating.toLowerCase())
          && categoryOptions.includes(article.category.toLowerCase())
          && identityMatchOption < article.score,
        );
      } else {
        filteredArticles = data.newsArticles.filter(
          (article) => riskRatingOptions.includes(article.risk_rating.toLowerCase())
            && categoryOptions.includes(article.category.toLowerCase())
            && new Date(article.publishedAt) > dates[0]
            && new Date(article.publishedAt) < dates[1]
            && identityMatchOption < article.score,
        );
      }
      return {
        ...currentData,
        newsArticles: filteredArticles,
      };
    };

    if (filterNow) {
      const newFilteredData = filterData(data, selectedFilterOptions);
      setFilteredData(newFilteredData);
      setFilterNow(false);
    }
  }, [filterNow, data, selectedFilterOptions]);

  return (
    <>
      <ResultHeader
        selectedFilterOptions={selectedFilterOptions}
        setSelectedFilterOptions={setSelectedFilterOptions}
        setFilterNow={setFilterNow}
      />
      <ResultsViewer data={filteredData} />
    </>
  );
}

export default Result;
