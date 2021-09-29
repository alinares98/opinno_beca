create table Candidatos(id integer, nombre varchar(100), email varchar(100));
insert into Candidatos(id, nombre, email) values(1, "Pepe", "pepe@email.com");
insert into Candidatos(id, nombre, email) values(2, "Javier", "javier@email.com");
insert into Candidatos(id, nombre, email) values(3, "Maria", "maria@email.com");

create table Jueces(id integer, nombre varchar(100), email varchar(100));
insert into Jueces(id, nombre, email) values(1, "Christian", "christian@email.com");
insert into Jueces(id, nombre, email) values(2, "Ramon", "ramon@email.com");

create table Evaluacion(id integer, candidato_id integer, juez_id integer, fase integer);
insert into Evaluacion (id, candidato_id, juez_id, fase) values (1, 1, 1, 1);
insert into Evaluacion (id, candidato_id, juez_id, fase) values (2, 3, 1, 2);
insert into Evaluacion (id, candidato_id, juez_id, fase) values (3, 1, 2, 2);
insert into Evaluacion (id, candidato_id, juez_id, fase) values (4, 3, 2, 1);
insert into Evaluacion (id, candidato_id, juez_id, fase) values (5, 2, 2, 1);

select * from Candidatos;
select * from Jueces;
select * from Evaluacion;
