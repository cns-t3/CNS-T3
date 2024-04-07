import React from 'react';
import RiskChart from './RiskChart';
import CategoryChart from './CategoryChart';
import IdentityMatchChart from './IdentityMatchChart';
import Summary from './Summary';

function Analytics({
  analyticsData,
}) {
  return (
    <div className="p-8 pt-0">
      <div className="text-base font-bold">
        Overview
      </div>
      <RiskChart riskRatingPercentages={analyticsData.risks} />
      <IdentityMatchChart identityData={analyticsData.identityScores} />
      <CategoryChart categoryData={analyticsData.categories} />
      <Summary summary={analyticsData.summary} />
    </div>
  );
}

export default Analytics;
