drop database if exists lol;
create database lol;
use lol;

create table ankiety
(
	nr_ankiety varchar(100),
	pyt1 int,
	pyt2 int,
	pyt3 int,
	pyt4 int,
	pyt5 int,
	pyt6 int,
	id_szkoly varchar(100),
	plec char
);


create table szkoly
(
	id_szkoly varchar(100),
	rodzaj_szkoly varchar(100),
	kod_gminy varchar(100)
);

create table gminy
(
	kod_gminy varchar(100),
	nazwa_gminy varchar(100)
);

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\ankiety.txt' into table ankiety lines terminated by '\r\n' ignore 1 lines;
load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\szkoly.txt' into table szkoly lines terminated by '\r\n' ignore 1 lines;
load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\gminy.txt' into table gminy lines terminated by '\r\n' ignore 1 lines;


select count(*) as chlopcy from ankiety where plec = 'm';
select count(*) as dziewczeta from ankiety where plec = 'k';

select rodzaj_szkoly, round(avg(pyt1), 2) as 'pyt1', round(avg(pyt2), 2) as 'pyt2', round(avg(pyt3), 2) as 'pyt3', round(avg(pyt4), 2) as 'pyt4', round(avg(pyt5), 2) as 'pyt5', round(avg(pyt6), 2) as 'pyt6' from szkoly, ankiety where szkoly.id_szkoly = ankiety.id_szkoly group by rodzaj_szkoly;

select kod_gminy, round(avg(pyt6), 2) as 'pyt6' from szkoly, ankiety where ankiety.id_szkoly = szkoly.id_szkoly group by kod_gminy order by avg(pyt6) desc;

select rodzaj_szkoly, count(*) from szkoly, ankiety where ankiety.id_szkoly = szkoly.id_szkoly and pyt3 = 5 group by rodzaj_szkoly order by rodzaj_szkoly;

select max(nazwa_gminy) from gminy, szkoly, ankiety where ankiety.id_szkoly = szkoly.id_szkoly and szkoly.kod_gminy = gminy.kod_gminy group by gminy.kod_gminy order by count(*) desc limit 1;

select rodzaj_szkoly, count(*) as 'pyt1 na 5: chlopcy' from szkoly, ankiety where ankiety.id_szkoly = szkoly.id_szkoly and pyt1 = 5 and plec = 'm' group by rodzaj_szkoly;
select rodzaj_szkoly, count(*) as 'pyt1 na 5: dziewczeta' from szkoly, ankiety where ankiety.id_szkoly = szkoly.id_szkoly and pyt1 = 5 and plec = 'k' group by rodzaj_szkoly;
