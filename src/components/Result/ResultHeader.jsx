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
  dateModified,
}) {
  const formatDate = (dateString) => {
    const options = { day: '2-digit', month: 'short', year: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-GB', options);
  };
  const dateString = `Last Modified ${formatDate(dateModified)}`;
  return (
    <div className="px-10 fixed top-[160px] md:top-[110px] right-0 left-0 z-10">
      <div className="flex flex-row justify-between">
        <div className="flex flex-row">
          <div>
            <p className="px-3 font-semibold text-gray-500">Results</p>
            <hr className="border-red border-t-2" />
          </div>
          <div className="flex place-items-end">
            <p className="font-light italic text-xs px-5 pb-1 text-gray-500">
              {dateString}
            </p>
            <hr className="border-t-2" />
          </div>
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
