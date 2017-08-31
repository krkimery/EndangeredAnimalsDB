drop database if exists Endangered;
create database Endangered;
Use Endangered;
CREATE TABLE Endangered_Animal ( scientific_name VARCHAR(255) NOT NULL, common_name VARCHAR(255) NOT NULL, endangered_status CHAR(1) NOT NULL, animal_type CHAR(1) NOT NULL, PRIMARY KEY (Scientific_Name) );
CREATE TABLE Bird ( scientific_name VARCHAR(255) NOT NULL, migratory_status VARCHAR(255), CONSTRAINT bird_scientific_name FOREIGN KEY (scientific_name) REFERENCES Endangered_Animal (scientific_name), CONSTRAINT pk_Bird PRIMARY KEY (scientific_name) );
CREATE TABLE Continent ( continent_name VARCHAR(255) NOT NULL, PRIMARY KEY (continent_name) );
CREATE TABLE Animal_Range ( scientific_name VARCHAR(255) NOT NULL, continent_name VARCHAR(255) NOT NULL,  CONSTRAINT pk_animalcontinent PRIMARY KEY (scientific_name, continent_name), FOREIGN KEY (scientific_name) REFERENCES Endangered_Animal (scientific_name), FOREIGN KEY (continent_name) REFERENCES Continent (continent_name) );