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
    email varchar(50),
    constraint CleCLIENT PRIMARY KEY (codeCl)
);

insert into CLIENT values(12, 'Foucher', 'Matteo', '194 Avenue de lArgonne', 'matteofoucher@gmail.com');

create table ARTICLE(
    RefArt number(5),
    designation varchar2(20),
    prix number(5.2),
    TVA number(4.2),
    qteStock number(5.2),
    

);

create table COMMANDE(
    NumCom number(5),
    DateCom date,
    codeCl number(5)
);

create table COLIS(
    Numcom number(5),
    NumColis number(5),
    indiceRetrait varchar2(20)
);

create table EXPEDIER(
    NumCom number(5),
    NumColis number(5),
    RefArt number(5),
    qteExp number(5),
    qteAcc number(5)
);

create table CONTENIR(
    numCom number(5),
    RefArt number(5),
    qteCom number(5)
);