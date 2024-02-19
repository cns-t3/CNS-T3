import React from 'react';
import { useState, useRef, useEffect } from 'react';
import { IoFilterOutline } from 'react-icons/io5';

function FilterButton({
  selectedFilterOptions,
  setSelectedFilterOptions,
  setFilterNow,
}) {
  const [isFilterOpen, setFilterOpen] = useState(false);
  const options = ['low', 'medium', 'high'];
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

  const handleCheckboxChange = (e) => {
    const { name, value, checked } = e.target;
    setSelectedFilterOptions((prevState) => ({
      ...prevState,
      [name]: checked
        ? [...prevState[name], value]
        : prevState[name].filter((item) => item !== value),
    }));
  };

  const applyFilters = () => {
    setFilterNow(true);
    setFilterOpen(false);
  };

  const removeFilters = () => {
    setSelectedFilterOptions({
      riskRating: [],
      categories: [],
    });
    setFilterNow(true);
    setFilterOpen(false);
  };

  return (
    <div className="relative inline-block text-left" ref={dropdownRef}>
      <button
        id="filterButton"
        className="flex flex-row text-gray-500 pr-3"
        onClick={handleFilterOpen}
      >
        <IoFilterOutline size={20} />
        <span className="text-sm pl-2">Filter</span>
      </button>
      {isFilterOpen && (
        <div className="absolute mt-[6px] right-0 bg-white rounded-md border border-gray-200 shadow-lg z-50 w-64 py-2 px-3">
          <form>
            <div className="mx-2 my-4 font-semibold">Filter By</div>
            <div>
              <p className="text-xs m-2 text-gray-500 font-semibold">
                Risk Rating
              </p>
              {options.map((option) => (
                <label key={option} className="flex items-center space-x-2 m-2">
                  <input
                    type="checkbox"
                    value={option}
                    name="riskRating"
                    checked={selectedFilterOptions.riskRating.includes(option)}
                    onChange={handleCheckboxChange}
                    className="h-4 w-4 accent-sky-900 cursor-pointer"
                  />
                  <span className="text-sm text-gray-900">
                    {option.charAt(0).toUpperCase() + option.slice(1)}
                  </span>
                </label>
              ))}
            </div>

            <hr className="m-2 my-5" />

            {/* You can add category checkboxes similar to the riskRating ones here */}

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
