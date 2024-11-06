-- dual: 임시 가상 테이블
select sysdate from dual;
select sysdate - 30, sysdate, sysdate + 30 from dual;

-- employees 테이블 안에 hire_date 컬럼
select hire_date - 1, hire_date, hire_date + 1 from employees;

-- 날짜 범위 검색 가능, 정렬 oreder by, asc: 순차정렬, desc: 역순정렬
select emp_name, hire_date from employees where hire_date >= '02/01/01' and hire_date <= '04/12/31' order by hire_date desc;
select emp_name, hire_date from employees where hire_date between '02/01/01' and '04/12/31' order by hire_date;

-- like
select emp_name from employees where emp_name like '___a%';
select emp_name from employees where emp_name like '%a_';

-- 정렬 desc: null 값이 제일 위에 검색, asc: 제일 아래에 검색
select department_id from employees order by department_id desc;

-- 월급(salary) 역순 정렬
select emp_name, salary from employees order by salary desc;

-- students 테이블에서 total 역순 정렬
select no, name, total from students order by total desc;

-- hire_date 기준 순차정렬
select * from employees order by hire_date;

select name, kor, eng, math from students order by kor desc;

-- 한국어 순차정렬: ㄱ, ㄴ, ㄷ... 역순정렬: ㅎ, ㅍ, ㅌ...
select name from students order by name;

-- 입사일이 빠른 순으로 정렬하는데, 이름은 역순으로 정렬 하시오.
select emp_name, hire_date from employees order by hire_date, emp_name desc;

-- abs 절대값
select -10 val, abs(-10) as abs from dual;

select kor, kor - eng, abs(kor - eng) abs from students order by abs desc;

-- floor 소수점 이하 버림
select 3.141592, floor(3.141592) from dual;
-- trunc 버림, 자리수 지정
select 34.5678, trunc(34.5678, 2) from dual;
select 34.5678, trunc(34.5678, -1) from dual;

-- ceil 소수점 이하 올림
select 3.14592, ceil(3.14592) from dual;

-- round 반올림, 자릿수 범위 지정
select 34.5678, round(34.5678) from dual;
-- 소수점 둘째자리 출력, 셋째자리에서 반올림.
select 34.5678, round(34.5678, 2) from dual;
-- 양수 첫째자리에서 반올림, 소수점 자릿수에서 앞쪽으로 한칸위치 반올림
select 34.5678, round(34.5678, -1) from dual;

-- mod 나머지
select 27 / 2, mod(27, 2) from dual;
select 31 / 7, mod(31, 7) from dual;

-- 사원번호가 홀수인 사원을 출력하시오.
select employee_id, emp_name from employees where mod(employee_id, 2) = 1;

-- 최종연봉: 월급 * 12 + (월급 * 12) * 커미션, 소수점 두번째자리에서 반올림. 첫째자리로 만드시오.
select emp_name, salary, round(salary * 12 + ((salary * 12) * nvl(commission_pct, 0)) * 1381.86795, 1) as year_salary from employees;

-- 시퀀스: 자동으로 번호 부여
create sequence stu_seq
    start with 1
    increment by 1
    minvalue 1
    maxvalue 9999
    nocycle
    nocache;
    
-- 시퀀스에서 번호생성
select stu_seq.nextval from dual;
-- 시퀀스 현재번호
select stu_seq.currval from dual;

-- 게시판 테이블 생성
create table board(
    bno number(4),
    btitle varchar2(100),
    bcontent varchar2(4000),
    id varchar2(30),
    bhit number(10),
    bdate date
);
insert into board values(1, '제목입니다.', '내용입니다.', 'aaa', 1, sysdate);
insert into board values(2, '제목입니다.2', '내용입니다.2', 'aaa', 1, sysdate);
insert into board values(stu_seq.nextval, '제목입니다.', '내용입니다.', 'aaa', 1, sysdate);
commit;

create sequence board_seq
    start with 7 -- 시작번호
    increment by 1 -- 증감숫자
    minvalue 1 -- 최솟값
    maxvalue 9999 -- 최댓값
    nocycle -- 1~9999 이상이 되면, 다시 1
    nocache; -- 메모리에 시퀀스값 미리할당

insert into board values(board_seq.nextval, '제목14', '내용14', 'aaa', 1, sysdate);
select * from board;

update board set btitle = '제목을 다시 변경' where bno = 7;

-- drop table board;

create table board(
    bno number(4),
    btitle varchar2(100),
    bcontent clob, -- 대용량 글자 타입
    id varchar2(20),
    bgroup number(4), -- 답변달기 그룹핑
    bstep number(4), -- 답변달기 경우 순서정의
    bindent number(4), -- 답변달기 들여쓰기
    bhit number(10), -- 조회수
    bdate date -- 등록일
);

