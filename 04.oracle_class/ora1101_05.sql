-- join
-- inner join - equi join / non-equi join, self join, outer join

-- employees 사원번호, 사원명, 부서번호, 부서명 - departments 을 출력하시오.
select employee_id, emp_name, a.department_id, department_name 
from employees a, departments b
where a.department_id = b.department_id;

select * from stu_grade;
select * from students;

-- 두 테이블간 동일한 컬럼없이 데이터를 가져오는 방법: non-equi join
-- avg 값을 가지고 다른 컬럼을 다른 테이블에서 가져와 출력
select name, avg, grade 
from students, stu_grade
where avg between loavg and hiavg;

-- self join 자신의 테이블을 2번 호출
select a.employee_id, a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id = b.employee_id;

select * from stu;
-- 컬럼 삭제
--alter table stu drop column result;
-- 컬럼 추가
alter table stu add result varchar2(10);

-- avg의 컬럼을 가지고, stu_grade 활용해서 이 값을 result컬럼에 모두 입력 하시오.
update stu a set result = (select grade from stu_grade where a.avg between loavg and hiavg);
select name, avg, result from stu order by avg;
-- no, avg, result 출력
select no, avg, result from stu;

select no, avg, result, grade
from stu, stu_grade
where avg between loavg and hiavg;

-- non-equi join update 구문
update stu a set result = (select grades from (select no, grade as grades from stu, stu_grade where avg between loavg and hiavg) b where a.no = b.no);
select name, avg, result from stu order by avg;

-- rank()
select * from stu;
update stu set rank = 0;

select no, name, avg, rank() over(order by avg desc) as ranks from stu;

-- rank()의 결과 값을 rank 컬럼에 모두 입력하시오.
update stu a set rank = (select ranks from (select no, rank() over(order by avg desc) as ranks from stu) b where a.no = b.no);
select no, name, avg, rank from stu order by avg desc;

-- null 값을 포함한 개수: 107개
select employee_id, emp_name, manager_id from employees;
-- null 값을 제외한 개수: 106개
select manager_id from employees where manager_id is not null;
-- null 값일때 ceo 출력하시오
select nvl(manager_id, 0) from employees;
select nvl(to_char(manager_id), 'CEO') as manager_id from employees;

-- self join manager_id, 매니저의 이름을 출력하시오.
-- self join 106개
-- outer join: 해당컬럼에 null 값이 존재할 시 null 값을 포함해서 출력
select a.employee_id, a.emp_name, a.manager_id, b.emp_name, a.salary
from employees a, employees b
where a.manager_id = b.employee_id(+);

select * from employees
where emp_name = 'Martha Sullivan';


-- 사원번호, 사원명, 부서번호, 부서명 출력하시오
-- equi-join, employees에 부서번호 null 값도 출력하시오.
select employee_id, emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id(+) = b.department_id;

-- ansi cross join
select * from employees cross join departments;
-- cross join
select * from employees, departments;

-- equi-join
select a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id;

-- ansi inner join
select a.department_id, department_name
from employees a inner join departments b
on a.department_id = b.department_id;

-- ansi join: using
select department_id, department_name
from employees inner join departments
using (department_id);

-- ansi join: natural join - 두개의 공통부분의 컬럼이 있으면 자동으로 인식해서 검색
select department_id, department_name
from employees natural join departments;

-- outer join (left, right, full)
select employee_id, emp_name, a.department_id, department_name
from employees a full outer join departments b
on a.department_id = b.department_id;

-- Oracle outer-join: 두개 컬럼의 (+)는 에러
select employee_id, emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id(+);

select * from students
where total >= 250;

select * from students
where name like '%a%';

-- union: 중복은 제외
-- union all: 중복 허용
select * from students
where total >= 250
union
select * from students
where name like '%a%';

select * from students
where total >= 250 or name like '%a%';

-- union: 같은 테이블, 다른테이블 모두 사용이 가능하고 컬럼의 타입만 맞으면 모두 출력
-- 조건 1. 위쪽쿼리문과 아래쪽 쿼리문 개수가 동일
-- 조건 2. 타입 무조건 일치
select employee_id no, emp_name, manager_id from employees
union
select no, name, kor from students;

-- 자유게시판, 공지사항, 이벤트, 종합게시판
-- 통합적으로 검색해서 출력하고 싶을 때 union

-- employees department_id가 50인 사원 검색 -> 부서번호, 부서이름
select a.department_id, department_name
from employees a, departments b 
where a.department_id = b.department_id and a.department_id = 50;
-- employees에 없는 departments의 부서 검색 -> 부서번호, 부서이름
select department_id, department_name 
from departments a
where not exists
(select 1 from employees b where a.department_id = b.department_id);
select distinct department_id from employees;
-- 두개를 union 하시오.
select a.department_id, department_name
from employees a, departments b 
where a.department_id = b.department_id and a.department_id = 50
union
select department_id, department_name 
from departments a
where not exists
(select 1 from employees b where a.department_id = b.department_id);

desc member; -- name, mdate
desc students; -- name, sdate

select name, mdate from member
union
select name, sdate from students;

