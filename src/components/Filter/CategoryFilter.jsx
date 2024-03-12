'use client';

import React, { useEffect, useState } from 'react';

function CategoryFilter({ selectedFilterOptions, setSelectedFilterOptions }) {
  const [categoryOptions, setCategories] = useState([]);

  useEffect(() => {
    fetch('/categories.json')
      .then((response) => response.json())
      .then((data) => {
        const categoryNames = Object.keys(data.categories).map((cat) => cat.toLowerCase());
        setCategories(categoryNames);
      });
  }, []);

  const handleCheckboxChange = (e) => {
    const { name, value, checked } = e.target;
    setSelectedFilterOptions((prevState) => ({
      ...prevState,
      [name]: checked
        ? [...prevState[name], value]
        : prevState[name].filter((item) => item !== value),
    }));
  };

  const capitaliseWords = (option) => {
    const capitalizedWords = option
      .split(' ')
      .map((word) => word.charAt(0).toUpperCase() + word.slice(1));
    return capitalizedWords.join(' ');
  };

  return (
    <div>
      <p className="text-xs m-2 text-gray-500 font-semibold">Category</p>
      {categoryOptions.map((option) => (
        <label
          htmlFor={option}
          key={option}
          className="flex items-center space-x-2 m-2"
        >
          <input
            type="checkbox"
            value={option}
            name="category"
            checked={selectedFilterOptions.category.includes(option)}
            onChange={handleCheckboxChange}
            className="h-4 w-4 accent-sky-900 cursor-pointer"
          />
          <span className="text-sm text-gray-900">
            {capitaliseWords(option)}
          </span>
        </label>
      ))}
    </div>
  );
}

export default CategoryFilter;
