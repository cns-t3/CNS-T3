CREATE DATABASE IF NOT EXISTS `CNS-T3`;
USE `CNS-T3`;

-- Drop tables if they exist
DROP TABLE IF EXISTS `Person-Company`;
DROP TABLE IF EXISTS Person;
DROP TABLE IF EXISTS Company;


-- Create the Person table
CREATE TABLE Person (
    PersonID int PRIMARY KEY,
    Name varchar(50),
    Occupation varchar(25),
    DoB date,
    Nationality varchar(25),
    Description varchar(255),
    CountryOfResidency varchar(50),
    PEPStatus boolean,
    SourceOfWealth varchar(25),
    ImgURL varchar(255)
);

-- Create the Company table
CREATE TABLE Company (
    CompanyID int PRIMARY KEY,
    Name varchar(100),
    Industry varchar(25),
    CountryOfHeadquarters varchar(50),
    Type varchar(25)
);

-- Create the Person-Company table
CREATE TABLE `Person-Company` (
    PersonID int,
    CompanyID int,
    Role varchar(25),
    PRIMARY KEY (PersonID, CompanyID),
    FOREIGN KEY (PersonID) REFERENCES Person(PersonID),
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);

-- Insert data into the Person table for Tim Cook
INSERT INTO Person (PersonID, Name, DoB, CountryOfResidency, Nationality, Occupation, PEPStatus, SourceOfWealth, Description, ImgURL)
VALUES 
    (1, 'Anthony Tan', '1982-12-01', 'Singapore', 'Singaporean', 'CEO', NULL, 'Grab', "Anthony Tan is the co-founder and former CEO of Grab, a prominent Southeast Asian technology company offering ride-hailing, food delivery, and financial services. Tan played a pivotal role in establishing Grab as a leading super app in the region, transforming it into a multi-billion-dollar company. He is recognized for his entrepreneurial vision and leadership in navigating Grab's expansion and innovation in various sectors across Southeast Asia.", NULL),
    (2, 'Goh Cheng Liang', '1928-01-01', 'Singapore', 'Singaporean', 'Businessman', NULL, 'Paint Manufacturing', NULL, NULL),
    (3, 'Zhang Yong', '1974-01-01', 'Singapore', 'Singaporean', 'Co-founder and Chairman', NULL, 'Haidilao International Holding Ltd.', NULL, NULL),
    (4, 'Helen Wong', '1961-06-01', 'Singapore', NULL, 'CEO', NULL, 'Banking and Finance', NULL, NULL),
    (5, 'Chee Koon Lee', NULL, 'Singapore', NULL, 'CEO', NULL, 'Real Estate', NULL, NULL);

-- Insert data into the Company table for Grab, OCBC, and CapitaLand
INSERT INTO Company (CompanyID, Name, Industry, CountryofHeadquarters, Type)
VALUES 
    (1, 'Grab', 'Technology', 'Singapore', 'Private'),
    (2, 'Wuthelam Holdings','Paint Manufacturing', 'Singapore', 'Private'),
    (3, 'OCBC', 'Banking', 'Singapore', 'Public'),
    (4, 'CapitaLand', 'Real Estate', 'Singapore', 'Public'),
    (5, 'Hai Di Lao', 'Hospitality', 'China', 'Private');


-- Insert data into the Person-Company table to link the individuals with their respective companies
INSERT INTO `Person-Company` (PersonID, CompanyID, Role)
VALUES 
    (1, 1, 'CEO'), 
    (2, 2, 'Founder'), 
    (3, 5, 'Co-founder and Chairman'), 
    (4, 3, 'CEO'),
    (5, 4, 'CEO');