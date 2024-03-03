import React from 'react';
import Image from 'next/image';
import Result from "@/components/Result/Result";
import SmallSearchBar from "@/components/Search/SmallSearchBar";

async function getData(query) {
  const url = `http://127.0.0.1:8000/search?search_query=${query}`;
  try {
    const res = await fetch(url, { cache: 'no-store' });
    if (!res.ok) {
      throw new Error('Failed to fetch data');
    }
    return res.json();
  } catch {
    return null;
  }
}

export default async function Search({ params }) {
  const query = decodeURIComponent(params.query);
  const data = await getData(query);

  return (
    <div>
      <div className="flex md:flex-row flex-col m-6 items-center justify-center">
        <Image
          width={1000}
          height={1000}
          className="md:w-2/12 sm:w-1/3 w-1/2 m-3"
          src="/logo.png"
        />
        <SmallSearchBar initialValue={query} />
      </div>
      <div className="flex md:flex-row flex-col m-6 items-center justify-center" />
      {data === null ? <></> : <Result data={data} />}
    </div>
  );
}
