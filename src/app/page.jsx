import React from 'react';

async function getData() {
  // const searchDNS = process.env.NEXT_PUBLIC_SEARCH_DNS || '127.0.0.1';
  // const searchDNS = '10.0.70.117';
  const searchDNS = 'localhost';
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
async function getPerson(name) {
  // const personHostname = '10.0.36.137';
  const personHostname = 'localhost';
  const url = `http://${personHostname}:8001/persons/search`;

  try {
    const params = new URLSearchParams({ name });
    const fullUrl = `${url}?${params.toString()}`;
    const res = await fetch(fullUrl, { cache: 'no-store' });

    if (!res.ok) {
      throw new Error(`Failed to fetch data: ${res.status} ${res.statusText}`);
    }

    const person = await res.json();
    return person;
  } catch (error) {
    return null;
  }
}

async function postIdentity(searchResultModelJson) {
  const identityHostname = 'localhost';
  const url = `http://${identityHostname}:8003/identity`;

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(searchResultModelJson),
    });

    if (!response.ok) {
      throw new Error(`Failed to post data: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    return null;
  }
}

async function getNews() {
  // const searchDNS = '10.0.114.249';
  const searchDNS = 'localhost';
  const url = `http://${searchDNS}:8002/news/anthony%20tan`;
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
  const searchData = await getData();
  const personData = await getPerson('Anthony Tan');
  const newsData = await getNews();
  const json = { person: personData, newsArticles: newsData };
  const identityData = await postIdentity(json);

  return (
    <div>
      <div>
        <h2>Search Data</h2>
        <pre>{JSON.stringify(searchData, null, 2)}</pre>
      </div>
      <div>
        <h2>Person Data</h2>
        <pre>{JSON.stringify(personData, null, 2)}</pre>
      </div>
      <div>
        <h2>News Data</h2>
        <pre>{JSON.stringify(newsData, null, 2)}</pre>
      </div>
      <div>
        <h2>Identity Data</h2>
        <pre>{JSON.stringify(identityData, null, 2)}</pre>
      </div>
    </div>
  );
}
