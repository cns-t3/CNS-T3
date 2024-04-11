import React from 'react';
import RiskChart from './RiskChart';
import CategoryChart from './CategoryChart';
import IdentityMatchChart from './IdentityMatchChart';
import Summary from './Summary';

function Analytics({
  analyticsData,
}) {
  return (
    <div className="px-8">
      <div className="text-base font-bold">
        Overview
      </div>
      <RiskChart riskRatingPercentages={analyticsData.risks} />
      <div className=" w-full flex sm:flex-row lg:flex-col flex-col">
        <IdentityMatchChart identityData={analyticsData.identityScores} />
        <CategoryChart categoryData={analyticsData.categories} />
      </div>
      {analyticsData.summary !== '' && <Summary summary={analyticsData.summary} />}
    </div>
  );
}

export default Analytics;
