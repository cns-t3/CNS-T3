"use client";

import React from "react";
import RiskRating from "./RiskRating";
import Category from "./Category";

function NewsArticle({ articleDetails, onOpen }) {
  // Format the date
  const formatDate = (dateString) =>
    new Date(dateString).toLocaleDateString("en-SG", {
      day: "2-digit",
      month: "short",
      year: "numeric",
      timeZone: "Asia/Singapore",
    });

  return (
    <div
      id="news-article-container"
      className="flex justify-between items-center bg-white px-4 pb-5 rounded-lg relative my-2"
      onClick={() => onOpen(articleDetails)}
    >
      <div className="flex-1 pr-3">
        <Category categoryDetails={articleDetails.category}></Category>
        <p
          id="article-publisher"
          className="text-sky-800 text-xs font-bold uppercase"
        >
          {articleDetails.publisher}
        </p>
        <div className="flex items-center flex-row">
          <h2
            id="article-title"
            className="text-xl font-bold text-gray-900 my-1"
          >
            {articleDetails.title}
          </h2>
        </div>
        <p id="article-summary" className="text-gray-500 text-sm line-clamp-2">
          <span className="date">{formatDate(articleDetails.publishedAt)}</span> — "
          {articleDetails.summary}"
        </p>
      </div>
      <div className="flex items-center md:space-x-0 space-x-0 relative md:flex-row flex-col ">
        <RiskRating riskRating={articleDetails.risk_rating} />
      </div>
    </div>
  );
}

export default NewsArticle;
