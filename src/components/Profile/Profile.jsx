import React from 'react';

const formatDate = (inputDate) => {
  const dateObj = new Date(inputDate);

  if (Number.isNaN(dateObj.getTime())) {
    return 'Invalid Date';
  }

  const months = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec',
  ];

  const day = dateObj.getDate();
  const month = months[dateObj.getMonth()];
  const year = dateObj.getFullYear();

  return `${day} ${month} ${year}`;
};

function Profile({ profileDetails }) {
  const formattedDate = profileDetails.dob !== '' ? formatDate(profileDetails.dob) : '';

  return (
    <div id="profile-container" className="p-8">
      <div className="grid grid-cols-2 gap-1 ">
        <div id="profile-image-container" className="">
          <img
            src={profileDetails.img_url}
            alt="Profile Pic"
            className="object-cover w-3/4 h-full"
          />
        </div>
        <div>
          <h2
            id="profile-name"
            className="text-xl font-bold text-gray-900 my-1"
          >
            {profileDetails.name}
          </h2>
          <p id="profile-occupation" className="text-sm mb-5">
            {`${profileDetails.occupation}, at ${profileDetails.company}`}
          </p>
          {profileDetails.dob !== '' && (
            <p id="profile-dob" className="text-gray-500 text-sm">
              Born:
              {' '}
              {formattedDate}
            </p>
          )}
          {profileDetails.nationality !== '' && (
            <p id="profile-nationality" className="text-gray-500 text-sm">
              Nationality:
              {' '}
              {profileDetails.nationality}
            </p>
          )}
        </div>
      </div>
      <div id="profile-description" className="text-sm mt-5">
        {profileDetails.description}
      </div>
    </div>
  );
}

export default Profile;
