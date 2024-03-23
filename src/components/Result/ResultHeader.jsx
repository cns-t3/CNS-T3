import React from 'react';
import FilterButton from '../Filter/FilterButton';
import SortButton from '../Sort/SortButton';

function ResultHeader({
  selectedFilterOptions,
  setSelectedFilterOptions,
  setFilterNow,
  selectedSortOption,
  setSelectedSortOption,
  categoryOptions,
}) {
  return (
    <div className="px-10 fixed top-[160px] md:top-[110px] right-0 left-0 z-10">
      <div className="flex flex-row justify-between">
        <div>
          <p className="px-3 font-semibold text-gray-500">Results</p>
          <hr className="border-red border-t-2" />
        </div>
        <div className="flex flex-row relative">
          <SortButton
            selectedSortOption={selectedSortOption}
            setSelectedSortOption={setSelectedSortOption}
          />
          <FilterButton
            selectedFilterOptions={selectedFilterOptions}
            setSelectedFilterOptions={setSelectedFilterOptions}
            setFilterNow={setFilterNow}
            categoryOptions={categoryOptions}
          />
        </div>
      </div>
      <hr className=" mb-5" />
    </div>
  );
}

export default ResultHeader;
