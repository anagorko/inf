drop database if exists lol;
create database lol;
use lol;

create table osoby
(
	id_osoby int,
	imie varchar(100),
	nazwisko varchar(100),
	grupa varchar(100)
);

create table listy
(
	id_listy int,
	nazwa varchar(100),
	termin_oddania date
);

create table punktacja
(
	lp int,
	id_osoby int,
	id_listy int,
	punkty float,
	czas_oddania date
);

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\osoby.txt' into table osoby lines terminated by '\r\n' ignore 1 lines;
load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\listy.txt' into table listy lines terminated by '\r\n' ignore 1 lines;
load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\punktacja.txt' into table punktacja lines terminated by '\r\n' ignore 1 lines;


select max(nazwa), round(avg(punkty), 2) from punktacja, listy where punktacja.id_listy = listy.id_listy group by listy.id_listy;

select imie, nazwisko from listy, osoby, punktacja where punktacja.id_listy = listy.id_listy and osoby.id_osoby = punktacja.id_osoby 
and nazwa like 'P%' and datediff(czas_oddania, termin_oddania) >= 14 group by osoby.id_osoby;

select count(*) as 'ocena 1' from (select count(*) as x from punktacja group by id_osoby having sum(punkty) < 72) as t;
select count(*) as 'ocena 2' from (select count(*) as x from punktacja group by id_osoby having sum(punkty) < 90 and sum(punkty) >= 72) as t;
select count(*) as 'ocena 3' from (select count(*) as x from punktacja group by id_osoby having sum(punkty) < 126 and sum(punkty) >= 90) as t;
select count(*) as 'ocena 4' from (select count(*) as x from punktacja group by id_osoby having sum(punkty) < 153 and sum(punkty) >= 126) as t;
select count(*) as 'ocena 5' from (select count(*) as x from punktacja group by id_osoby having sum(punkty) < 180 and sum(punkty) >= 153) as t;

select grupa, count(*) as '10 pkt' from osoby, (select grupa as g, osoby.id_osoby as i from punktacja, osoby where osoby.id_osoby = punktacja.id_osoby and punkty = 10 group by grupa, osoby.id_osoby order by grupa asc) as o 
where grupa = g and id_osoby = i group by grupa;
select grupa, count(*) as '11 pkt' from osoby, (select grupa as g, osoby.id_osoby as i from punktacja, osoby where osoby.id_osoby = punktacja.id_osoby and punkty = 11 group by grupa, osoby.id_osoby order by grupa asc) as o 
where grupa = g and id_osoby = i group by grupa;
select grupa, count(*) as '12 pkt' from osoby, (select grupa as g, osoby.id_osoby as i from punktacja, osoby where osoby.id_osoby = punktacja.id_osoby and punkty = 12 group by grupa, osoby.id_osoby order by grupa asc) as o 
where grupa = g and id_osoby = i group by grupa;

select imie, nazwisko from osoby left join (select id_osoby as i from punktacja group by id_osoby having count(*) = 11) as t on id_osoby = i where i is null order by nazwisko asc;
