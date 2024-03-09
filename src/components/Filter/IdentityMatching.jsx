import React, { useState } from 'react';

function IdentityMatchingFilter({
  selectedFilterOptions,
  setSelectedFilterOptions,
}) {
  const [isInputInvalid, setInputInvalid] = useState(false);

  const handleInput = (e) => {
    const newIdentityMatch = e.target.value;

    if (newIdentityMatch >= 0 && newIdentityMatch < 100) {
      setInputInvalid(false);
      setSelectedFilterOptions((prevState) => ({
        ...prevState,
        identityMatch: newIdentityMatch,
      }));
    } else {
      setInputInvalid(true);
    }
  };

  return (
    <div className="my-3 m-2">
      <p className="text-xs text-gray-500 font-semibold mb-2">Identity Match</p>
      <div className="text-sm text-gray-900">
        <span className="self-center">Above</span>
        <input
          id="identityMatchFilter"
          type="number"
          value={selectedFilterOptions.identityMatch}
          onChange={handleInput}
          className="border border-gray-200 rounded-md mx-3 p-1.5 w-[60px] focus:outline-none"
        />
        <span className="self-center">%</span>
      </div>
      {isInputInvalid && (
        <div className="text-xs text-red mt-2">
          Please enter a number from 0 to 99
        </div>
      )}
    </div>
  );
}

export default IdentityMatchingFilter;
