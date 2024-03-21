import React from 'react';
import Image from 'next/image';
import SearchBar from '@/components/Search/SearchBar';
import SimilarPeople from '@/components/Search/SimilarPeople';

// function getSimilarPeople(name) {
//   const personDNS = process.env.NEXT_PUBLIC_PERSON_DNS || '127.0.0.1';
//   const url = `http://${personDNS}:8001/person/similar_search?name=${name}`;
//   fetch(url)
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error('Network response was not ok');
//       }
//       return response.json(); // Correctly return the promise from response.json()
//     })
//     .then(data => {
//       console.log(data); // Now you can log the actual data
//       return data; // If you need to use the data outside, you need to handle this promise
//     })
//     .catch(() => null);
// }
export default function Home() {
  return (
    <div className="flex h-screen justify-center items-center">
      <div className="w-full flex-col flex justify-center items-center">
        <Image
          width={1000}
          height={1000}
          className="md:w-1/4 sm:w-1/3 w-1/2 m-3"
          src="/logo.png"
        />
        <SearchBar />
        {/* {similarPeople.length !== 0 && (
          <SimilarPeople
            similarPeople={similarPeople}
          />
        )} */}
      </div>
    </div>
  );
}
