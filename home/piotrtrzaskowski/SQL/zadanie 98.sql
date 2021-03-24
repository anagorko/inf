drop database if exists matura;
create database matura;
use matura;
CREATE Table uczniowie(
	id VARCHAR(30),
	imie VARCHAR(60),
	nazwisko VARCHAR(120),
	klasa VARCHAR(120)
);

LOAD DATA infile "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\uczniowie.txt" 
into table uczniowie 
lines terminated by "\r\n" 
ignore 1 lines;

CREATE table przedmioty(
	id_przedmiotu INTEGER,
	nazwa_przedmiotu VARCHAR(300)
);

LOAD DATA infile "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\przedmioty.txt" 
into table przedmioty
lines terminated by "\r\n" 
ignore 1 lines;

CREATE table oceny(
	id_oceny INTEGER,
	data DATE,
	id VARCHAR(30),
	id_przedmiotu INTEGER,
	ocena INTEGER
);

LOAD DATA infile "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\oceny.txt" 
into table oceny
lines terminated by "\r\n" 
ignore 1 lines;

show tables;

-- Zadanie 1
select klasa from uczniowie group by klasa having sum(case when imie like '%a' then 1 else 0 end)>COUNT(*)/2;

-- Zadanie 2
select data from oceny group by data having sum(case when ocena = 1 then 1 else 0 end)>10;

-- Zadanie 3
select klasa, AVG(ocena) from uczniowie, oceny, przedmioty where uczniowie.id = oceny.id 
and klasa like 'IV%' and oceny.id_przedmiotu = przedmioty.id_przedmiotu 
and nazwa_przedmiotu = 'j.polski' group by klasa order by klasa;

-- Zadanie 4
select nazwa_przedmiotu,MONTH(data), count(*) 
from przedmioty, oceny 
where przedmioty.id_przedmiotu = oceny.id_przedmiotu and ocena = 5 
group by nazwa_przedmiotu, MONTH(data) order by nazwa_przedmiotu;

-- Zadanie 5
-- id 21
select imie, nazwisko
from uczniowie
left join oceny on oceny.id = uczniowie.id and oceny.id_przedmiotu = 21
where klasa = 'II A' and ocena is NULL;