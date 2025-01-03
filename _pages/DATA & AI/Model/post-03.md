---
title: "RAG 모델"
tags:
    - LLM
    - RAG
    - 시맨틱 검색
date: "2024-11-26"
thumbnail: "https://docs.aws.amazon.com/images/sagemaker/latest/dg/images/jumpstart/jumpstart-fm-rag.jpg"
---
<a style="font-size:0.9rem" href="https://aws.amazon.com/ko/what-is/retrieval-augmented-generation/">- 출처 : 검색 증강 생성(RAG)이란 무엇인가요?</a>

Retrieval-Augmented Generation(RAG)은 LLM의 단점 중 **'사실 관계 오류 가능성'**과 **'맥락 이해의 한계'**를 개선하는 데 초점을 맞춘다.

### 보완하는 한계
1. 외부 지식 활용
    - 대규모 구조화된 지식베이스를 모델에 연결
    - 주어진 질의에 대한관련 정보를 지식 베이스에서 검색 및 추출
2. 증거 기반 생성
    - 검색된 지식 정보를 증거로 활용하여 사실에 기반한 답변 생성
    - 생성된 답변의 출처를 명시함으로써 신뢰성 향상
3. 맥락 이해력 향상
    - 외부 지식을 통해 질의에 대한 배경 지식과 맥락 정보를 파악
    - 단순한 패턴 매칭이 아닌 추론 능력을 바탕으로 한 답변 생성

### 주요 구성 요소
1. 질의 인코더
    - 사용자 질문을 이해하는 부분
    - 주어진 질문을 벡터 형태로 인코딩
2. 지식 검색기
    - 외부 지식 베이스에서 관련 정보 검색
3. 지식 증강 생성기
    - 검색된 지식을 활용하여(프롬프트) 답변 생성하는 부분 (LLM과 유사)

### 이점
1. 비용 효율적 구현
2. 최신정보 활용
3. 사용자 신뢰 강화
4. 개발자 제어 강화

---

## RAG 와 시맨틱 검색의 차이

###  시맨틱 검색
- 트리플(주어, 술어, 목적어) 형태로 이루어진 온톨로지(지식표현)를 사용하여 주어와 연계된 데이터를 연속적으로 찾아가며 의미 검색을 하는 것!

시맨틱 검색은 서로 다른 정보의 대규모 DB를 스캔하고 데이터를 정확하게 검색한다.
이를 기반으로 LLM에 더 많은 컨텍스트를 제공할 수 있다.
지식 기반 준비의 모든 작업을 수행하므로 개발자가 관여하지 않아도 된다.

### RAG
RAG는 지식 집약적 작업에 대해 제한된 결과를 제공하며, 개발자는 수동으로 데이터 준비를 할 때 워드 임베딩, 문서 청킹 등 문제를 해결해야 한다.

---

- 출처
    - <https://modulabs.co.kr/blog/retrieval-augmented-generation/>
    - <https://aws.amazon.com/ko/what-is/retrieval-augmented-generation/>
    - <https://naver.me/IDbtXrj2>