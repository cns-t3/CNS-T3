import React from 'react';
import RiskChart from './RiskChart';
import CategoryChart from './CategoryChart';
import IdentityMatchChart from './IdentityMatchChart';
import Summary from './Summary';

function Analytics({
  analyticsData,
}) {
  const newAnalyticsData = {};
  newAnalyticsData['Source of Wealth'] = 0;
  Object.entries(analyticsData.categories).forEach(([key]) => {
    if (key === 'Source of Wealth' || key === 'Source Of Wealth') {
      newAnalyticsData['Source of Wealth'] += analyticsData.categories[key];
    } else {
      newAnalyticsData[key] = analyticsData.categories[key];
    }
  });
  return (
    <div className="px-8">
      <div className="text-base font-bold">
        Overview
      </div>
      <RiskChart riskRatingPercentages={analyticsData.risks} />
      <div className=" w-full flex sm:flex-row lg:flex-col flex-col">
        <IdentityMatchChart identityData={analyticsData.identityScores} />
        <CategoryChart categoryData={newAnalyticsData} />
      </div>
      {analyticsData.summary !== '' && <Summary summary={analyticsData.summary} />}
    </div>
  );
}

export default Analytics;
