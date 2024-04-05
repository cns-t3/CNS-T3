import React from 'react';
import LegendLabel from './LegendLabel';

function RiskChart({ riskRatingPercentages }) {
  // A helper function to determine if a risk rating is the first visible one.
  const isFirstVisible = (rating) => {
    const firstNonZero = ['low', 'medium', 'high'].find((key) => riskRatingPercentages[key] > 0);
    return rating === firstNonZero;
  };

  // Similarly, a helper function to determine if a risk rating is the last visible one.
  const isLastVisible = (rating) => {
    const lastNonZero = ['high', 'medium', 'low'].find((key) => riskRatingPercentages[key] > 0);
    return rating === lastNonZero;
  };

  // Adjust the getTailwindWidthClass to include rounded corners conditionally.
  // Also, use inline style for the width to avoid issues with dynamic classes in Tailwind CSS.
  const getTailwindWidthClass = (percentage, rating) => {
    const clampedPercentage = Math.max(0, Math.min(100, percentage));
    let classes = 'h-full';
    if (clampedPercentage > 0) {
      if (isFirstVisible(rating)) {
        classes += ' rounded-l-md';
      }
      if (isLastVisible(rating)) {
        classes += ' rounded-r-md';
      }
    }
    return classes;
  };

  // Apply the background colors as Tailwind classes.
  const getColorClass = (rating) => {
    const colorClasses = {
      low: 'bg-green',
      medium: 'bg-orange',
      high: 'bg-red',
    };
    return colorClasses[rating] || '';
  };

  return (
    <div className="py-3">
      <div className="text-sm text-textgrey font-semibold py-2">
        Risk
      </div>
      <div className="h-5 flex flex-row">
        <div
          style={{ width: `${riskRatingPercentages.low}%` }}
          className={`${getTailwindWidthClass(riskRatingPercentages.low, 'low')} ${getColorClass('low')}`}
        />
        <div
          style={{ width: `${riskRatingPercentages.medium}%` }}
          className={`${getTailwindWidthClass(riskRatingPercentages.medium, 'medium')} ${getColorClass('medium')}`}
        />
        <div
          style={{ width: `${riskRatingPercentages.high}%` }}
          className={`${getTailwindWidthClass(riskRatingPercentages.high, 'high')} ${getColorClass('high')}`}
        />
      </div>
      <div className="flex mt-2 ">
        <LegendLabel label="Low" colour="green" />
        <LegendLabel label="Medium" colour="orange" />
        <LegendLabel label="High" colour="red" />
      </div>
    </div>
  );
}

export default RiskChart;
