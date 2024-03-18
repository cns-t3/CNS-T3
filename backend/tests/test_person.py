import unittest
from datetime import datetime
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest import mock
from backend.api.personAPI.sqlalchemy_models import Person, PersonCompany, Company, Base
from backend.api.personAPI.main import app
from backend.api.personAPI.database import get_db
from contextlib import contextmanager

# Create a temp database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


class TestPersonAPI(unittest.TestCase):
    def setUp(self):
        Base.metadata.create_all(bind=engine)
        person_data = {
            "Name": "John Doe",
            "Occupation": "Developer",
            "DoB": datetime(1990, 1, 1).date(),
            "Nationality": "American",
            "Description": "Test Description",
            "CountryOfResidency": "USA",
            "PEPStatus": False,
            "SourceOfWealth": "Salary",
            "ImgURL": "test.jpg",
        }
        company_data = {
            "Name": "Grab",
            "Industry": "Technology",
            "CountryOfHeadquarters": "Singapore",
            "Type": "Private",
        }
        person_company_data = {"PersonID": 0, "CompanyID": 0, "Role": "Developer"}

        self.client = TestClient(app)
        app.dependency_overrides[get_db] = override_get_db
        with override_get_db() as db:
            person = Person(**person_data)
            db.add(person)
            db.commit()
            company = Company(**company_data)
            db.add(company)
            db.commit()
            person_company = PersonCompany(**person_company_data)
            db.add(person_company)
            db.commit()

    def tearDown(self):
        engine.dispose()

    # Mock the function that interacts with the database
    @mock.patch("backend.api.personAPI.main.search_person_by_name")
    def test_search_persons_by_name(self, mock_search_person_by_name):
        # Define the mock behavior
        date = datetime(1990, 1, 1).date()
        mock_search_person_by_name.return_value = (
            Person(
                PersonID=1,
                Name="John Doe",
                Occupation="Developer",
                DoB=date,
                Nationality="American",
                Description="Test Description",
                CountryOfResidency="USA",
                PEPStatus=False,
                SourceOfWealth="Salary",
                ImgURL="test.jpg",
            ),
            "Test Company",
            "Developer",
        )

        # Make a request to the endpoint
        response = self.client.get("/persons/search/?name=John")

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the response content
        self.assertEqual(
            response.json(),
            {
                "person_id": 1,
                "name": "John Doe",
                "occupation": "Developer",
                "role": "Developer",
                "dob": "1990-01-01",
                "nationality": "American",
                "description": "Test Description",
                "company": "Test Company",
                "country_of_residency": "USA",
                "pep_status": False,
                "source_of_wealth": "Salary",
                "img_url": "test.jpg",
            },
        )

    # Test when name is not provided
    def test_search_persons_by_name_missing_name(self):
        response = self.client.get("/persons/search/")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Name parameter is required"})

    # Test when no persons found with the provided name
    @mock.patch("backend.api.personAPI.main.search_person_by_name")
    def test_search_persons_by_name_no_person_found(self, mock_search_person_by_name):
        mock_search_person_by_name.return_value = (None, None, None)
        response = self.client.get("/persons/search/?name=Unknown")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            {"detail": "No persons found with the provided name"},
        )


if __name__ == "__main__":
    unittest.main()
