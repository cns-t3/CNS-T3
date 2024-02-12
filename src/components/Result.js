"use client";
import { useState, useEffect } from "react";
import ResultHeader from "./ResultHeader";
import ResultsViewer from "./ResultsViewer";

const Result = ({ data }) => {
  const [filterNow, setFilterNow] = useState(false);
  const [selectedFilterOptions, setSelectedFilterOptions] = useState({
    riskRating: [],
    categories: [],
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
    const filteredArticles = data.newsArticles.filter((article) =>
      riskRatingOptions.includes(article.risk_rating)
    );

    console.log({
      ...data,
      newsArticles: filteredArticles,
    });

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
      <ResultsViewer data={filteredData}></ResultsViewer>
    </>
  );
};

export default Result;
