'use client';

import { React, useState } from 'react';
import NewsArticle from '../NewsArticle/NewsArticle';
import NewsSummary from '../NewsArticleDetails/NewsSummary';
import PersonOverview from './PersonOverview';

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

  const analyticsData = {
    risks: {
      low: 60,
      medium: 30,
      high: 10,
    },
    categories: {
      'Source Of Wealth': 7,
      Others: 12,
      'Sensitive Industries': 1,
    },
    identityScores: {
      identity_0_19: 1,
      identity_20_39: 2,
      identity_40_59: 7,
      identity_60_79: 7,
      identity_80_100: 3,
    },
    summary: 'Grab Holdings Limited, a tech giant in Southeast Asia, went from an overpriced IPO to becoming profitable. The CEO and Co-Founder, Anthony Tan, discussed safety with Cambodia\'s Prime Minister at a forum. Co-founder Tan Hooi Ling is stepping down by year-end due to market challenges. Tan, with a background in Malaysia, focuses on social impact and aims for Grab to be triple bottom line. The company\'s innovative services like motorbike rides set it apart. Tan Hooi Ling is transitioning to an advisory role supported by Anthony Tan, recognizing her role in Grab\'s success.',
  };

  return (
    <div className="fixed top-[210px] md:top-[160px] z-0 h-[calc(100vh-180px)] overflow-y-auto">
      <div className="px-10">
        <div className="flex flex-col lg:flex-row w-full">
          <div
            className={`flex bg-beige rounded-md h-min lg:order-last lg:overflow-y-auto lg:h-[calc(100vh-180px)] ${
              articleDetails == null ? 'lg:w-1/3' : 'lg:w-1/2'
            }`}
          >
            {articleDetails == null && (
              <PersonOverview
                personData={data.person}
                analyticsData={analyticsData}
              />
            )}
            {articleDetails != null && (
              <NewsSummary
                article={articleDetails}
                onClose={handleArticleClose}
              />
            )}
          </div>
          <div
            id="news-articles-container"
            className={`flex flex-col pt-5 lg:pt-0 lg:overflow-y-auto lg:h-[calc(100vh-180px)] ${
              articleDetails == null
                ? 'lg:w-2/3 pr-4'
                : 'lg:w-1/2 lg:pr-4 hidden lg:flex'
            }`}
          >
            {data.newsArticles.length === 0 && (
              <div id="noArticles">No articles found.</div>
            )}
            {data.newsArticles.map((article) => (
              <NewsArticle
                articleDetails={article}
                onOpen={handleArticleOpen}
                key={article.news_id}
              />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default ResultsViewer;
