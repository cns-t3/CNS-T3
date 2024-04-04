import React from 'react';

function DiagramLabel({
  label,
}) {
  return (
    <div className="flex flex-row text-xs p-2 ">
      <div className="rounded-full w-3 h-3 bg-black self-center mr-1" />
      <div>{ label }</div>
    </div>
  );
}

export default DiagramLabel;
