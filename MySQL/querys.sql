
/*El nombre y el email de los candidatos que han sido evaluados en la fase 2 por el juez Ramón*/
select c.nombre, c.email
from Candidatos c
INNER JOIN Evaluacion e on c.id=e.candidato_id
INNER JOIN Jueces j on e.juez_id = j.id
where j.nombre="Ramon" AND e.fase=2;

/*El nombre de los jueces que evaluaron a Pepe*/
select j.nombre
from Jueces j
INNER JOIN Evaluacion e on e.juez_id=j.id
INNER JOIN Candidatos c on c.id=e.candidato_id
where c.id=1;

/*Número de evaluaciones realizadas por cada juez*/
select j.nombre, count(*)
from Jueces j
INNER JOIN Evaluacion e on e.juez_id=j.id
group by(j.nombre)