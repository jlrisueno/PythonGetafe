------------------------------------------ SUBCONSULTAS ------------------------------------------
-- mostrar los datos del empleado que más cobra de la empresa
select * from emp where salario=
(select max(salario) from emp);
-- mostrar todos los empleados que tengan el mismo oficio que  'sala' (apellido)
-- y que tengan más salario que el empleado 'ford'
select * from emp where oficio=
(select oficio from emp where apellido='sala')
and salario>(select salario from emp where apellido='ford');
-- mostrar todos los empleados que tengan el mismo oficio que  'sala' (apellido)
-- o que tengan el mismo oficio que 'jimenez'
-- cuando la subconsulta devulve más de un resultado se utiliza IN
select * from emp where oficio IN
(select oficio from emp where apellido='sala' or apellido='jimenez');

------------------------------------------ CONSULTAS UNION ------------------------------------------
---- Estas consultas sirven para mostrar datos de varias tablas que NO tienen relación dentro de un mismo cursor
---- Reglas:
---- 1º La consulta que manda es la primera (jefa)
---- 2º Todas las columnas de cada consulta deben ser del mismo tipo de datos
---- 3º Todas las consultas deben tener el mismo número de columnas
---- Es como unir varias consultas en una sola. Quita repetidos
select apellido, oficio, salario from emp
where salario>250000
union
select apellido, especialidad, salario from doctor
where salario>250000
union
select apellido, funcion, salario from plantilla
where salario>250000
order by 2;
-- NO quita repetidos
select apellido, oficio, salario from emp
union all
select apellido, oficio, salario from emp;
------------------------------------------ SELECT TO SELECT ------------------------------------------
--- consultas sobre consulta
select * from
(select apellido, oficio, salario from emp
union
select apellido, especialidad, salario from doctor
union
select apellido, funcion, salario from plantilla) CONSULTA
where salario>250000
order by oficio;
------------------------------------------ CONSULTA A NIVEL DE FILA ------------------------------------------
select apellido,case turno
when 'T' then 'Tarde'
when 'M' then 'Mañana'
else 'Noche'
end as TURNO
from plantilla;
------------------------------------------ 05 - CONSULTAS DE COMBINACION_JOIN ------------------------------------------
--Seleccionar el apellido, oficio, salario, numero de departamento y su nombre de todos los empleados cuyo salario sea mayor de 300000
select emp.apellido, emp.oficio, emp.salario, emp.dept_no, dept.dnombre as DEPARTAMENTO
from emp inner join dept on emp.dept_no=dept.dept_no
where emp.salario>300000;
--Mostrar todos los nombres de Hospital con sus nombres de salas correspondientes.
select sala.nombre as NOMBRESALA, hospital.nombre as NOMBREHOSPITAL
from sala inner join hospital on sala.hospital_cod=hospital.hospital_cod;
--Calcular cuántos trabajadores de la empresa hay en cada ciudad.
select count(emp.dept_no) as TRABAJADORES, dept.loc as CIUDAD
from emp right join dept on emp.dept_no=dept.dept_no
group by dept.loc;
--Visualizar cuantas personas realizan cada oficio en cada departamento mostrando el nombre del departamento.
select dept.dnombre as DEPARTAMENTO, count(emp.dept_no) as PERSONAS, emp.oficio
from emp inner join dept on emp.dept_no=dept.dept_no
group by dept.dnombre, emp.oficio;
--Contar cuantas salas hay en cada hospital, mostrando el nombre de las salas y el nombre del hospital.
select count(*), sala.nombre as NOMBRESALA, hospital.nombre as NOMBREHOSPITAL
from sala inner join hospital on sala.hospital_cod=hospital.hospital_cod
group by sala.nombre, hospital.nombre;
--Queremos saber cuántos trabajadores se dieron de alta entre el año 1997 y 1998 y en qué departamento.
select count(emp.dept_no) as ALTAS, dept.dnombre as DEPARTAMENTO
from emp inner join dept on emp.dept_no=dept.dept_no
where emp.fecha_alt>'01/01/1997' and emp.fecha_alt<'01/01/1998'
group by dept.dnombre;
--Buscar aquellas ciudades con cuatro o más personas trabajando.
select count(emp.dept_no) as TRABAJADORES, dept.loc as CIUDAD
from emp inner join dept on emp.dept_no=dept.dept_no
group by dept.loc
having count(*) > 3;
--Calcular la media salarial por ciudad.  Mostrar solamente la media para Madrid y Elche.
select avg(emp.salario) as MEDIASALARIO, dept.loc as CIUDAD
from emp inner join dept on emp.dept_no=dept.dept_no
where dept.loc='MADRID' or dept.loc='ELCHE'
group by dept.loc;
--Mostrar los doctores junto con el nombre de hospital en el que ejercen, la dirección y el teléfono del mismo.
select doctor.apellido as DOCTOR, hospital.nombre as NOMBREHOSPITAL, hospital.direccion, hospital.telefono
from doctor inner join hospital on doctor.hospital_cod=hospital.hospital_cod;
--Mostrar los nombres de los hospitales junto con el mejor salario de los empleados de la plantilla de cada hospital.
select hospital.nombre as NOMBREHOSPITAL, max(doctor.salario) as SALARIOMAXIMO
from doctor inner join hospital on doctor.hospital_cod=hospital.hospital_cod
group by hospital.nombre;
--Visualizar el Apellido, función y turno de los empleados de la plantilla junto con el nombre de la sala y el nombre del hospital con el teléfono.
select plantilla.apellido, plantilla.funcion, plantilla.turno, sala.nombre as NOMBRESALA, hospital.nombre as NOMBREHOSPITAL, hospital.telefono
from plantilla inner join hospital on plantilla.hospital_cod=hospital.hospital_cod
inner join sala on hospital.hospital_cod=sala.hospital_cod and sala.sala_cod=plantilla.sala_cod;
--Visualizar el máximo salario, mínimo salario de los Directores dependiendo de la ciudad en la que trabajen. Indicar el número total de directores por ciudad.
select count(emp.dept_no) as DIRECTORES, dept.loc as CIUDAD, max(emp.salario) as SALARIOMAX, min(emp.salario) as SALARIOMIN
from emp inner join dept on emp.dept_no=dept.dept_no
where emp.oficio='DIRECTOR'
group by dept.loc;
--Averiguar la combinación de que salas podría haber por cada uno de los hospitales.
select sala.nombre as NOMBRESALA, hospital.nombre as NOMBREHOSPITAL
from sala cross join hospital;