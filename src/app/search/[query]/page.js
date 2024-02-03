import React from "react";

export default function Search({ params }) {
  const query = decodeURIComponent(params.query)
  return (
    <>
      <p>{query}</p>
    </>
  );
}
