"use client";

import React from "react";
import { useState, useEffect } from "react";
import ResultHeader from "./ResultHeader";
import ResultsViewer from "./ResultsViewer";

function Result({ data }) {
  const [filterNow, setFilterNow] = useState(false);
  const [selectedFilterOptions, setSelectedFilterOptions] = useState({
    riskRating: ["low", "medium", "high"],
    category: [
      "source of wealth",
      "family circumstances",
      "sanctioned countries",
      "sensitive industries",
      "others",
    ],
  });
  const [filteredData, setFilteredData] = useState(data);

  useEffect(() => {
    if (filterNow) {
      const newFilteredData = filterData(data, selectedFilterOptions);
      setFilteredData(newFilteredData);
      setFilterNow(false);
    }
  }, [filterNow]);

  const filterData = (data, selectedFilterOptions) => {
    const riskRatingOptions = selectedFilterOptions.riskRating;
    const categoryOptions = selectedFilterOptions.category;
    console.log(riskRatingOptions)
    console.log(categoryOptions)

    if (riskRatingOptions.length == 3 && categoryOptions.length == 5) {
      return data;
    }
    const filteredArticles = data.newsArticles.filter(
      (article) =>
        riskRatingOptions.includes(article.risk_rating.toLowerCase()) &&
        categoryOptions.includes(article.category.toLowerCase())
    );

    return {
      ...data,
      newsArticles: filteredArticles,
    };
  };

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
