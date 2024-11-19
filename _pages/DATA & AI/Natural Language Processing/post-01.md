---
title: "텍스트 데이터 전처리 과정"
tags:
    - Python
    - 데이터 처리
date: "2024-11-19"
# thumbnail: "/assets/img/Project/GitBlog/post-05/thumbnail.png"
---

### 문장 분리
텍스트를 문장 단위로 분리해준다.
간단하게는 `.split()`을 이용해서, 개행문자 단위로, 혹은 '.' 단위로 문장을 끊을 수도 있으나, 이는 불확실한만큼 보통은 외부 라이브러리를 사용한다.

```python
import nltk
nltk.sent_tokenize(sentence)
```

대표적으로 nltk를 사용하지만, 이것 또한 불확실해서 참고한 글에서는 `tokenizers/punkt/english.pickle`를 불러와서 추가로 약어들을 학습시키고, 문장 분리하는 것을 보기도 하였다.

### 토큰화
토큰 단위, 일반적으로 단어 단위로 분리해준다. '일반적으로'란 의미는, 상황에 따라 문장 단위로 토큰화를 할 필요가 있을 수도 있고, 특수 문자를 붙인다거나 따로 해야할 필요가 있을 수도 있기 때문이다.
때문에 다양한 툴들이 있으며, 상황에 맞게 사용해주면 된다.

```python
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from tensorflow.keras.preprocessing.text import text_to_word_sequence
from nltk.tokenize import TreebankWordTokenizer
```

한국어의 경우 띄어쓰기만으로 토큰화를 하기 어려운만큼, 형태소를 활용하여 토큰화 처리를 한다.
대표적으로 Okt, Mecab, Komoran, Hannanum, Kkma 등의 툴들이 존재한다.

```python
from konlpy.tag import Okt
from konlpy.tag import Kkma
```

### 불용어 제거 및 특수 문자 제거
의미 없는 글자(불용어)나 필요하다면 특수 문자도 제거해준다.
자주 등장하지만, 큰 의미가 없는 불용어는 다른 단어와 높은 연관성을 보여준다거나, 자주 등장했다는 점 하나로 높은 가중치를 받아 모델 학습 시 노이즈를 일으킨다.
특수 문자의 경우 의미를 갖고 있어 제거보다는 하나의 토큰으로 분리하는게 좋을 수도 있다. 다만 일반적인 경우에는 일단 제거해주는게 방법일 수 도 있다.

영어에서는 또다시 `nltk`를 활용하여 불용어 제거를 시도 한다.

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english')) 

word_tokens = word_tokenize(sentence)

result = []
for word in word_tokens: 
    if word not in stop_words: 
        result.append(word) 
```

한국어에서는 다양한 불용어 리스트를 별도로 만들어서, txt 파일 등으로 읽어들인 후 위와 같이 처리하는 경우가 많다.
물론 불용어 기준은 모든 사람마다 다르고, 상황에 따라 또 다른만큼 신경써서 진행해주면 된다.

### 대소문자 통일 및 서로 다른 표현 통일화
서로 다른 표현법을 가진 같은 글자들을 하나로 통일시켜준다.
이러한 과정을 정규화 및 정제 라고 많이 말하며, 어간 추출이나 정규 표현식 등을 활용해 많이 처리해준다.
[해당 링크](https://blog.naver.com/j7youngh/222793453503)는 정규 표현식에 대해 정리가 잘 돼 있어 첨부한다.

### 표제어 추출
단어의 원형으로 변형시켜서 단어의 수를 줄여준다.
- stemming : 단어의 어간을 추출
- lemmatization : 단어의 원형 추출

---

- 참고
	- <https://applepy.tistory.com/88>
	- <https://cryptosalamander.tistory.com/140>
	- <https://wikidocs.net/21698>
	- <https://wikidocs.net/22530>