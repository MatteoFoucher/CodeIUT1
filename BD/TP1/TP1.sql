--sqlplus foucher@ora12
--select * from tab;
--drop table BIN$IW6GqmstT2fgY/YNqMD/NQ==$0;
--purge recyclebin;
--rlwrap sqlplus foucher@ora12
create table CLIENT(
    codeCl number(10),
    nomCl varchar2(40),
    prenom varchar2(30),
    adresse varchar(50),
    email varchar(50)
)

insert into CLIENT values(12, 'Foucher', 'Matteo', '194 Avenue de lArgonne', 'matteofoucher@gmail.com');

create table ARTICLE(
    RefArt number(5).
    designation 
)