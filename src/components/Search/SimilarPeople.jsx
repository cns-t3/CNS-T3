import React from 'react';

function SimilarPeople({
  similarPeople,
}) {
  if (!Array.isArray(similarPeople)) {
    return null;
  }
  return (
    <div className="p-5">
      <span className="text-sm">Did you mean: </span>
      {similarPeople.map((person) => (
        <div key={person}>
          {person.name}
          ,
          {person.role}
          of
          {person.company}
        </div>
      ))}
    </div>
  );
}

export default SimilarPeople;
