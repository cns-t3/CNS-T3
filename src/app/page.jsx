import React from 'react';

async function getData() {
  const searchDNS = process.env.SEARCH_DNS || '127.0.0.1';
  const url = `http://${searchDNS}:8000/search?search_query=anthony%20tan`;
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

export default async function test() {
  const data = await getData();

  return <div><pre>{JSON.stringify(data, null, 2)}</pre></div>;
}
