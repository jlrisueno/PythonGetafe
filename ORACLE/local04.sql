------------------------------------------ CONSULTAS DE ACCION ------------------------------------------
--commit: subir cambios, solo de Oracle
commit;
--rollback: retroceder cambios, solo de Oracle
rollback;
--- INSERT ---
select * from dept;
insert into dept values (50, 'PYTHON', 'GETAFE');
insert into dept (dept_no, dnombre) values (60, 'I+D');
-- insert con subconsulta
select * from plantilla;
insert into plantilla
(apellido, funcion, turno, empleado_no, hospital_cod)
values ('López', 'ENFERMERA', 'T', (select max(empleado_no)+1 from plantilla), 22);
--- DELETE ---
-- elimina toda la tabla: delete form tabla;
delete from plantilla where empleado_no=9902;
--
delete from plantilla where hospital_cod=
(select hospital_cod from hospital where nombre='El Carmen');
--- UPDATE ---
--incrementar el salario de todos en +1
update plantilla set salario=salario+1;
--modificar la funcion de los interino a interina y subir salario +1
update plantilla set funcion='INTERINA',salario=salario+1
where funcion='INTERINO';
--subconsulta: modificar salario de la sala 4 igual al de karplus w.
update plantilla set salario=
(select salario from plantilla where apellido='karplus w.')
where sala_cod=4;
--distinct!!
update plantilla set turno='M' where sala_cod=
(select distinct sala_cod from sala where nombre='psiquiatria');
-- insertar nuevo registro datos X en el hospital El Carmen y cod MAX+1
select * from hospital;
select * from plantilla;
insert into plantilla (apellido, sala_cod, funcion, turno, hospital_cod, empleado_no)
values ('Cabrales', 4, 'ENFERMERA', 'M',
(select hospital_cod from hospital where nombre='El Carmen'),
(select max(empleado_no)+1 from plantilla));
--eliminar las personas que no tengan hospital o null
delete from plantilla where 
hospital_cod not in (select hospital_cod from hospital) or hospital_cod is null;
--- TRUNCATE ---
--NO USAR
--elimina todos los registros de una tabla, NO TIENE ROLLBACK
--Sintaxis: truncate table nombretabla;

------------------------------------------ 07 - CONSULTAS DE ACCION ------------------------------------------
--Dar de alta con fecha actual al empleado José Escriche Barrera como programador perteneciente al departamento de producción.
--Tendrá un salario base de 70000 pts/mes y no cobrará comisión. 
select * from dept;
select * from emp;
insert into emp (emp_no, fecha_alt, apellido, oficio, dept_no, salario, comision) values
((select max(emp_no)+1 from emp), '20/02/2025', 'José Escriche Barrera', 'PROGRAMADOR', (select dept_no from dept where dnombre='PRODUCCIÓN'), 70000*12, 0);
--Se quiere dar de alta un departamento de informática situado en Fuenlabrada (Madrid).
insert into dept values ((select max(dept_no)+10 from dept), 'INFORMATICA', 'Fuenlabrada (Madrid)');
--El departamento de ventas, por motivos peseteros, se traslada a Teruel, realizar dicha modificación.
update dept set loc='TERUEL' where dnombre='VENTAS';
--En el departamento anterior (ventas), se dan de alta dos empleados: Julián Romeral y Luis Alonso.
--Su salario base es el menor que cobre un empleado, y cobrarán una comisión del 15% de dicho salario.
insert into emp values
((select max(emp_no)+1 from emp), 'Julián Romeral', 'EMPLEADO', (select max(dir)+1 from emp), '20/02/2025',
(select min(salario) from emp where oficio='EMPLEADO'), 15, (select dept_no from dept where dnombre='VENTAS'));
insert into emp values
((select max(emp_no)+1 from emp), 'Luis Alonso', 'EMPLEADO', (select max(dir)+1 from emp), '20/02/2025',
(select min(salario) from emp where oficio='EMPLEADO'), 15, (select dept_no from dept where dnombre='VENTAS'));
--Modificar la comisión de los empleados de la empresa, de forma que todos tengan un incremento del 10% del salario.
update emp set comision=comision+((comision*10)/100);
--Incrementar un 5% el salario de los interinos de la plantilla que trabajen en el turno de noche.
select * from plantilla;
update plantilla set salario=salario+((salario*5)/100) where turno='N';
--Incrementar en 5000 Pts. el salario de los empleados del departamento de ventas y del presidente,
--tomando en cuenta los que se dieron de alta antes que el presidente de la empresa.
select * from emp;
update emp set salario=salario+5000 where dept_no=(select dept_no from dept where dnombre='VENTAS') or
dept_no=(select dept_no from emp where oficio='PRESIDENTE') and
fecha_alt<(select fecha_alt from emp where oficio='PRESIDENTE');
--El empleado Sanchez ha pasado por la derecha a un compañero.  Debe cobrar de comisión 12.000 ptas más que
--el empleado Arroyo y su sueldo se ha incrementado un 10% respecto a su compañero.

--Se tienen que desplazar cien camas del Hospital SAN CARLOS para un Hospital de Venezuela.  Actualizar el número de camas del Hospital SAN CARLOS.

--Subir el salario y la comisión en 100000 pesetas y veinticinco mil pesetas respectivamente a los empleados que se dieron de alta en este año.

--Ha llegado un nuevo doctor a la Paz.  Su apellido es House y su especialidad es Diagnostico.   Introducir el siguiente número de doctor disponible.

--Borrar todos los empleados dados de alta entre las fechas 01/01/80 y 31/12/82.

--Modificar el salario de los empleados trabajen en la paz y estén destinados a Psiquiatría.  Subirles el sueldo 20000 Ptas. más que al señor Amigo R.

--Insertar un empleado con valores null (por ejemplo la comisión o el oficio), y después borrarlo buscando como valor dicho valor null creado.

--Borrar los empleados cuyo nombre de departamento sea producción.

--Borrar todos los registros de la tabla Emp sin delete.

--Volver a ejecutar los SCRIPTS de BBDD para dejar la base de datos intacta para el siguiente módulo.
