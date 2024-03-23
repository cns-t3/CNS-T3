import React from 'react';

function SearchTag({
  setRouterStr,
  person,
  setDoSearch,
}) {
  const {
    person_id,
    name,
    role,
    company,
  } = person;
  const formatString = () => `${name}, ${role} of ${company}`;
  const handleClick = () => {
    const routerStr = `${person_id}/${name}`;
    setRouterStr(routerStr);
    setDoSearch(true);
  };

  return (
    <button type="button" className="text-sm text-sky-800 cursor-pointer underline" onClick={handleClick}>
      {formatString()}
    </button>
  );
}

export default SearchTag;
