-- create 테이블 생성, alter 테이블 수정, drop 테이블 삭제
create table member(
    no number(4),
    id varchar2(20),
    pw varchar2(20),
    name varchar2(20),
    phone varchar2(20),
    mdate date
);

-- insert 데이터 입력, select 데이터 검색, update 데이터 수정, delete 데이터 삭제
insert into member values(
    1, 'aaa', '1111', '홍길동', '010-1111-1111', '2024-10-29'
);

insert into member values(
    2, 'bbb', '1111', '유관순', '010-2222-2222', '2024-09-20'
);

-- select 데이터 검색
select * from member;

commit;
rollback;

-- delete 삭제
-- delete member where no = 2;
-- delete member;

-- update 수정
update member set name = '홍길자' where no = 1;
-- where 조건절이 없으면 모두 바뀜
update member set name = '김구';

select * from member;

-- create 테이블 생성
create table students(
    stuno number(4),
    name varchar2(20),
    kor number(3),
    eng number(3),
    total number(3),
    sdate date
);

insert into students values(
    1, '홍길동', 100, 100, 100 + 100, sysdate
);

commit;

-- 모든 컬럼 검색
select * from students;
-- 특정컬럼을 입력하면 특정 컬럼만 검색
select name, sdate from students;

-- 특정컬럼만 입력하면 특정 컬럼만 저장
insert into students (stuno, name) values(
    2, '유관순'
);
select * from students;

select * from employees;
select count(*) from emp2;
-- 테이블을 생성하면서 테이블 내용을 모두 복사
create table emp2 as select * from employees;
select * from emp2;
-- 데이터 개수
select count(*) from emp2;

-- 테이블을 생성하면서 테이블 구조만 복사
create table emp3 as select * from employees where 1 = 2;
select * from emp3;

-- 테이블이 존재 할 경우 데이터만 복사
create table member2 as select * from member where 1 = 2;
insert into member2 select * from member;

-- 컬럼 데이터 타입, 길이 변경
-- alter 변경 member 테이블 no 컬럼의 타입 길이를 변경
alter table member modify no number(10);
-- alter 변경, 컬럼의 이름을 변경
alter table member rename column no to memberNo;
-- alter 변경, 컬럼의 데이터 타입 변경
update member set no = '';
select * from member;
commit;
alter table member modify no varchar2(10);
desc member;

-- 대소문자 구분 없음
SELECT * FROM MEMBER;
select * from member;
select memberno from member;
SELECT MEMBERNO FROM MEMBER;
SELECT memberno from member;

-- 테이블 안에 내용은 대소문자 구분함.
select * from member where id = 'aaa';
SELECT * FROM MEMBER WHERE ID = 'AAA';

-- 테이블 구조
desc employees;

-- employees 테이블에서 사원번호(employee_id), 사원명(emp_name) , 입사일(hire_date)
select employee_id, emp_name, hire_date from employees;
select * from employees;

-- 연산자: 산술연산자(+, -, *, /)
create table member (
	id VARCHAR2(50),
	pw varchar2(4),
	name VARCHAR2(50),
	email VARCHAR2(50),
	phone VARCHAR2(50),
	gender VARCHAR2(50),
	hobby varchar2(50),
	mdate DATE
);
select * from member;

create table students (
	no number(4),
	name VARCHAR2(50),
	kor number(3),
	eng number(3),
	math number(3),
	total number(3),
	avg number,
	rank number(3),
	sdate DATE
);
select * from students;
commit;

select kor, eng, (kor + eng) from students;
select kor, eng, (kor + eng), abs(kor - eng) from students;

select * from employees;
-- 문자 더하기안됨.
select emp_name + email from employees;
-- concat 명령어, ||
select concat(employee_id, emp_name) from employees;
select employee_id || emp_name from employees;

-- 달러환산 1384
select salary from employees;
select salary * 1384 from employees;
-- 문자로 변환, 천단위 표시
select to_char(salary * 1384, '999,999,999') from employees;
select emp_name, salary, salary * 1384 from employees;

create table stu(
    no number(4),
    name varchar2(20),
    kor number(3)
);
-- null 값 검색: is null
select * from stu where name is null;
-- null 값이 아닌 것 출력: is not null
select commission_pct from employees where commission_pct is not null;

select salary from employees;
-- 연봉 계산 * 12
select salary, salary * 12 from employees;
select salary, salary * 12, salary * 12 * 1384 from employees;

-- commission_pct 가 없는 사원은 null 값이 있는데, null +, -, *, / 해도 null값으로 변경
select salary, salary * 12, salary * 12 + (salary * 12) * commission_pct * 0.01 from employees;
-- 컬럼명 별칭 사용 as
select salary, salary * 12 as "연 봉", salary * 12 + (salary * 12) * nvl(commission_pct, 0) * 0.01 as "r e al_yearsalary" from employees;

-- nvl() 함수, nvl(kor, 0): kor 컬럼에 null 값이 있으면 0으로 표시
select * from stu;
select no, name, kor, kor + 100 from stu;
select no, name, kor, nvl(kor, 0) + 100 from stu;

-- 번호, 이름, 국어, 영어, 수학, 합계, 평균, 등수, 입력일 컬럼명 별칭을 사용해서 출력하시오
select * from students;
select no as 번호, name as 이름, kor as 국어, eng as 영어, math as 수학, total as 합계, avg as 평균, rank as 등수, sdate as 입력일 from students;

