'use client';

import React from 'react';
import RiskRating from './RiskRating';
import Category from './Category';
import IdentityMatching from './IdentityMatching';

function NewsArticle({ articleDetails, onOpen }) {
  // Format the date
  const formatDate = (dateString) => new Date(dateString).toLocaleDateString('en-SG', {
    day: '2-digit',
    month: 'short',
    year: 'numeric',
    timeZone: 'Asia/Singapore',
  });

  return (
    <button
      id="news-article-container"
      className="flex justify-between items-center bg-white px-4 pb-5 rounded-lg relative my-2 text-left"
      onClick={() => onOpen(articleDetails)}
      type="button"
    >
      <div className="flex-1 pr-3">
        <Category categoryDetails={articleDetails.category} />
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
          <span className="date">{formatDate(articleDetails.publishedAt)}</span>
          {' '}
          — &quot;
          {articleDetails.summary}
          &quot;
        </p>
      </div>
      <div className="flex items-center relative md:flex-row flex-col md:space-x-3">
        <RiskRating
          riskRating={articleDetails.risk_rating}
          riskJustification={articleDetails.risk_justification}
        />
        <IdentityMatching score={articleDetails.score} />
      </div>
    </button>
  );
}

export default NewsArticle;
