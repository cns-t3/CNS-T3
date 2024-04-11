'use client';

import React, { useEffect, useState } from 'react';
import Profile from '../Profile/Profile';
import Analytics from '../Analytics/Analytics';

function PersonOverview({
  personData,
  analyticsData,
  showAnalytics,
}) {
  const [showMore, setShowMore] = useState(false);

  useEffect(() => {
    const handleResize = () => {
      const tailwindMdBreakpoint = 768;
      if (window.innerWidth >= tailwindMdBreakpoint) {
        setShowMore(true);
      } else {
        setShowMore(false);
      }
    };

    handleResize();
  }, []);

  return (
    <div className="flex flex-col">
      <Profile profileDetails={personData} showMore={showMore} setShowMore={setShowMore} />
      {showAnalytics && showMore && <Analytics analyticsData={analyticsData} />}
      {showMore && (
        <button
          className="text-xs font-bold pb-4 underline cursor-pointer text-sky-800"
          onClick={() => setShowMore(false)}
          type="button"
        >
          Show Less
        </button>
      )}
    </div>
  );
}

export default PersonOverview;