insert into board values(board_seq.nextval, '제목1', '내용1', 'aaa', board_seq.currval, 0, 0, 1, sysdate);

select * from board;

-- 시퀀스 생성
-- students_seq.nextval
-- students 테이블 100 -> 101
-- 101, '홍길순', 99, 99, 90, total, avg, rank, sdate
-- 1명을 입력하시오.
create sequence students_seq
    start with 101
    increment by 1
    minvalue 1
    maxvalue 9999
    nocycle
    nocache;
insert into students values(students_seq.nextval, '홍길순', 99, 99, 90, (99 + 99 + 90), (99 + 99 + 90)/ 3.0, 0, sysdate);
commit;

select no, name, kor, eng, math, total, round(avg, 2), rank, sdate from students;
select round(avg, 2) from students;
select s.*, round(avg, 2) from students s;

select dept_seq.nextval from dual;

-- s_seq
-- 시작 1, 증분 1, 최댓값 99999
create sequence s_seq
    start with 1
    increment by 1
    minvalue 1
    maxvalue 99999
    nocycle
    nocache;

-- 시퀀스 생성, nextval: 다음 시퀀스번호 생성, currval: 현재시퀀스 번호 보여줌
select s_seq.nextval from dual;
select emp_seq.nextval from dual;
select emp_seq.currval from dual;

-- 타입
-- 문자형, 숫자형, 날짜형
-- char, varchar2, nchar, nvarchar2, long, clob
-- char, varchar2: 한글문자 입력시 3byte 사용
-- varchar2(6): 한글 2글자입력
-- nvarchar2(5): 한글 입력 5자리까지 가능 - 2byte
-- number
-- date - 초까지 입력, timestamp - 밀리세컨드 까지 입력

select '홍길동' from dual;
-- length: 문자길이
select length('홍길동') from dual;
-- 이름의 길이로 역순 정렬
select name, length(name) n from students order by n desc;
-- lengthb: byte 크기
select lengthb('홍길동') from dual;

-- 합계 200점 이상이면서, 번호 10이상 50 이하이면서 이름의 2번째 자리에 e가 들어가있는 학생을 출력
select * from students where total >= 200 and no >= 10 and no <= 50 and name like '_e%';

-- 이중쿼리
select * from (
    select * from students where total >= 200
) where name like '_e%' and no >= 30;

-- 등수함수 rank() over(기준점) 입력, no 중복이 없음. 유일키, 기본키, primary key
select no, rank() over(order by total desc) ranks from students;
select ranks from (select no, rank() over(order by total desc) ranks from students);

select no, name, total, rank from students order by total desc;

-- 수정: update
update students a set rank = (select ranks from (select no, rank() over(order by total desc) ranks from students) b where a.no = b.no);

update students a set rank = 1 where a.no = 101;

select * from students order by rank;

select no, rank() over(order by total desc) as ranks from students;

update students set rank = 1 where no = 101;
update studetns set rank = 2 where no = 96;
update students set rank = 3 where no = 64;
update students set rank = 4 where no = 49;
update sutdnets set rank = 5 where no = 14;

-- 사원번호가 높은 순으로 등수를 생성하시오.
-- 사원번호, 사원명, 등수
select employee_id, emp_name, rank() over(order by employee_id desc) as ranks from employees;

-- emp2 테이블 복사, employees 테이블
create table emp2 as select * from employees;

-- rank() 실행
select rank() over(order by employee_id desc) from employees;
desc emp2;

-- 테이블 rank 컬럼 추가
alter table emp2 add rank number(4);
desc emp2;
select * from emp2;

-- rank() 등수를 rank에 입력
update emp2 e set rank = (select ranks from (select employee_id, rank() over(order by employee_id desc) ranks from employees) e2 where e.employee_id = e2.employee_id);

select employee_id, rank from emp2 order by employee_id desc;

select * from emp2;

-- 컬럼의 순서를 변경
-- emp_name 뒤에 rank 컬럼을 배치
-- 컬럼 숨김처리
alter table emp2 modify email invisible;
alter table emp2 modify phone_number invisible;
alter table emp2 modify hire_date invisible;
alter table emp2 modify salary invisible;
alter table emp2 modify manager_id invisible;
alter table emp2 modify commission_pct invisible;
alter table emp2 modify retire_date invisible;
alter table emp2 modify department_id invisible;
alter table emp2 modify job_id invisible;
alter table emp2 modify create_date invisible;
alter table emp2 modify update_date invisible;
-- 컬럼 숨김처리 해제
alter table emp2 modify email visible;
alter table emp2 modify phone_number visible;
alter table emp2 modify hire_date visible;
alter table emp2 modify salary visible;
alter table emp2 modify manager_id visible;
alter table emp2 modify commission_pct visible;
alter table emp2 modify retire_date visible;
alter table emp2 modify department_id visible;
alter table emp2 modify job_id visible;
alter table emp2 modify create_date visible;
alter table emp2 modify update_date visible;