-- 사원번호, 사원명, 이메일을 합쳐서 출력하시오.
select * from employees;
select employee_id || emp_name || email from employees;
select concat(concat(employee_id, emp_name), email) from employees;
select emp_name || ' is a ' || job_id from employees;

-- 중복제거: distinct
select department_id from employees;
select distinct department_id from employees;
-- 정렬: order by - asc(생략가능) 오름차순, desc - 내림차순
select distinct department_id from employees order by department_id desc;

-- job_id 중복제거해서 출력
select job_id from employees;
select distinct job_id from employees;

-- 문자열 자르기: substr(0, 2) = 0, 1 (2)앞까지 출력  
select substr(job_id, 0, 2) from employees;
-- 4번째 부터 시작하는 컬럼데이터를 가져와서 중복을 제거함.
select distinct substr(job_id, 4) from employees;

-- where절: 조건비교연산자 >, <, >=, <=, =, !=
select * from employees;
select * from employees where manager_id = 124;
select * from employees where job_id = 'SH_CLERK';
select * from employees where employee_id > 100;

-- students 테이블에서 합계가 250 이상인 것만 출력하시오.
select * from students where total >= 250;

-- 합계 250 이상이면서, kor 90점 이상인 것을 출력하시오.
select * from students where total >= 250 and kor >= 90;

-- 영어점수 70 이상, 90이하 출력하시오.
select * from students where eng >= 70 and eng <= 90;

-- 월급이 5000이상 8000이하 출력
select * from employees where salary >= 5000 and salary <= 8000;

-- 월급이 7000이 아닌 것을 출력하시오. !=, <>, ^=
select * from employees where salary != 7000;

-- 부서(department_id) = 50
-- count 개수 확인
select * from employees where department_id = 50;
select count(*) from employees where department_id = 50;
-- 50번이 아닌 것을 출력
select * from employees where department_id != 50;
select count(*) from employees where department_id != 50;

-- null 값은 count() 포함되지 않음
select count(*) from employees where department_id is null;
select count(employee_id) from employees; -- 107개
select count(department_id) from employees; -- 106개, null 값 1개가 있기에 106개가 출력

-- 급여 4000이하, 사원번호, 사원명, 급여 컬럼만 출력하시오. as 생략가능
select employee_id 사원번호, emp_name 사원명, salary 급여 from employees where salary <= 4000;

-- 숫자 비교연산자 가능, 날짜 비교연산자 가능
select emp_name, hire_date from employees;
select emp_name, hire_date from employees where hire_date >= '2002/01/01';
-- 1999/12/31 이전에 입사한 사람을 출력하시오.
select emp_name, hire_date from employees where hire_date < '1999/12/31';
-- 2001/01/01 부터 2004/12/31 까지 출력하시오.(2001-01-01, 20010101 가능)
select emp_name, hire_date from employees where hire_date > '20010101' and hire_date < '20041231';

-- 논리연산자
-- 국어점수가 90점 이상 또는 영어점수가 90점 이상을 출력하시오.
select count(*) from students where kor >= 90 or eng >= 90;
select count(*) from students where kor >= 90 and eng >= 90;
select count(*) from students where not kor >= 90;

-- 부서번호 - 80 department_id, job_id = MAN
select * from employees;
select * from employees where department_id = 80 and substr(job_id, 4) = 'MAN';
select * from employees where department_id = 80 and job_id = 'SA_MAN';

-- 0.2, 0.3, 0.5 or 연산자 사용
select commission_pct from employees where commission_pct is not null;
select commission_pct from employees where commission_pct = 0.2 or commission_pct = 0.3 or commission_pct = 0.5;
-- in 연산자
select commission_pct from employees where commission_pct in (0.2, 0.3, 0.5);

-- 사원번호(employee_id) 110, 120, 130 출력
select * from employees where employee_id = 110 or employee_id = 120 or employee_id = 130;
select * from employees where employee_id in (110, 120, 130);

-- 150 - 170 사원번호 출력
select * from employees where employee_id > 150 and employee_id < 170;
-- between - and: <= 포함이 되어 있는 경우만 해당
select * from employees where employee_id between 150 and 170;

-- 날짜 in
select hire_date from employees;
select hire_date from employees where hire_date in ('2004/02/17', '2002/06/07');
-- 날짜 between
select hire_date from employees where hire_date between '2002/06/17' and '2004/12/31';

-- job MAN 출력
select * from employees where substr(job_id, 4) = 'MAN';

-- LIKE 연산자: 포함되어 있는 글자를 검색할 때 사용
-- MAN으로 끝나는 단어를 검색
select * from employees where job_id like '%MAN';
-- ST로 시작되는 단어를 검색
select * from employees where job_id like 'ST%';
-- EMP_NAME에서 a가 들어가 있는 이름 출력
select * from employees where emp_name like '%a%';
-- EMP_NAME에서 두번째 자리에 t가 들어가 있는 이름 출력
select * from employees where emp_name like '_t%';
-- EMP_NAME에서 네번째 자리에 v가 들어가 있는 이름 출력
select * from employees where emp_name like '___v%';
-- EMP_NAME 뒤에서 두번째 자리에 l이 들어가 있는 이름 출력
select * from employees where emp_name like '%l_';
-- EMP_NAME 첫번째 자리에 D가 들어가 있는 이름 출력
select * from employees where emp_name like 'D%';