import Image from "next/image";

const Profile = ({ profileDetails }) => {
  return (
    <div className="col-span-1 p-8">
      <div className="grid grid-cols-2 gap-1 ">
        <div className="">
          <img
            src={profileDetails.img_url}
            alt="Profile image"
            className="object-cover w-3/4 h-full"
          />
        </div>
        <div>
          <h2 className="text-xl font-bold text-gray-900 my-1">
            {profileDetails.name}
          </h2>
          <p className="text-sm mb-5">
            {profileDetails.occupation}, at {profileDetails.company}
          </p>
          {profileDetails.dob !== "" && (
            <p className="text-gray-500 text-sm">Born: {profileDetails.dob}</p>
          )}
          {profileDetails.nationality !== "" && (
            <p className="text-gray-500 text-sm">
              Nationality: {profileDetails.nationality}
            </p>
          )}
        </div>
      </div>
      <div className="text-sm mt-5">{profileDetails.description}</div>
    </div>
  );
};

export default Profile;
