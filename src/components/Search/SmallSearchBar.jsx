'use client';

import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { MdOutlineSearch } from 'react-icons/md';
import SimilarPeople from './SimilarPeople';

import Spinner from './Spinner';

export default function SmallSearchBar({ initialValue }) {
  const [value, setValue] = useState(initialValue);
  const [routerStr, setRouterStr] = useState(0);
  const [findPeople, setFindPeople] = useState('');
  const [doSearch, setDoSearch] = useState();
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();
  const handleChange = (e) => {
    setValue(e.target.value);
  };

  const onSearchSubmit = (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      setIsLoading(true);
      setFindPeople(true);
    }
  };

  useEffect(() => {
    if (doSearch) {
      const updatedRouterPath = `/search/${routerStr.replace(/ /g, '%20')}`;
      if (window.location.pathname === updatedRouterPath) {
        window.location.reload();
      } else {
        router.push(`/search/${routerStr}`);
      }
    }
  }, [doSearch]);

  return (
    <div className="w-full md:mx-6">
      <div className="w-full pl-4 border-l-4 border-red">
        <div className="w-full p-4 rounded-md text-gray-700 bg-beige flex justify-between">
          <input
            type="text"
            id="small-input"
            defaultValue={value}
            autoComplete="off"
            onChange={handleChange}
            onKeyDown={onSearchSubmit}
            className="md:text-base text-sm bg-transparent w-4/5 focus:outline-none caret-red-500"
          />
          <div className="w-1/5 flex justify-end items-center">
            {isLoading ? (
              <Spinner />
            ) : (
              <MdOutlineSearch size={25} />
            )}
          </div>
        </div>
      </div>
      <div className="pl-8 py-1.5">
        <SimilarPeople
          query={value}
          setRouterStr={setRouterStr}
          findPeople={findPeople}
          setFindPeople={setFindPeople}
          setDoSearch={setDoSearch}
          setIsLoading={setIsLoading}
          isSmall
        />
      </div>
    </div>
  );
}
