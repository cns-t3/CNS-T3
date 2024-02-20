"use client";

import { useState, useEffect } from "react";
import NewsArticle from "./NewsArticle";
import Profile from "./Profile";
import NewsSummary from "./NewsSummary";

function ResultsViewer({ data }) {
  const [articleDetails, setArticleDetails] = useState(null);
  const [scrollPosition, setScrollPosition] = useState(0);
  const [noArticlesMessage, setNoArticlesMessage] = useState("");

  const handleArticleOpen = (article) => {
    setArticleDetails(article);
    setScrollPosition(document.documentElement.scrollTop);
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: "smooth",
    });
  };

  const handleArticleClose = () => {
    setArticleDetails(null);
    window.scrollTo({
      top: scrollPosition,
      behavior: "smooth",
    });
  };

  useEffect(() => {
    if (data.length === 0) {
      setNoArticlesMessage("No articles match your filter criteria.");
    } else {
      setNoArticlesMessage("");
    }
  }, [data]);

  return (
    <div>
      <div className="px-10">
        <div className="flex flex-col lg:flex-row w-full">
          <div
            className={`flex bg-beige rounded-md h-min lg:order-last ${
              articleDetails == null ? "lg:w-1/3" : "lg:w-1/2"
            }`}
          >
            {articleDetails == null && <Profile profileDetails={data.person} />}
            {articleDetails != null && (
              <NewsSummary
                article={articleDetails}
                onClose={handleArticleClose}
              />
            )}
          </div>
          <div
            id="news-articles-container"
            className={`flex flex-col  ${
              articleDetails == null
                ? "lg:w-2/3 pr-4"
                : "lg:w-1/2 lg:pr-4 hidden lg:flex"
            }`}
          >
            {data.newsArticles.map((article, index) => (
              <NewsArticle
                articleDetails={article}
                onOpen={handleArticleOpen}
                key={index}
              />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default ResultsViewer;
