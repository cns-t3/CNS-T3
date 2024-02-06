"use client";
import { useState } from "react";
import NewsArticle from "./NewsArticle";
import Profile from "./Profile";
import ArticleSum from "./ArticleSummaryBox";

const data = ({ json }) => {
  const [articleDetails, setArticleDetails] = useState(null);

  return (
    <div className="px-10">
      <hr className=" mb-5"></hr>
      <div className="flex flex-row w-full">
        <div
          className={`flex flex-col ${
            articleDetails == null ? "w-2/3" : "w-1/2"
          }`}
        >
          {json.newsArticles.map((article, index) => (
            <NewsArticle
              articleDetails={article}
              setArticleDetails={setArticleDetails}
              key={index}
            />
          ))}
        </div>
        <div
          className={`flex bg-beige rounded-md h-min ${
            articleDetails == null ? "w-1/3" : "w-1/2"
          }`}
        >
          {articleDetails == null && (
            <Profile profileDetails={json.profile} />
          )}
          {articleDetails != null && (
            <ArticleSum article={articleDetails} setArticleDetails={setArticleDetails}></ArticleSum>
          )}
        </div>
      </div>
    </div>
  );
};

export default data;