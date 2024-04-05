import React from 'react';
import Profile from '../Profile/Profile';
import Analytics from '../Analytics/Analytics';

function PersonOverview({
  personData,
  analyticsData,
}) {
  return (
    <div className="flex flex-col">
      <Profile profileDetails={personData} />
      <Analytics analyticsData={analyticsData} />
    </div>
  );
}

export default PersonOverview;
