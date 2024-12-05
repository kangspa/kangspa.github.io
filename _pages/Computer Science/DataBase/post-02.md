---
title: "NoSQL에 대해"
tags:
    - NoSQL
    - 확장성
    - 비정형데이터
date: "2024-11-28"
thumbnail: "https://jaro-website.s3.ap-south-1.amazonaws.com/2024/04/1-aft5e-gFeDW4DQ8tayEsrA.webp"
---
<a style="font-size:0.9rem" href="https://www.jaroeducation.com/blog/what-is-nosql/">- 출처 : What Is NoSQL? NoSQL Databases Explained</a>

***"테이블 간 관계를 정의하지 않고, 일반적으론 테이블 간 Join도 불가능."***
데이터 일관성은 포기하되 여러 대에 데이터를 분산 저장하는 수평적 확장성(Scale-Out)을 목표로 등장.
4가지 다양한 형태의 저장기술을 지원한다.
1. **Document Database** : Key와 Document 형태로 저장, 검색 최적화
2. **Graph Database** : 그래프 구조를 사용하여 데이터 표현 및 저장(객체와 관계를 그래프 형태로 표현), 데이터 간 관계가 탐색의 키일 경우 적합
3. **Key-Value Database** : Key와 Value 쌍으로 저장되며 어떠한 형태의 데이터라도 담을 수 있음(이미지나 비디오도 가능), API를 제공하여 질의 속도가 굉장히 빠른 편
4. **Wide Column Database** : 키에서 필드를 결정하고, 키는 Row(키 값), Column-family, Column-name을 가짐

## 특징
1. 유연성 : 자유로운 Schema-less 구조
2. 확장성 : Scale-out을 통한 서버 확장이 용이
3. 고성능 : 대용량 데이터 처리성능이 뛰어남
4. 가용성 : 여러 대 백업 서버 구성이 가능하여 무중단 서비스가 가능
5. 데이터 간 관계 정의를 안 함.
6. RDBMS에 비해 훨씬 더 대용량 데이터 저장 가능
7. 분산형 구조 : 여러 대의 서버에 분산해서 데이터를 저장
8. Key에 대한 입출력만 지원
9. Schema가 없다보니 Data에 대한 규격화된 결과 값을 얻기 힘듦.

## 장점
1. 자유로운 데이터 구조, 언제든 데이터 조정 및 새로운 필드 추가 가능
2. 데이터 분산이 용이하며, Scale-up 뿐만 아니라 Scale-out도 가능

## 단점
1. 데이터 중복 발생 우려가 있으므로 중복된 데이터가 변경 될 경우 수정을 모든 컬렉션에서 수정해야함.
2. 명확한 데이터 구조를 보장하지 않으며 데이터 구조 결정이 어려울 수 있음.
3. 데이터를 UPDATE할 경우 모든 컬렉션에서 수행해야 하여 작업이 느림.
4. key 값에 대한 입출력만 지원한다.

---

- 참고 : <https://hstory0208.tistory.com/entry/RDBMS와-NoSQL의-차이점-및-개념-완벽-정리>