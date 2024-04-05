import React from 'react';

function LegendLabel({
  label,
  colour,
}) {
  return (
    <div className="flex flex-row text-xs p-2">
      <div className="flex items-center mr-1 h-full">
        <div className={`rounded-full w-3 h-3 self-center bg-${colour}`} />
      </div>
      <div>{ label }</div>
    </div>
  );
}

export default LegendLabel;
