select * from EMP;
select loc, dnombre from DEPT;
select * from emp order by apellido desc;
select * from emp where dept_no=10;
select * from emp where oficio='DIRECTOR';
select * from emp where dept_no=10 or dept_no=20;
select * from emp where emp_no >= 7800 and emp_no <=7900;
select * from emp where emp_no BETWEEN 7800 and 7900;
select * from emp where not oficio='VENDEDOR'; -- no usar, no es eficiente usa <>
select * from emp where oficio<>'VENDEDOR';
select * from emp where dept_no=10 or dept_no=20;
select * from emp where dept_no in (10, 20);
select * from emp where dept_no not in (10, 20);
select * from emp where apellido like 's%a';
select * from emp where apellido like '____';
select distinct oficio from emp;
select apellido, (salario+comision) as TOTAL from emp; -- no se puede usar WHERE en un "campo calculado=TOTAL"
select apellido, (salario+comision) as TOTAL from emp where TOTAL >=210000; -- falla, pero se puede hacer con el cálculo
select apellido, (salario+comision) as TOTAL from emp where (salario+comision) >= 210000; -- <--------------------------
select apellido, (salario+comision) as TOTAL from emp order by TOTAL;

-- PRACTICAS
--Mostrar todos los datos de los empleados de nuestra tabla emp.
select * from emp;
--Mostrar el apellido, oficio, salario anual, con las dos extras para aquellos empleados con comisión mayor de 100000.
select apellido, oficio, (salario*14) as SANUAL from emp where comision>100000;
--Idem del anterior, pero para aquellos empleados que su salario anual con extras supere las 750.000 ptas.
select apellido, oficio, (salario*14) as SANUAL from emp where (14*salario)>750000;
--Idem del anterior, pero para aquellos empleados que sumen entre salario anual con extras y comisión el 1.000.000. 
select apellido, oficio, (salario*14) as SANUAL from emp where (14*salario+comision)>1000000;
--Mostrar todos los datos de empleados ordenados por departamento y dentro de este por oficio para tener una visión jerárquica.(order by)
select * from emp order by dept_no, oficio;
--Mostrar todos los enfermos nacidos antes del 1/1/70.
select * from enfermo where fecha_nac<'1/1/70';
--Igual que el anterior, para los nacidos antes del 1/1/1970 ordenados por número de inscripción.
select * from enfermo where fecha_nac<'1/1/1970' order by inscripcion;
--Listar todos los datos de la plantilla del hospital del turno de mañana
select * from plantilla where turno='M';
--Idem del turno de noche.
select * from plantilla where turno='N';
--Listar los doctores que su salario anual supere 3.000.000 ptas.
select * from doctor where (salario*12)>3000000;
--Visualizar los empleados de la plantilla del turno de mañana que tengan un salario entre 2.000.000 y 2.250.000.
select * from plantilla where (salario*12) >= 2000000 and (salario*12) <= 2250000 and turno='M';
--Visualizar los empleados de la tabla emp que no se dieron de alta entre el 01/01/80 y el 12/12/82.
select * from emp where fecha_alt not BETWEEN '01/01/80' and '12/12/82';
--Mostrar los nombres de los departamentos situados en Madrid o en Barcelona.
select dnombre from dept where loc='MADRID' or loc='BARCELONA';