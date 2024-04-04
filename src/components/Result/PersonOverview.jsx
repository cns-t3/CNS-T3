import React from 'react';
import Profile from '../Profile/Profile';
import Analytics from '../Analytics/Analytics';

function PersonOverview({
  personData,
}) {
  return (
    <div className="flex flex-col">
      <Profile profileDetails={personData} />
      <Analytics />
    </div>
  );
}

export default PersonOverview;
