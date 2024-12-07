---
title: "LangChain Expression Language(LCEL)"
tag:
    - LangChain
    - LCEL
date: "2024-12-07"
thumbnail: "/assets/img/Project/LangChain/post-04/thumbnail.png"
---

`LCEL` 이란, LangChain을 쉽게 구성할 수 있도록 도와주는 '선언적 언어'라고 한다.
간단히 말하자면, 원래는 각 단계를 선언하고 모델에 넣고 파싱해주는 일련의 단계를 체인으로 구성하여 한번에 끝내는 방식을 말해준다고 보면 될 것 같다.

기본적으로 아래와 같이 `unix 파이프 연산자`처럼 구성한다고 한다.

```python
chain = prompt | model | output_parser
```

여기서 `prompt`는 `from langchain_core.prompts import PromptTemplate` 을 활용하여 미리 작성해두는 프롬프트에 해당한다.
`output_parser`는 `from langchain_core.output_parsers import StrOutputParser`에 해당하며, 모델의 답변을 지정해둔 양식으로 파싱해주는 패키지에 해당한다.
각 `prompt`와 `output_parser`는 각각 `CH-02`, `CH-03`에서 다루게 되니 간단히 아래와 같이 선언해서 사용한다고 생각하고 넘어간다.

```python
template = """
당신은 영어를 가르치는 10년차 영어 선생님입니다. 상황에 [FORMAT]에 영어 회화를 작성해 주세요.

상황:
{question}

FORMAT:
- 영어 회화:
- 한글 해석:
"""

# 프롬프트 템플릿을 이용하여 프롬프트를 생성합니다.
prompt = PromptTemplate.from_template(template)

# ChatOpenAI 챗모델을 초기화합니다.
model = ChatOpenAI(model_name="gpt-4o-mini")

# 문자열 출력 파서를 초기화합니다.
output_parser = StrOutputParser()

# 체인을 구성합니다.
chain = prompt | model | output_parser
```

이렇게 구성한 `chain`은 표준 인터페이스로 다음과 같은 3가지 메소드가 포함되어 있다고 한다.
- `stream` : 응담의 청크를 스트리밍
- `invoke` : 입력에 대해 체인을 호출
- `batch` : 입력 목록에 대해 체인 호출

이와 함께, 비동기 메소드도 아래와 같이 포함되어 있다고 한다.
- `astream` : 비동기적으로 응답의 청크를 스트리밍
- `ainvoke` : 비동기적으로 입력에 대해 체인을 호출
- `abatch` : 비동기적으로 입력 목록에 대해 체인을 호출
- `astream_log` : 최종 응답뿐만 아니라 발생하는 중간 단계를 스트리밍

앞서 [LangChain & LLM 사용하기](https://kangspa.github.io/Project/LangChain/post-03.html) 포스팅에서 진행했듯이 진행해주면 된다.

`batch`의 경우, 아래와 같이 여러 개의 딕셔너리를 포함하는 리스트를 인자로 받아, 각 딕셔너리 값을 프롬프트에서 선언해둔 키 값으로 사용하여 일괄 처리를 수행한다.
이 때 `max_concurrency` 값을 선언하여 최대 선언 작업 수를 제한할 수 있다.

```python
chain.batch(
    [
        {"question": "저는 식당에 가서 음식을 주문하고 싶어요"},
        {"question": "호텔에서 숙박을 예약하고 싶어요"},
        {"question": "10대의 학생에게 파이썬에 대해 가르치고 싶어요"},
        {"question": "차량에 주유를 하고 싶어요"},
        {"question": "엔비디아 주식에 투자하고 싶어요"},
    ],
    config={"max_concurrency": 3},
)
```

이러한 일련의 과정은 `Runnable` 프로토콜을 통해 체인을 좀 더 쉽게 사용하도록 구현됐다고 한다.