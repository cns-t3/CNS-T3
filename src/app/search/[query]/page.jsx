import React from 'react';
import Image from 'next/image';
import Result from '@/components/Result/Result';
import SmallSearchBar from '@/components/Search/SmallSearchBar';

async function getData(query) {
  const searchDNS = process.env.NEXT_PUBLIC_SEARCH_DNS || '127.0.0.1';
  const url = `http://${searchDNS}:8000/search?search_query=${query}`;
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
      <div className="flex md:flex-row flex-col p-6 pb-3 items-center justify-center top-0 left-0 right-0 fixed">
        <a href="/" className="w-1/6" id="logoLink" aria-label="Home">
          <Image
            layout="responsive"
            width={800}
            height={800}
            className="m-3"
            src="/logo.png"
          />
        </a>
        <SmallSearchBar initialValue={query} />
      </div>
      <div className="flex md:flex-row flex-col p-6 pt-0 items-center justify-center" />
      {data === null ? (
        <p className="m-6">
          No Results Found
        </p>
      ) : <Result data={data} />}
    </div>
  );
}
