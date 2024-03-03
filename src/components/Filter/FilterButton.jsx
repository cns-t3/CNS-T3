import React, { useState, useRef, useEffect } from 'react';
import { IoFilterOutline } from 'react-icons/io5';
import CategoryFilter from './CategoryFilter';
import RiskRatingFilter from './RiskRatingFilter';
import DateFilter from './DateFilter';

function FilterButton({
  selectedFilterOptions,
  setSelectedFilterOptions,
  setFilterNow,
}) {
  const [isFilterOpen, setFilterOpen] = useState(false);

  const dropdownRef = useRef();

  useEffect(() => {
    function handleClickOutside(event) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setFilterOpen(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  const handleFilterOpen = () => {
    setFilterOpen((isOpen) => !isOpen);
  };

  const applyFilters = () => {
    setFilterNow(true);
    setFilterOpen(false);
  };

  const removeFilters = () => {
    setSelectedFilterOptions({
      riskRating: ['low', 'medium', 'high'],
      category: [
        'source of wealth',
        'family circumstances',
        'sanctioned countries',
        'sensitive industries',
        'others',
      ],
      date: 'all time',
    });
    setFilterNow(true);
    setFilterOpen(false);
  };

  return (
    <div className="relative inline-block text-left" ref={dropdownRef}>
      <button
        type="button"
        id="filterButton"
        className="flex flex-row text-gray-500 pr-3"
        onClick={handleFilterOpen}
      >
        <IoFilterOutline size={20} />
        <span className="text-sm pl-2">Filter</span>
      </button>
      {isFilterOpen && (
        <div className="absolute mt-[6px] right-0 bg-white rounded-md border border-gray-200 shadow-lg z-50 w-64 py-2 px-3">
          <form method="POST">
            <div className="mx-2 my-4 font-semibold">Filter By</div>

            <DateFilter
              selectedFilterOptions={selectedFilterOptions}
              setSelectedFilterOptions={setSelectedFilterOptions}
            />

            <hr className="m-2 my-5" />

            <RiskRatingFilter
              selectedFilterOptions={selectedFilterOptions}
              setSelectedFilterOptions={setSelectedFilterOptions}
            />

            <hr className="m-2 my-5" />

            <CategoryFilter
              selectedFilterOptions={selectedFilterOptions}
              setSelectedFilterOptions={setSelectedFilterOptions}
            />

            <div className="grid grid-cols-2 gap-2 m-2 mt-5">
              <button
                type="button"
                onClick={removeFilters}
                className="border-sky-800 border-1 border text-xs text-black px-3 py-2 rounded-md hover:bg-gray-300"
              >
                Reset
              </button>
              <button
                id="applyButton"
                type="button"
                onClick={applyFilters}
                className="bg-sky-800 text-xs text-white px-3 py-2 rounded-md hover:bg-sky-900"
              >
                Apply
              </button>
            </div>
          </form>
        </div>
      )}
    </div>
  );
}

export default FilterButton;
