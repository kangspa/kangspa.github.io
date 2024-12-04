---
title: "임베딩과 벡터"
tags:
   - Python
   - Embedding
   - vector
   - Word2Vec
date: "2024-11-21"
thumbnail: "/assets/img/DATA & AI/Natural Language Processing/post-02/thumbnail.png"
---

# Embedding 임베딩

임베딩은 객체를 연속 벡터 공간의 점으로 표현하는 수단이다.
벡터는 동일 유형의 스칼라를 포함하는 1차원 '텐서'라고 한다. 간단히 말하면 1차원 배열로 표현된 숫자라고 할 수 있다.

- Tensor(텐서) : n차원 공간의 숫자 배열 또는 숫자 배열의 집합을 총칭하는 용어
- Scalar(스칼라) : 0차원 텐서, 크기만 갖는 값
- Vector(벡터) : 동일한 유형의 데이터의 여러 스칼라를 포함하는 1차원 텐서, 크기와 방향을 갖는 값
- Tuple(튜플) : 두 가지 이상의 데이터 유형으로 구성된 스칼라를 포함하는 1차원 텐서
- Matrix(행렬) : 동일한 유형의 데이터를 가진 여러 벡터를 포함하는 2차원 텐서
   - 행 또는 열인 스칼라의 2차원 그리드로 시각화 할 수 있는 유형

- 참고
   - <https://www.ibm.com/kr-ko/topics/embedding>
   - <https://www.ibm.com/kr-ko/think/topics/vector-embedding>

## Sparse vector (희소 표현)

간단히 말하면 one-hot encodding이라고 할 수 있다.
단어 인덱스만 1이고 나머지는 전부 0으로 표현하는 방법이다.
단어 개수가 늘어날수록 벡터의 차원이 한없이 커지는 단점으로 인해, 공간적 낭비가 심하다.
즉 단어 수가 1만개 라면, 총 차원이 10,000 이 되어야 한다.

## Dense vector (밀집 표현)

사용자가 설정한 값으로 모든 단어의 벡터 차원을 맞춘다.
즉, 128을 값으로 맞춘다고 하면, 모든 단어는 128 차원 이내에서 실수값을 갖는 벡터로 표현이 가능하다.

이 기법으로 단어를 표현하는 것을 워드 임베딩(word embedding) 이라고 하며, 이렇게 나온 밀집 벡터를 임베딩 벡터(embedding vector)라고 한다.
방법론으로는 LSA, Word2Vec, FastText, Glove 등의 방법 등이 있다.

## Word2Vec

희소 표현(sparse representation)은 단어 벡터 간 유사성을 표현할 수 없다.
대안으로 다차원 공간에 의미를 벡터화 하는 **분산 표현(distributed representation)**을 사용하고,
이를 통해 단어 간 유사성을 벡터화 하는걸 임베딩이라하여, 표현된 벡터는 임베딩 벡터라고 한다.
이 단어 벡터 간 유의미한 유사도를 계산하는 대표적인 학습 방법이 **Word2Vec**이다.

**Word2Vec**은 워드 임베딩이 목적이라, 중심 단어를 에측하여 학습한다. 이는 타겟 단어 전후를 모두 참고한다는 것을 뜻한다.
또한 은닉층이 존재하지 않아 속도가 빠르고, 연산에 log를 사용하여 더욱 빠른 연산 속도를 보여준다.

- 참고
   - <https://wikidocs.net/33520>
   - <https://wikidocs.net/22660>