<!-- ---
title: "sparse vector 와 dense vector 차이"
tags:
   - Python
   - 데이터 처리
date: "2024-11-19"
# thumbnail: "/assets/img/Project/GitBlog/post-05/thumbnail.png"
--- -->

 - **Sparse vector** : one-hot vectors, 단어 인덱스만 1이고 나머지는 전부 0으로 표현
    단어 개수가 늘어날수록 벡터의 차원이 한없이 커지는 단점이 있다. (공간적 낭비)
 - **Dense vector** : word embedding(embedding vector), 사용자가 설정한 값으로 모든 단어의 벡터 차원을 맞춘다.
    LSA, Word2Vec, FastText, Glove 등의 방법 등이 있다.
 - 출처 : <https://wikidocs.net/33520>

 - **Word2Vec** 에 대한 설명
    희소 표현(sparse representation)은 단어 벡터 간 유사성을 표현할 수 없다.
    대안으로 다차원 공간에 의미를 벡터화 하는 **분산 표현(distributed representation)**을 사용하고,
    이를 통해 단어 간 유사성을 벡터화 하는걸 임베딩이라하여, 표현된 벡터는 임베딩 벡터라고 한다.
    이 단어 벡터 간 유의미한 유사도를 계산하는 대표적인 학습 방법이 **Word2Vec**이다.
- 출처 : <https://wikidocs.net/22660>