const Profile = ({ name, position, details }) => (
  <div className="profile">
    <h3>{name}</h3>
    <p>{position}</p>
    {/* ... Iterate over details to display education, accolades, etc. ... */}
    {/* ... Add more HTML and CSS classes as needed to match your design ... */}
  </div>
);

export default Profile;