alter table emp2 modify rank invisible;
alter table emp2 modify rank visible;

select * from emp2;

-- 컬럼 삭제
desc emp2;
alter table emp2 drop column email;
alter table emp2 drop column phone_number;
alter table emp2 drop column hire_date;
alter table emp2 drop column salary;
alter table emp2 drop column commission_pct;
alter table emp2 drop column retire_date;
alter table emp2 drop column create_date;
alter table emp2 drop column update_date;

select * from departments;
desc departments;

alter table emp2 add department_name varchar2(80);
-- 부서명이 없음
select * from emp2;
-- 부서명은 departments
select * from departments;

select department_id, department_name from emp2;
select department_id, department_name from departments;

-- 부서명 입력
update emp2 e set department_name = (select dname from (select department_id, department_name dname from departments) d where e.department_id = d.department_id);

-- 테이블 복사
create table stu as select * from students;
desc stu;

alter table stu drop column rank;

select * from stu;
-- total 컬럼, avg 컬럼 추가
alter table stu add total number(3);
alter table stu add avg number;
alter table stu add rank number(3);

alter table stu modify sdate invisible;
alter table stu modify sdate visible;

-- 합계, 평균 추가
update stu set total = kor + eng + math, avg = (kor + eng + math) / 3.0;

-- rank 입력
update stu s set rank = (select ranks from (select no, rank() over(order by total desc) ranks from stu) b where s.no = b.no);
commit;

-- 날짜 함수
-- 현재 날짜: sysdate
select sysdate from dual;
select sysdate - 1 from dual;
select sysdate + 30 from dual;

create table datetable (
    no number(4),
    predate date,
    today date,
    nextdate date
);

-- 회원가입 한달치, 6개월, 1년
insert into datetable values(1, sysdate - 30, sysdate, sysdate + 180);
select no, predate, today as 가입일, nextdate as 만료일 from datetable;

select * from member;
select id, name, mdate, sysdate, round(sysdate - mdate) from member;
select id, name, mdate, sysdate, round(sysdate - mdate) from member where sysdate >= mdate + 180;

-- 입사일 현재날짜와 입사일 며칠 지났는지 출력하시오.
-- employees, hire_date
select emp_name, hire_date, sysdate, round(sysdate - hire_date) from employees;

-- 15일 이상이면 1달을 올림, 15일 미만이면 일을 초기화
select hire_date, round(hire_date, 'month') from employees;

-- 일을 모두 1로 초기화
select hire_date, trunc(hire_date, 'month') from employees;

-- 입사일, 현재일 기준의 달수
select hire_date, sysdate, months_between(sysdate, hire_date) from employees;
-- months_between: 두 일자 가운데 지나간 달수를 알려줌
select hire_date, sysdate, round(months_between(sysdate, hire_date)) 달수, round(sysdate - hire_date) 일수 from employees;

-- add_months 3개월 추가
select hire_date, add_months(hire_date, 3) from employees;

-- next_date: 다음 주 수요일 날짜를 알려줌
select next_day(sysdate, '수요일') from dual;
select sysdate, next_day(sysdate, '토요일') from dual;

-- last_day: 그 달의 마지막 날짜를 알려줌
select hire_date, last_day(hire_date) from employees;
select sysdate, last_day(sysdate) from dual;

-- 형변환 함수
select sysdate from dual;
select to_char(sysdate, 'YYYY/MM/DD HH24:MI:SS') from dual;

select hire_date from employees;
select hire_date, to_char(hire_date, 'YYYY-MM-DD') from employees;
select to_char(to_date('24/01/01'), 'yyyy/mm/dd hh24:mi:ss') from dual;
select to_char('24/01/01', 'yyyy-mm-dd') from dual;
-- 입력의 타입: 날짜형이 되어야 함.
select to_char(to_date('24/01/01'), 'yyyy-mm-dd') from dual;

select * from member where id = 'aaa' and pw = '1111';
select * from member;

update member set id = 'abc', pw = '1111', name = '이상준', email = 'sjlee_0220@naver.com' where id = 'Trineman';
commit;

select * from member where id = 'eee';
desc member;