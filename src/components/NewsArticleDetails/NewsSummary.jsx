import React from 'react';

export default function NewsSummary({ article, onClose }) {
  return (
    <div className="flex flex-row p-8">
      <button
        type="button"
        className="text-red transition duration-300 ease-in-out pr-4"
        onClick={onClose}
        aria-label="Close"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="red"
          transform="rotate(180, 0,0)"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M15 19l-7-7 7-7"
          />
        </svg>
      </button>
      <div className="flex flex-col">
        {/* Article Header */}
        <div className="flex items-center">
          <h1 className="text-xl font-bold text-gray-800">{article.title}</h1>
        </div>
        <div className="pt-4">
          <p className="font-semibold text-sm">Risk Justification:</p>
          <p className="text-gray-600 text-sm pt-2">{article.risk_justification}</p>
        </div>
        {/* Summary with smaller font */}
        <div className="pt-4">
          <p className="font-semibold text-sm">Summary:</p>
          <p className="text-gray-600 text-sm pt-2">{article.summary}</p>
        </div>
        {/* Content with a top border as a divider and smaller font */}
        {/* <div className="mt-4 pt-4 border-t border-blue-300">
          <p className="text-gray-600 text-sm whitespace-pre-wrap">
            {article.content}
          </p>
        </div> */}
        {/* Read More Link */}
        <div className="pt-4">
          <div>
            <p className="font-semibold text-sm">Source URL:</p>
            <a
              href={article.source_url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-gray-600 hover:text-gray-800 text-sm underline transition duration-300 ease-in-out"
            >
              {article.source_url}
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
