



use Endangered; select scientific_name from Animal_Range group by Animal_Range.scientific_name having scientific_name like ['a%'];



use Endangered; select count(*) NumBirds from Bird group by migratory_status having migratory_status = ['Y'];



use Endangered; SELECT Endangered_Animal.common_name, Animal_Range.continent_name FROM Endangered_Animal INNER JOIN Animal_Range ON Endangered_Animal.scientific_name = Animal_Range.scientific_name ORDER BY Endangered_Animal.common_name;



use Endangered; SELECT Endangered_Animal.common_name, Bird.migratory_status FROM Endangered_Animal INNER JOIN Bird ON Endangered_Animal.scientific_name = Bird.scientific_name WHERE Bird.migratory_status = ["Y"] ORDER BY Endangered_Animal.common_name;


use Endangered; SELECT Endangered_Animal.common_name, Animal_Range.continent_name FROM Endangered_Animal INNER JOIN Animal_Range ON Endangered_Animal.scientific_name = Animal_Range.scientific_name WHERE Endangered_Animal.animal_type = ["M"] ORDER BY Animal_Range.continent_name;




use Endangered; SELECT Endangered_Animal.common_name, Bird.migratory_status FROM Endangered_Animal LEFT JOIN Bird ON Endangered_Animal.scientific_name = Bird.scientific_name ORDER BY Endangered_Animal.animal_type;




use Endangered; SELECT Endangered_Animal.endangered_status, Animal_Range.continent_name FROM Endangered_Animal LEFT JOIN Animal_Range ON Endangered_Animal.scientific_name = Animal_Range.scientific_name ORDER BY Animal_Range.continent_name;



use Endangered; SELECT COUNT(*) NumEnd FROM Endangered_Animal WHERE endangered_status = "E";



use Endangered; SELECT DISTINCT continent_name FROM Continent WHERE continent_name like "a%";



use Endangered; SELECT common_name FROM Endangered_Animal WHERE common_name like ["%bear%"];



USE Endangered; CREATE VIEW AnimalNames AS SELECT scientific_name FROM Animal_Range;



use Endangered; SELECT * FROM AnimalNames WHERE scientific_name like "%myotis%";



use Endangered; SELECT * FROM AnimalNames WHERE scientific_name like "%Equus%";




use Endangered; SELECT * FROM AnimalNames WHERE scientific_name like "%Prionailurus%";



USE Endangered; CREATE VIEW BirdNames AS SELECT scientific_name FROM Bird;



use Endangered; SELECT * FROM BirdNames WHERE scientific_name like "%re%";



use Endangered; SELECT * FROM BirdNames WHERE scientific_name like "%ea%";


