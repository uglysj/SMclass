-- 테이블 create할 때, foreign key 생성
create table board2(
    bno number(4) primary key,
    btitle varchar2(1000) not null,
    bcontent clob,
    id varchar2(30),
    constraint fk_board2_id foreign key(id) references bmember(id)
);

desc board;
-- 닉네임: id_fk, foreign key: id, bmember 테이블의 primary key: id 등록
alter table board add constraint id_fk foreign key (id) references bmember(id);

-- foreign key 삭제
alter table board drop constraint id_fk;

select * from board;
select * from bmember;

-- abc 글을 등록하면, 등록이 안됨.
insert into board values(
    board_seq.nextval, '제목6', '내용6', 'abc', board_seq.currval, 0, 0, 0, sysdate, ''
);

-- [ foreign key 등록된 id 삭제 방법 ]
-- bmember 테이블 id, foreign key로 board, board2 에 등록
-- foreign key: 외래키
-- 원본의 primary key 데이터를 지우려면, 원칙으로는 foregin key의 데이터를 모두 삭제해야 삭제가 됨.
-- foreign key를 해제해야 삭제 가능
-- primary key: 기본키
delete bmember where id = 'aaa';
delete board where id = 'aaa';
rollback;

select * from bmember;
select * from board;

alter table board drop constraint id_fk;

-- foreign key로 등록이 되면, primary key를 삭제할 때 foreign key에 데이터가 있으면 삭제가 안됨.
-- on delete cascade: primary key가 삭제가 되면, foreign key로 등록된 모든 글을 삭제 시킴.
alter table board add constraint id_fk foreign key (id) references bmember(id) on delete cascade;

-- on delete restricted
-- 기본값: 입력하지 않을 시, 자식데이터가 있을 경우, 부모데이터가 삭제가 되지 않음.
-- on delete cascade
-- 부모데이터 삭제시, 자식데이터 모두 삭제
-- on delete set null
-- 부모데이터 삭제시, 자식데이터에 해당되는 값이 null 표시
-- 외래키 삭제
alter table board drop constraint id_fk;
-- 1.
alter table board add constraint id_fk foreign key(id) references bmember(id);

select * from board;

-- 자식테이블에 aaa로 쓴 데이터를 삭제해야 id를 삭제할 수 있음.
delete bmember where id = 'aaa';
delete board where bno = 3;

-- 2. on delete cascade
-- 부모데이터 삭제시, 자식데이터 모두 삭제
alter table board add constraint id_fk foreign key (id) references bmember(id) on delete cascade;
-- 부모데이터를 삭제하면, 자식데이터의 모든 글이 삭제됨
delete bmember where in = 'aaa';
select * from board;

-- 3. on delete set null
-- 부모데이터 삭제시, 자식데이터에 해당되는 값이 null 표시
alter table board add constraint id_fk foreign key (id) references bmember(id) on delete set null;
-- 부모데이터를 삭제하면 자식데이터의 해당컬럼만 null 변경되고, 데이터는
delete bmember where id = 'aaa';
select * from board;

-- check 구문
create table emp01(
    empno number(4) primary key,
    ename varchar2(30) not null,
    salary number(7, 2) check(salary between 2000 and 20000),
    gender varchar2(10) check(gender in('Male', 'Female'))
);
-- check 가 지정되어 있는 컬럼에 추가
insert into emp01 values(1, '홍길동', 2500, 'Male');
-- salary 범위를 벗어나면 에러
insert into emp01 values(2, '유관순', 20000, 'Female');
-- Male, Female 이외 단어 입력 시 에러
insert into emp01 values(3, '이순신', 20000, 'male');

-- default: insert 시 값이 입력이 되지 않을 시, 문자, 숫자, 날짜를 넣을 수 있음
create table emp02(
    empno number(4) primary key,
    ename varchar2(30) default '무명',
    income number(4) default 0,
    salary number(7, 2) check(salary between 2000 and 20000),
    gender varchar2(10) check(gender in('Male', 'Female')),
    edate date default sysdate
);
insert into emp02 (empno, salary, gender) values(1, 5000, 'Male');
select * from emp02;
commit;

create table mem(
    id varchar2(30) primary key,
    pw varchar2(30) not null,
    name varchar2(30) default '무명',
    age number(3) default 0,
    birth date default sysdate,
    gender varchar2(6) check(gender in('Male', 'Female')),
    hobby varchar2(50) default 'game',
    mdate date default sysdate
);

insert into mem values('aaa', '1111', '홍길동', 24, '2000/05/05', 'Male', 'golf', sysdate);
insert into mem values('bbb', '1111', '유관순', 24, '2000/06/05', 'Female', 'book', sysdate);
insert into mem values('ccc', '1111', '이순신', 23, '2001/07/25', 'Male', 'game', sysdate);
commit;
select * from mem;

-- employees 테이블 부서별 개수, 부서번호, 부서이름, 그룹함수
select count(*) no, a.department_id dept, department_name deptname 
from employees a, departments b 
where a.department_id = b.department_id and a.department_id = 50
group by a.department_id, department_name;

desc mem;

select * from students;
desc students;

insert into students values(studnets_seq.nextval, '김유신', 99, 98, 96, (99 + 98 + 96), (99 + 98 + 96) / 3.0, 0, sysdate);