---
title: Vector DB에 대해
tags:
    - vector
    - chroma
    - NLP
    - LLM
date: "2024-11-29"
---

# Vector DB란?
실시간 분석 및 검색에 특화된 데이터베이스로, 벡터 형태의 데이터 모델 사용 및 고차원 벡터로 데이터를 표현한다.
대량 데이터 신속 처리, 고속 쿼리 수행, 실시간 업데이트 데이터를 다룰 수 있단 특징이 있다.
비정형 데이터나 벡터 데이터 다루는데 특히 유용하다. 벡터 데이터를 다루기에 유사성 검색이 가능하다.

# Chroma DB
벡터 임베딩의 저장 및 검색을 위해 설계된 오픈 소스 벡터 데이터베이스이다.
LangChain, OpenAI 등 함께 사용이 용이하여, LLM과 같은 다른 모델에서 많이 사용된다.

관계형 데이터베이스의 테이블과 유사한, 컬렉션을 생성해야 한다.
많은 임베딩 모델을 활용하여 컬렉션 수정이 가능한데, 필자의 경우 `OpenAIEmbeddings(model="text-embedding-ada-002")`을 사용해서 프로젝트를 진행한 경험이 있다.
이후 메타데이터와 텍스트 문서를 컬렉션에 추가 하고, 컬렉션에서는 임베딩으로 변환하여 저장하게 된다.

---

- 참고
	- [2023 벡터 DB 선택을 위한 비교](https://discuss.pytorch.kr/t/2023-picking-a-vector-database-a-comparison-and-guide-for-2023/2625)
	- [벡터 데이터베이스란?](https://www.elastic.co/kr/what-is/vector-database)
	- [RDB와 Vector DB의 차이점](https://kosena.tistory.com/87)
	- [Chroma Vector DB를 사용해서 RAG (Retireval-Augmented Generation) 구현](https://rfriend.tistory.com/832)
	- [ChromaDB 개요: 벡터 데이터베이스](https://www.jiniai.biz/2023/10/29/chromadb-개요-벡터-데이터베이스)
	- [얼굴 탐색 속도 높이기 : 벡터 데이터베이스의 이해 및 활용 (feat. Chroma)](https://blog.kbanknow.com/66)