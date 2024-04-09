import React from 'react';
import Profile from '../Profile/Profile';
import Analytics from '../Analytics/Analytics';

function PersonOverview({
  personData,
  analyticsData,
  showAnalytics,
}) {
  return (
    <div className="flex flex-col">
      <Profile profileDetails={personData} />
      {showAnalytics}
      {showAnalytics && <Analytics analyticsData={analyticsData} />}
    </div>
  );
}

export default PersonOverview;
