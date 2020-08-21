CREATE DATABASE sfia2;
USE sfia2;
CREATE TABLE weather (weather_id int NOT NULL AUTO_INCREMENT, weather_name varchar(5) NOT NULL, PRIMARY KEY (weather_id));
CREATE TABLE speed (speed_id int NOT NULL AUTO_INCREMENT, speed_name varchar(7) NOT NULL, PRIMARY KEY (speed_id));

/*Populate speeds*/
INSERT INTO speed VALUES(1,'Slow');
INSERT INTO speed VALUES(2,'Average');
INSERT INTO speed VALUES(3,'Fast');

/*Populate weather */
INSERT INTO weather VALUES(1,'Sun');
INSERT INTO weather VALUES(2,'Rain');
INSERT INTO weather VALUES(3,'Frost');
INSERT INTO weather VALUES(4,'Snow');