import React, { useState, useRef, useEffect } from 'react';
import { IoChevronDownOutline, IoConstructOutline } from 'react-icons/io5';

function DateFilter({ selectedFilterOptions, setSelectedFilterOptions }) {
  const dateOptions = [
    'all time',
    'today',
    'past 7 days',
    'past 30 days',
    'past 60 days',
    'past 90 days',
    'past 180 days',
    'past year',
  ];

  const [isDateFilterOpen, setIsDateFilterOpen] = useState(false);
  const dropdownRef = useRef(null);

  useEffect(() => {
    function handleClickOutside(event) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsDateFilterOpen(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  const toggleDropdown = () => setIsDateFilterOpen(!isDateFilterOpen);

  const capitaliseWords = (option) => {
    const capitalizedWords = option
      .split(' ')
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1));
    return capitalizedWords.join(' ');
  };

  const handleDateChange = (value) => {
    setIsDateFilterOpen(false);
    setSelectedFilterOptions((prevState) => ({
      ...prevState,
      date: value,
    }));
  };

  return (
    <div className="my-3 m-2" ref={dropdownRef}>
      <p className="text-xs text-gray-500 font-semibold mb-2">Date</p>
      <button
        id="dateFilterButton"
        type="button"
        onClick={toggleDropdown}
        className="block text-sm text-gray-700 border rounded-md border-gray-200 p-2 text-sm text-gray-900 flex flex-rows w-full justify-between"
      >
        {capitaliseWords(selectedFilterOptions.date)}
        <IoChevronDownOutline className="mt-1" />
      </button>
      {isDateFilterOpen && (
        <div className=" mb-2 absolute w-[214.67px] rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none ">
          <div className="" role="none">
            {dateOptions.map((option) => (
              <div
                id={option}
                onClick={() => handleDateChange(option)}
                name="date"
                // checked={selectedFilterOptions.date.includes(option)}
                // onChange={handleCheckboxChange}
                className={`accent-sky-900 text-sm px-2 py-1.5 rounded-md ${
                  selectedFilterOptions.date === option
                    ? 'bg-sky-900 text-white'
                    : 'text-gray-900'
                }`}
              >
                {capitaliseWords(option)}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default DateFilter;
