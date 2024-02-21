'use client';

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import Image from 'next/image';

export default function SmallSearchBar({ initialValue }) {
  const [value, setValue] = useState(initialValue);
  const router = useRouter();
  const handleChange = (e) => {
    setValue(e.target.value);
  };

  const onSearchSubmit = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      router.push(`/search/${value}`);
    }
  };

  return (
    <div className="w-full md:mx-6 md:mt-6 pl-4 border-l-4 border-red flex justify-end items-center">
      <input
        type="text"
        id="large-input"
        defaultValue={value}
        onChange={handleChange}
        onKeyDown={onSearchSubmit}
        className="block w-full p-4 rounded-md  text-gray-700 bg-gray-100 lg:text-xl md:text-lg text-md sm:text-lg focus:outline-none caret-red-500"
      />
      <Image
        src="/search.svg"
        className="absolute mr-2 w-10"
        alt="Search Icon"
        width={1000}
        height={1000}
      />
    </div>
  );
}
