"use client";
import React, { useRef, useEffect } from "react";

const NewsArticle = ({ articleDetails }) => {
  // Format the date
  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString("en-SG", {
      day: "2-digit",
      month: "short",
      year: "numeric",
      timeZone: "Asia/Singapore",
    });
  };

  return (
    <div
      id="news-article-container"
      className="flex justify-between items-center bg-white px-4 py-5 shadow rounded-lg relative my-5"
    >
      <div className="flex-1 pr-3">
        <p
          id="article-tag"
          className="text-xs font-semibold text-gray-500 border border-gray-300 rounded px-2 py-1 mb-2 block md:hidden w-min"
        >
          {articleDetails.tag}
        </p>
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
          <p
            id="article-tag-hidden"
            className="text-xs font-semibold text-gray-500 border border-gray-300 rounded px-2 py-1 ml-5 hidden md:block"
          >
            {articleDetails.tag}
          </p>
        </div>
        <p id="article-summary" className="text-gray-500 text-sm line-clamp-2">
          {formatDate(articleDetails.publishedAt)} — "{articleDetails.summary}"
        </p>
      </div>
    </div>
  );
};

export default NewsArticle;
