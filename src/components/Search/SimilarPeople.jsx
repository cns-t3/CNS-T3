'use client';

import React, { useEffect, useState } from 'react';
import SearchTag from './SearchTag';

export default function SimilarPeople({
  query,
  setRouterStr,
  findPeople,
  setFindPeople,
  setDoSearch,
  setIsLoading,
  isSmall,
}) {
  const [similarPeopleArr, setSimilarPeopleArr] = useState([]);
  const [errorMsg, setErrorMsg] = useState('');

  useEffect(() => {
    const getSimilarPersonData = async (param) => {
      setFindPeople(false);
      setIsLoading(false);
      try {
        // const personDNS = process.env.NEXT_PUBLIC_PERSON_DNS || '127.0.0.1';
        // const response = await fetch(`http://${personDNS}:8001/persons/similar_search?name=${param}`);
        const response = await fetch(`/api/similar-person-search?name=${encodeURIComponent(param)}`);
        const data = await response.json();
        if (data.length > 0) {
          setSimilarPeopleArr(data);
        } else {
          setErrorMsg('The individual you searched for is not in the database.');
        }

        return null;
      } catch (error) {
        return null;
      }
    };

    const getPersonData = async (param) => {
      setErrorMsg('');
      try {
        // const personDNS = process.env.NEXT_PUBLIC_PERSON_DNS || '127.0.0.1';
        // const response = await fetch(`http://${personDNS}:8001/persons/search?name=${param}`);
        const response = await fetch(`/api/person?name=${encodeURIComponent(param)}`);
        const data = await response.json();
        if (data.length === 1) {
          setRouterStr(`${data[0].person_id}/${data[0].name}`);
          setDoSearch(true);
        } else if (data.length > 1) {
          setSimilarPeopleArr(data);
        } else if (data.length === 0) {
          getSimilarPersonData(param);
        }
        return null;
      } catch (error) {
        return null;
      }
    };

    if (findPeople === true) {
      getPersonData(query);
    }
  }, [findPeople]);

  return (
    <div className={isSmall ? 'px-1' : 'p-5'}>
      {similarPeopleArr.length > 0 ? (
        <div id="similarPeople" className="flex flex-row space-x-2 text-sm text-gray-700">
          <div className="italic">Did you mean: </div>
          <div className={isSmall ? 'p-0' : 'flex flex-col space-y-2'}>
            {similarPeopleArr.map((person) => (
              <SearchTag
                key={person.person_id}
                person={person}
                setRouterStr={setRouterStr}
                setDoSearch={setDoSearch}
              />
            ))}
          </div>
        </div>
      ) : (
        <div id="noSimilarPeople" className="text-red text-sm">
          { errorMsg }
        </div>
      )}
    </div>
  );
}
