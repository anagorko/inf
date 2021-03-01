drop database if exists lol;
create database lol;
use lol;

create table uczniowie
(
	id_ucznia varchar(100),
	imie varchar(100),
	nazwisko varchar(100),
	klasa varchar(20)
);

create table przedmioty
(
	id_przedmiotu int,
	nazwa_przedmiotu varchar(100)
);

create table oceny
(
	id_oceny int,
	czas date,
	id_ucznia varchar(100),
	id_przedmiotu int,
	ocena int
);

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\uczniowie.txt' into table uczniowie lines terminated by '\r\n' ignore 1 lines;
load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\przedmioty.txt' into table przedmioty lines terminated by '\r\n' ignore 1 lines;
load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\oceny.txt' into table oceny lines terminated by '\r\n' ignore 1 lines;

select k from (select klasa as k, count(*) as c from uczniowie where imie like '%a' group by klasa) as a, (select klasa as k2, count(*) as c2 from uczniowie group by klasa) as b 
where k = k2 and c / c2 > 0.5;

select czas, count(*) from oceny where ocena = 1 group by czas having count(*) > 10;

select klasa, round(avg(ocena), 2) from uczniowie, oceny where uczniowie.id_ucznia = oceny.id_ucznia and id_przedmiotu = 1 and klasa like 'IV%' group by klasa;

select month(czas), max(nazwa_przedmiotu), count(*) from oceny, przedmioty where przedmioty.id_przedmiotu = oceny.id_przedmiotu and ocena = 5 group by month(czas), oceny.id_przedmiotu;

select max(imie), max(nazwisko) from uczniowie left join (select uczniowie.id_ucznia as id from uczniowie, oceny, przedmioty where 
uczniowie.id_ucznia = oceny.id_ucznia and przedmioty.id_przedmiotu = oceny.id_przedmiotu and nazwa_przedmiotu = 'sieci komputerowe' group by uczniowie.id_ucznia) as u2 
on id_ucznia = id where id is null and klasa = 'II a' group by id_ucznia;