create table board2 (
	bno number(4),
	btitle VARCHAR2(1000),
	bcontent clob,
	id VARCHAR2(30),
	bgroup number(4),
	bstep number(4),
	bindent number(4),
	bhit number(4),
	bdate DATE,
	bfile VARCHAR2(100)
);
select * from board2;
commit;

-- 8, 11, 12, 16, 21, 22, 25, 29, 35, 38, 44, 46, 57, 61, 66, 74, 88, 95, 96, 98
delete board2 where bno = 98;

select * from board2
where bno between 1 and 20;

-- rownum: 번호를 새롭게 부여
select rownum, bno, btitle, bdate from board2
order by bdate desc, btitle;
-- rownum 번호가 순서대로 정렬됨. 서브쿼리 사용
select rnum, bno, btitle from (select rownum rnum, bno, btitle from (select bno, btitle from board2 order by bdate desc))
where rnum between 11 and 20;
-- row_number() over(): 정렬한 후 번호를 부여
select rnum, bno, btitle, bdate from(
select row_number() over(order by bdate desc) rnum, bno, btitle, bdate from board2)
where rnum between 11 and 20;

-- 모든 컬럼 출력
select * from (
select row_number() over(order by bdate desc) rnum, a.* from board2 a)
where rnum between 11 and 20;

select * from (select rownum rnum, a.* from (select * from board2 order by bdate desc) a)
where rnum between 11 and 20;

-- rownum
select * from (select rownum rnum, a.* from (select no, name, avg, rank() over(order by avg desc) from students) a)
where rnum between 11 and 20;
-- row_number() over()
select * from(select row_number() over(order by avg desc) rnum, a.*, rank() over(order by avg desc) from students a)
where rnum between 21 and 30;

-- rank() 함수
select no, name, avg, rank() over(order by avg desc) from students;

-- rank() 값 rank 컬럼에 모두 입력하시오.
update students a set rank = (select ranks from (select no, rank() over(order by avg desc) ranks from students) b where a.no = b.no);
select * from students;
commit;

-- view
-- 상담원: 사원들 전화번호를 가지고 사원들에게 마케팅을 하려고 함
-- 100명에게 사원 테이블 오픈 제공해달라고 요청: 마케팅
-- 직원가 100만원 90% 10만원 아이폰16
create or replace view employees_view
as
select employee_id, emp_name, email, phone_number, hire_date
from employees;

-- employees_view
select * from employees_view;

-- 사원번호, 사원명, 이메일, 폰번호, 입사일, 부서번호, 부서명
select employee_id, emp_name, email, phone_number, hire_date, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id;

create or replace view emp_view
as
select employee_id, emp_name, email, phone_number, hire_date, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id;

select * from emp_view;

-- view 삭제
drop view emp_view;

-- view 컬럼 커멘트(주석-설명문) 추가
comment on column employees_view.employee_id is '사원번호에 해당됩니다.';
-- 커멘트 주석확인
select * from user_col_comments;
-- 테이블 커멘트 주석확인
select * from user_tab_comments;

create or replace view emp_view
as
select employee_id as e_id, emp_name as e_name from employees_view;

create table emp02(
    employee_id number(6),
    emp_name varchar2(80),
    hire_date date,
    salary number(8, 2),
    department_id number(6)
);
insert into emp02(employee_id, emp_name, hire_date, salary, department_id)
select employee_id, emp_name, hire_date, salary, department_id
from employees;

-- view 생성
-- with read only: select만 가능, insert, update, delete 불가
create or replace view emp02_view
as
select employee_id, emp_name, hire_date
from emp02
with read only;

-- view select
select * from emp02_view order by employee_id;

-- 단순 view: 1개 테이블로 구성된 것.
-- insert, update, delete 가능, not null 제약조건이 되어 있으면 insert 불가할 수도 있음.
-- 복합 view: 2개 이상 테이블 조인, 함수사용, group by 같은 경우는 insert, update, delete 불가

-- update 100번 이름 홍길동 변경
update emp02_view set emp_name = '유관순' where employee_id = 101;
commit;

insert into emp02_view values(207, '유관순', sysdate);
select * from emp02_view order by employee_id desc;

alter table emp02 modify salary number(8, 2) not null;

select * from emp02;

select * from students;
-- no: seq
-- 입력데이터: name, kor, eng, math
-- total: 오라클에서 입력
-- avg: 오라클에서 입력
-- rank: 오라클에서 입력
-- sdate: sysdate 오라클에서 입력

insert into students values(students_seq.nextval, name, kor, eng, math, kor + eng + math, (kor + eng + math) / 3.0, sysdate);

-- students 테이블 no가 가장 큰수
select max(no) from students;

-- avg 소수점 2ㅏ리 까지만 출력하시오.
-- no, name, kor, eng, math, total, avg, rank, sdate
select no, name, kor, eng, math, total, round(avg, 2), rank, to_char(sdate, 'yyyy-mm-dd') from students;

-- a가 포함되어 있는 이름을 검색하시오.
select * from students where name like '%a%';

select * from students order by name;

update students a set rank = (select ranks from (select no, rank() over(order by avg) ranks from students) b where a.no = b.no);
rollback;
select * from students order by rank;