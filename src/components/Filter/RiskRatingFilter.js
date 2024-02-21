const RiskRatingFilter = ({
    selectedFilterOptions,
    handleCheckboxChange,
  }) => {
    const riskRatingOptions = ["low", "medium", "high"];
  
    return (
        <div>
        <p className="text-xs m-2 text-gray-500 font-semibold">
          Risk Rating
        </p>
        {riskRatingOptions.map((option) => (
          <label key={option} className="flex items-center space-x-2 m-2">
            <input
              type="checkbox"
              value={option}
              name="riskRating"
              checked={selectedFilterOptions.riskRating.includes(option)}
              onChange={handleCheckboxChange}
              className="h-4 w-4 accent-sky-900 cursor-pointer"
            />
            <span className="text-sm text-gray-900">
              {option.charAt(0).toUpperCase() + option.slice(1)}
            </span>
          </label>
        ))}
      </div>
    );
  };
  
  export default RiskRatingFilter;
  