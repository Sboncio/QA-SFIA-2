create database sfia2;
USE sfia2;
create table weather ( id int AUTO_INCREMENT, weathers varchar(5), PRIMARY KEY(id));
create table speed ( id int AUTO_INCREMENT, speeds varchar(7), PRIMARY KEY(id));
create table results( id int AUTO_INCREMENT, weather varchar(5), speed varchar(7), result varchar(50), PRIMARY KEY(id));

INSERT INTO weather (weathers) VALUES ('Rain');
INSERT INTO weather (weathers) VALUES ('Sun');
INSERT INTO weather (weathers) VALUES ('Snow');
INSERT INTO weather (weathers) VALUES ('Ice');

INSERT INTO speed (speeds) VALUES ('Slow');
INSERT INTO speed (speeds) VALUES ('Average');
INSERT INTO speed (speeds) VALUES ('Fast');