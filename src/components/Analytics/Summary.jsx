'use client';

import React from 'react';

function Summary({
  summary,
}) {
  return (
    <div className="py-2">
      <div className="text-sm text-textgrey font-semibold py-3">
        News Roundup
      </div>
      <div className="text-sm">
        {summary}
      </div>
    </div>
  );
}

export default Summary;
