-- create an database
create database django2;

drop database sjdjango2;

use django2;

create table students_info(id int primary key auto_increment, f_name varchar(100) not null,
l_name varchar(100) not null, email varchar(50), address1 text not null, 
address2 varchar(100));

insert into students_info(id, f_name, l_name, email, address1, address2)
values(0, 'sadman', 'sakib', 'sakib@gmail.com', 'Uttara', 'Dhaka');

insert into students_info(id, f_name, l_name, email, address1, address2)
values(0, 'Ahmed', 'Rakib', 'rakib@gmail.com', 'Badda', 'Dhaka');

select * from students_info;

select * from students_info limit 1;

select * from students_info where f_name='Ahmed';

select * from students_info where f_name='Ahmed' or id = 1;

select * from students_info where f_name='Ahmed' and id = 2;

select * from students_info where f_name!='Ahmed';

update students_info set f_name='Rakib', l_name='Ahmed' where id=2;

insert into students_info(id, f_name, l_name, email, address1, address2)
values(0, 'Nahid', 'Mosharof', 'nahid@gmail.com', 'Dhanmondi', 'Dhaka');

delete from students_info where id = 2;

create table dept(id int primary key auto_increment, dept_name varchar(50) not null, details text);

insert into dept(id, dept_name, details)
values(0, 'Accounts', '');

select * from dept;

create table emp(id int primary key auto_increment, f_name varchar(100) not null,
l_name varchar(100) not null, email varchar(50), address1 text not null, 
address2 varchar(100));

alter table emp add dept_id int after l_name;

insert into emp(id, f_name, l_name, dept_id, email, address1, address2)
values(0, 'Shakil', 'Ahmed', 4, 'shail@gmail.com', 'Sobhanbag', 'Dhaka');

select * from emp;

-- inner join
select emp.f_name, emp.l_name, emp.email, dept.dept_name from emp
inner join dept on emp.dept_id = dept.id;

-- making alias like -> emp as e
select e.f_name, e.l_name, e.email, d.dept_name from emp as e
inner join dept as d on e.dept_id = d.id;

-- left join
select e.f_name, e.l_name, e.email, d.dept_name from emp as e
left join dept as d on e.dept_id = d.id;

-- right join
select e.f_name, e.l_name, e.email, d.dept_name from emp as e
right join dept as d on e.dept_id = d.id;

select e.f_name, e.l_name, e.email, d.dept_name from emp as e
full outer join dept as d on e.dept_id = d.id;

-- group by

select count(l_name), f_name from emp group by f_name;
select count(id), dept_name from dept group by dept_name;