---
title: "RDBMS에 대해"
tags:
    - RDBMS
    - 관계형
    - 정형데이터
date: "2024-11-28"
thumbnail: "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Relational_database_terms.svg/350px-Relational_database_terms.svg.png"
---
<a style="font-size:0.9rem" href="https://en.wikipedia.org/wiki/Relational_database">- 출처 : Relational database</a>

***"관계형 데이터베이스 관리 시스템, 모든 데이터를 2차원 테이블 형태로 표현한 DB를 생성, 수정, 삭제, 관리하는 소프트웨어."***
관계를 나타내기 위해 외래 키를 사용하고, 외래 키를 이용한 테이블 간 Join이 가능하다는 것이 특징
외래 키 값을 참조하는 테이블은 '자식 테이블', 외래 키 값을 제공하는 테이블은 '부모 테이블' 이다.

## 특징
1. Column과 Row형태로 저장
2. 분류, 정렬, 탐색 속도가 빠르다.
3. SQL을 통해 데이터를 다룬다.
4. 작업의 완전성 보장
5. Schema 규격에 맞춰야한다. (유연한 데이터 저장 불가)
6. 수직확장만 가능하다. (부하 분산이 어려움)

## 장점
1. 명확한 데이터 구조 보장
2. 관계는 각 데이터를 중복없이 한번만 저장가능하게 함
3. 일관성 및 무결성 유지 가능

## 단점
1. 시스템이 커질 경우 JOIN이 많은 복잡한 쿼리발생
2. 성능 향상을 위해서는 서버 성능 향상을 위한 Scale-up만 지원하기에 비용이 기하급수적으로 늘어날 수 있음
3. 데이터가 유연하지 못하여 스키마 변경 시 번거롭고 어려움

---

- 참고 : <https://hstory0208.tistory.com/entry/RDBMS와-NoSQL의-차이점-및-개념-완벽-정리>