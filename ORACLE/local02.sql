select count(*) as REGISTROS, max(salario) as MAXIMO from emp;
select count(*) as PERSONAS, oficio, dept_no from emp group by oficio, dept_no;
select count(*) as PERSONAS, oficio from emp where oficio in ('DIRECTOR', 'ANALISTA') group by oficio; -- muestran los mismo where y
select count(*) as PERSONAS, oficio from emp group by oficio having oficio in ('DIRECTOR', 'ANALISTA'); -- having
-- si está en el select lo que queremos mostrar usar having sino usar where por velocidad.
select count(*) as PERSONAS, oficio from emp group by oficio having count(*) > 1;

-------------------------------------- 04 - CONSULTAS DE AGRUPACION_SOLUCIONES ------------------------------------------
--Encontrar el salario medio de los analistas, mostrando el número de los empleados con oficio analista.
select avg(salario) as MEDIO, count(*) as PERSONAS, oficio from emp where oficio='ANALISTA' group by oficio;
--Encontrar el salario más alto, mas bajo y la diferencia entre ambos de todos los empleados con oficio EMPLEADO.
select  oficio, max(salario) as SALARIOMAXIMO, min(salario) as SALARIOMINIMO
, max(salario) - min(salario) as DIFERENCIA 
from emp group by oficio having oficio = 'EMPLEADO';
--Visualizar los salarios mayores para cada oficio.
select oficio, max(salario) as SALARIOMAXIMO from emp group by oficio;
--Visualizar el número de personas que realizan cada oficio en cada departamento.
select dept_no, 
count(*) as PERSONAS, oficio
from emp group by dept_no, oficio
order by 1;
--Buscar aquellos departamentos con cuatro o más personas trabajando.
select dept_no
, count(*) as PERSONAS from emp 
group by dept_no having count(*) > 3;
--Mostrar el número de directores que existen por departamento.
select count(*) as NUMEROEMPLEADOS, dept_no 
from emp
where oficio = 'DIRECTOR'
group by dept_no;
--Visualizar el número de enfermeros, enfermeras e interinos que hay en la plantilla, ordenados por la función.
select funcion, count(*) as PERSONAS from plantilla group by funcion order by funcion;
--Visualizar departamentos, oficios y número de personas, para aquellos departamentos que tengan dos o más personas trabajando en el mismo oficio.
select dept_no
,count(*) as PERSONAS, 
oficio from emp group by dept_no,oficio  
having count(*) > 1;
--Calcular el salario medio, Diferencia, Máximo y Mínimo de cada oficio. Indicando el oficio y el número de empleados de cada oficio.
select oficio, count(*) as EMPLEADOS
, min(salario) as SALARIOMAXIMO
, max(salario) as SALARIOMINIMO
, max(salario) - min(salario) as DIFERENCIA
, avg(salario) as MEDIA
 from emp group by  oficio;
--Calcular el valor medio de las camas que existen para cada nombre de sala. Indicar el nombre de cada sala y el número de cada una de ellas.
select nombre,avg(num_cama) as MEDIA from sala group by nombre;
--Calcular el salario medio de la plantilla de la sala 6, según la función que realizan. Indicar la función y el número de empleados.
select count(*) as PERSONAS, funcion, avg(salario) as SALARIOMEDIO from plantilla where sala_cod=6 group by funcion;
--Averiguar los últimos empleados que se dieron de alta en la empresa en cada uno de los oficios, ordenados por la fecha.
select max(fecha_alt) AS FECHAMAXIMA, 
Oficio from emp
group by oficio
order by 1;
--Mostrar el número de hombres y el número de mujeres que hay entre los enfermos.
select count(*), sexo from enfermo group by sexo;
--Mostrar la suma total del salario que cobran los empleados de la plantilla para cada función y turno.
select sum(salario) as TOTAL, funcion, turno from plantilla group by funcion, turno;
--Calcular el número de salas que existen en cada hospital.
select count(*) as NUMEROSALAS
, hospital_cod from sala
group by hospital_cod;
--Mostrar el número de enfermeras que existan por cada sala.
select count(*) as PERSONAS
, sala_cod, funcion from plantilla
where funcion='ENFERMERA'
group by sala_cod, Funcion
order by 1;

------------------------------- CONSULTAS DE COMBINACIONES -------------------------------
select emp.apellido, emp.oficio, dept.dnombre, dept.loc
from emp inner join dept on emp.dept_no=dept.dept_no
where loc='SEVILLA';
--
select dept.dnombre, count(*) as PERSONAS 
from emp inner join dept on emp.dept_no=dept.dept_no
group by dept.dnombre;
--              
select plantilla.apellido, plantilla.funcion, hospital.nombre
from plantilla inner join hospital on plantilla.hospital_cod=hospital.hospital_cod;
--
select * from dept;
select distinct dept_no from emp;
select distinct dept_no from dept;
-- INSERT INTO "SYSTEM"."EMP" (EMP_NO, APELLIDO, OFICIO, DIR, FECHA_ALT, SALARIO, COMISION, DEPT_NO) 
-- VALUES ('1111', 'getafe', 'ESTUDIANTE', '1', TO_DATE('2025-02-18 00:00:00', 'YYYY-MM-DD HH24:MI:SS'), '123000', '0', '50')
select emp.apellido, emp.oficio, dept.dnombre, dept.loc
from emp inner join dept on emp.dept_no=dept.dept_no;
--left join: muestra datos de la tabla izquierda
select emp.apellido, emp.oficio, dept.dnombre, dept.loc
from emp left join dept on emp.dept_no=dept.dept_no;
--left right: muestra datos de la tabla derecha
select emp.apellido, emp.oficio, dept.dnombre, dept.loc
from emp right join dept on emp.dept_no=dept.dept_no;
--full join: muestra todo
select emp.apellido, emp.oficio, dept.dnombre, dept.loc
from emp full join dept on emp.dept_no=dept.dept_no;
--cross join: muestra el producto cartesiano = mezcla todo
select emp.apellido, emp.oficio, dept.dnombre, dept.loc
from emp cross join dept;
-- apellido, salario, especiadlidad, direccion hospi y doctores de la paz
select doctor.apellido, doctor.salario, doctor.especialidad, hospital.direccion
from doctor inner join hospital on doctor.hospital_cod=hospital.hospital_cod
where hospital.nombre='la paz';
-- visualizar cuantos empleados trabajan en cada dpt mostrando el nombre del dpt
select count(emp.dept_no) as EMPLEADOS, dept.dnombre
from emp right join dept on emp.dept_no=dept.dept_no
group by dept.dnombre;
-- AGRUPACIÓN 3 TABLAS
select plantilla.apellido, plantilla.funcion,
hospital.nombre,
sala.nombre
from plantilla inner join hospital on plantilla.hospital_cod=hospital.hospital_cod
inner join sala on hospital.hospital_cod=sala.hospital_cod and sala.sala_cod=plantilla.sala_cod;