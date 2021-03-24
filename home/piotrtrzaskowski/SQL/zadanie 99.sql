drop database if exists matura;
create database matura;
use matura;

CREATE TABLE ankiety(
	nr_ankiety VARCHAR(30),
	pyt1 INTEGER,
	pyt2 INTEGER,
	pyt3 INTEGER,
	pyt4 INTEGER,
	pyt5 INTEGER,
	pyt6 INTEGER,
	id_szkoly VARCHAR(30),
	plec VARCHAR(1)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\ankiety.txt'
into table ankiety 
lines terminated by "\r\n" 
ignore 1 lines;

CREATE TABLE szkoly(
	id_szkoly VARCHAR(30),
	rodzaj_szkoly VARCHAR(30),
	kod_gminy VARCHAR(30)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\szkoly.txt'
into table szkoly
lines terminated by "\r\n" 
ignore 1 lines;


CREATE TABLE gminy(
	kod_gminy VARCHAR(30),
	nazwa_gminy VARCHAR(120)
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\gminy.txt'
into table gminy
lines terminated by "\r\n" 
ignore 1 lines;


-- Zadanie 1

select plec, count(*) from ankiety group by plec;

-- Zadanie 2

select rodzaj_szkoly, ROUND(avg(pyt1),2), ROUND(avg(pyt2),2), ROUND(avg(pyt3),2), ROUND(avg(pyt4),2), ROUND(avg(pyt5),2), ROUND(avg(pyt6),2) 
from ankiety, szkoly 
where szkoly.id_szkoly = ankiety.id_szkoly 
group by rodzaj_szkoly;

-- Zadanie 3

select kod_gminy, ROUND(avg(pyt6),2) as srednia
from ankiety, szkoly 
where szkoly.id_szkoly = ankiety.id_szkoly
group by kod_gminy order by srednia desc;

-- Zadanie 4

select rodzaj_szkoly, count(*) as liczba_uczniow
from ankiety, szkoly 
where szkoly.id_szkoly = ankiety.id_szkoly and pyt3 = 5
group by rodzaj_szkoly order by rodzaj_szkoly;

-- Zadanie 5

select nazwa_gminy, count(*) as liczba_uczniow
from ankiety, szkoly , gminy
where szkoly.id_szkoly = ankiety.id_szkoly and gminy.kod_gminy = szkoly.kod_gminy
group by nazwa_gminy order by liczba_uczniow desc limit 1;

-- Zadanie 6

select rodzaj_szkoly, sum(case when plec = 'k' then 1 else 0 end) as liczba_dziewczat, sum(case when plec = 'm' then 1 else 0 end) as liczba_chlopcow
from ankiety, szkoly 
where szkoly.id_szkoly = ankiety.id_szkoly and pyt1 = 5
group by rodzaj_szkoly order by rodzaj_szkoly;


