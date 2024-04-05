import React from 'react';
import RiskChart from './RiskChart';
import CategoryChart from './CategoryChart';
import IdentityMatchChart from './IdentityMatchChart';

function Analytics({
  analyticsData,
}) {
  return (
    <div className="p-8 pt-0">
      <div className="text-base font-bold">
        Summary
      </div>
      <RiskChart riskRatingPercentages={analyticsData.risks} />
      <IdentityMatchChart identityData={analyticsData.identityScores} />
      <CategoryChart categoryData={analyticsData.categories} />
    </div>
  );
}

export default Analytics;
