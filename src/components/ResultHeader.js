import React from 'react';
import FilterButton from './FilterButton';
import SortButton from './SortButton';

function ResultHeader({
  selectedFilterOptions,
  setSelectedFilterOptions,
  setFilterNow,
}) {
  return (
    <div className="px-10">
      <div className="flex flex-row justify-between">
        <div>
          <p className="px-3 font-semibold text-gray-500">Results</p>
          <hr className="border-red border-t-2" />
        </div>
        <div className="flex flex-row">
          <SortButton />
          <FilterButton
            selectedFilterOptions={selectedFilterOptions}
            setSelectedFilterOptions={setSelectedFilterOptions}
            setFilterNow={setFilterNow}
          />
        </div>
      </div>
      <hr className=" mb-5" />
    </div>
  );
}

export default ResultHeader;
