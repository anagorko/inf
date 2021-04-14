drop database if exists lol;
create database lol;
use lol;

create table osoby
(
	id_uzytkownika int,
	nazwisko varchar(100),
	imie varchar(100),
	plec char
);

create table zajecia
(
	id_zajec int,
	obiekt varchar(100),
	zajecia varchar(100),
	koszt float
);

create table wejscia
(
	lp int,
	id_uzytkownika int,
	data_wejscia date,
	id_zajec int
);


load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\osoby.txt' into table osoby fields terminated by ';' lines terminated by '\r\n' ignore 1 lines;
load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\zajecia.txt' into table zajecia fields terminated by ';' lines terminated by '\r\n' ignore 1 lines;
load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\wejscia.txt' into table wejscia fields terminated by ';' lines terminated by '\r\n' ignore 1 lines;

select count(*) as 'kobiety' from (select osoby.id_uzytkownika as id from zajecia, wejscia, osoby where osoby.id_uzytkownika = wejscia.id_uzytkownika and zajecia.id_zajec = wejscia.id_zajec and zajecia.zajecia = 'Fitness TBC' and plec = 'K' group by osoby.id_uzytkownika) as t;
select count(*) as 'mezczyzni' from (select osoby.id_uzytkownika as id from zajecia, wejscia, osoby where osoby.id_uzytkownika = wejscia.id_uzytkownika and zajecia.id_zajec = wejscia.id_zajec and zajecia.zajecia = 'Fitness TBC' and plec = 'M' group by osoby.id_uzytkownika) as t;

select obiekt, sum(koszt) from zajecia, wejscia, osoby where osoby.id_uzytkownika = wejscia.id_uzytkownika and zajecia.id_zajec = wejscia.id_zajec group by obiekt;

select max(imie), max(nazwisko) from zajecia, wejscia, osoby where osoby.id_uzytkownika = wejscia.id_uzytkownika and zajecia.id_zajec = wejscia.id_zajec and data_wejscia = '2014-04-16' group by osoby.id_uzytkownika having count(*) > 1;

select zajecia, count(distinct(id_uzytkownika)) as 'liczba osob', obiekt from zajecia, wejscia where zajecia.id_zajec = wejscia.id_zajec group by zajecia, obiekt order by count(distinct(id_uzytkownika)) desc;

select obiekt, count(*) from zajecia, wejscia where zajecia.id_zajec = wejscia.id_zajec group by obiekt order by obiekt;
