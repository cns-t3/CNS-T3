import React from "react";
import NewsArticle from "../../components/NewsArticle";

const SearchPage = () => {
  return (
    <div>
      <NewsArticle
        title="Apple CEO Tim Cook Takes Steep Pay Cut, as Expected"
        publishedAt="2024-01-11T22:30:09Z"
        summary="Tim Cook has been Apple's CEO since Steve Jobs' resignation in 2011. He has a history of work at IBM and Compaq, and under his leadership, Apple has focused on supply chain management and strategic product range reduction."
        score={0.8}
        riskRating="low"
        tag="BUSINESS"
        publisher="The Straits Times"
      />
    </div>
  );
};

export default SearchPage;
