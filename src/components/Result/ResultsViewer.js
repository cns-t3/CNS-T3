'use client';

import { useState, useEffect } from 'react';
import NewsArticle from '../NewsArticle/NewsArticle';
import Profile from '../Profile/Profile';
import NewsSummary from '../NewsArticleDetails/NewsSummary';

function ResultsViewer({ data }) {
  const [articleDetails, setArticleDetails] = useState(null);
  const [scrollPosition, setScrollPosition] = useState(0);

  const handleArticleOpen = (article) => {
    setArticleDetails(article);
    setScrollPosition(document.documentElement.scrollTop);
    window.scrollTo({
      top: 0,
      left: 0,
      behavior: 'smooth',
    });
  };

  const handleArticleClose = () => {
    setArticleDetails(null);
    window.scrollTo({
      top: scrollPosition,
      behavior: 'smooth',
    });
  };

  return (
    <div>
      <div className="px-10">
        <div className="flex flex-col lg:flex-row w-full">
          <div
            className={`flex bg-beige rounded-md h-min lg:order-last ${
              articleDetails == null ? 'lg:w-1/3' : 'lg:w-1/2'
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
            className={`flex flex-col pt-5 lg:pt-0 ${
              articleDetails == null
                ? 'lg:w-2/3 pr-4'
                : 'lg:w-1/2 lg:pr-4 hidden lg:flex'
            }`}
          >
            {data.newsArticles.length == 0 && (
              <div id="noArticles">No articles match your filter criteria.</div>
            )}
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
