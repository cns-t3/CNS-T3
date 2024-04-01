import React, { useState, useRef, useEffect } from 'react';
import { IoChevronDownOutline } from 'react-icons/io5';

function SortDropDown({ selectedSortOption, setSelectedSortOption }) {
  const sortOptions = [
    'Newest to Oldest',
    'Oldest to Newest',
    'High to Low Risk',
    'Low to High Risk',
    'High to Low Identity Match',
    'Low to High Identity Match',
  ];
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const dropdownRef = useRef(null);

  useEffect(() => {
    function handleClickOutside(event) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsDropdownOpen(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  const toggleDropdown = () => setIsDropdownOpen(!isDropdownOpen);

  const handleSortChange = (value) => {
    setIsDropdownOpen(false);
    setSelectedSortOption(value);
  };

  return (
    <div className="my-3 m-2" ref={dropdownRef}>
      <button
        id="dropDownButton"
        type="button"
        onClick={toggleDropdown}
        className="border rounded-md border-gray-200 p-2 text-sm text-gray-900 flex flex-rows w-full justify-between"
      >
        {selectedSortOption}
        <IoChevronDownOutline className="mt-1" />
      </button>
      {isDropdownOpen && (
        <div className=" mb-2 absolute w-[214.67px] rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none ">
          <div className="" role="none">
            {sortOptions.map((option) => (
              <button
                type="button"
                id={option}
                onClick={() => handleSortChange(option)}
                name="date"
                className={`accent-sky-900 text-sm px-2 py-1.5 rounded-md w-full text-left ${
                  selectedSortOption === option
                    ? 'text-white bg-sky-900'
                    : 'text-gray-900'
                }`}
              >
                {option}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default SortDropDown;
