import React from 'react';

function RiskChart({
  riskRatingPercentages,
}) {
  function getTailwindWidthClass(percentage) {
    const clampedPercentage = Math.max(0, Math.min(100, percentage));
    return `w-[${clampedPercentage}%]`;
  }
  return (
    <div className="h-5">
      <div className={`h-full ${getTailwindWidthClass(riskRatingPercentages.low)}`} />
      <div className={`h-full ${getTailwindWidthClass(riskRatingPercentages.medium)}`} />
      <div className={`h-full ${getTailwindWidthClass(riskRatingPercentages.high)}`} />
    </div>
  );
}

export default RiskChart;
