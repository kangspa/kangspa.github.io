---
title: "프롬프트"
tag:
    - Prompt
    - RAG
    - Fewshot
date: "2024-12-07"
thumbnail: "/assets/img/DATA & AI/Natural Language Processing/post-07/thumbnail.png"
---

**'프롬프트'**는 기본적으로 ***언어 모델에 사용할 질문이나 명령을 생성하는 과정***이다.
프롬프트 단계를 통해, LLM이 조금 더 답변을 잘 하도록 만들 수 있다.

# PromptTemplate

앞서 계속 진행했듯이, `LangChain`에서는 `PromptTemplate`을 통해 프롬프트를 입력 가능하다.

```python
from langchain_core.prompts import PromptTemplate

# template 정의. {country}는 변수로, 이후에 값이 들어갈 자리를 의미
template = "{country}의 수도는 어디인가요?"

# from_template 메소드를 이용하여 PromptTemplate 객체 생성
prompt = PromptTemplate.from_template(template)
prompt
```

아래와 같이 여러 인자 값을 프롬프트로 만들어두고, 추후 하나만 받거나 특정 인자의 default 값을 변경하는 것도 가능하다.

```python
# template 정의
template = "{country1}과 {country2}의 수도는 각각 어디인가요?"

# PromptTemplate 객체를 활용하여 prompt_template 생성
prompt = PromptTemplate(
    template=template,
    input_variables=["country1"],
    partial_variables={
        "country2": "미국"  # dictionary 형태로 partial_variables를 전달
    },
)

# 1개 인자만 전달하기
prompt.format(country1="대한민국")

# country2 인자 변경하기
prompt_partial = prompt.partial(country2="캐나다")
```

위와 같이 `partial`를 쓰는 경우는, 함수를 부분적으로 사용하는 경우라고 한다. 대표적으로 **날짜나 시간**은 가변적인만큼, 아래와 같이 미리 선언해두고 프롬프트 값으로 넣어두는 것이다.

```python
from datetime import datetime

# 날짜를 반환하는 함수 정의
def get_today():
    return datetime.now().strftime("%B %d")

prompt = PromptTemplate(
    template="오늘의 날짜는 {today} 입니다. 오늘이 생일인 유명인 {n}명을 나열해 주세요. 생년월일을 표기해주세요.",
    input_variables=["n"],
    partial_variables={
        "today": get_today  # dictionary 형태로 partial_variables를 전달
    },
)
```

# ChatPromptTemplate & MessagePlaceholder

대화 목록을 프롬프트로 주입하는 `ChatPromptTemplate`이나, 랜더링 메시지를 제어하기 위한 `MessagePlaceholder`를 사용할 수도 있다.

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "당신은 요약 전문 AI 어시스턴트입니다. 당신의 임무는 주요 키워드로 대화를 요약하는 것입니다.",
        ),
        MessagesPlaceholder(variable_name="conversation"),
        ("human", "지금까지의 대화를 {word_count} 단어로 요약합니다."),
    ]
)

formatted_chat_prompt = chat_prompt.format(
    word_count=5,
    conversation=[
        ("human", "안녕하세요! 저는 오늘 새로 입사한 테디 입니다. 만나서 반갑습니다."),
        ("ai", "반가워요! 앞으로 잘 부탁 드립니다."),
    ],
)

print(formatted_chat_prompt)
```

# FewShotPromptTemplate

약간의 예시를 줌으로써, 답변을 구체화 시키는 방식이다.
`Fewshot`뿐만 아니라, `Zeroshot`, `Oneshot` 프롬프트 방식도 있는데, 각각 예시를 얼마나 제공하느냐에 따라 구분된다.
- `Zeroshot` : 예시를 하나도 제공하지 않음
- `Oneshot` : 하나의 예시만 제공
- `Fewshot` : 2~5개의 예시를 제공

```python
from langchain_core.prompts.few_shot import FewShotPromptTemplate

examples = [
    {
        "question": "스티브 잡스와 아인슈타인 중 누가 더 오래 살았나요?",
        "answer": """이 질문에 추가 질문이 필요한가요: 예.
추가 질문: 스티브 잡스는 몇 살에 사망했나요?
중간 답변: 스티브 잡스는 56세에 사망했습니다.
추가 질문: 아인슈타인은 몇 살에 사망했나요?
중간 답변: 아인슈타인은 76세에 사망했습니다.
최종 답변은: 아인슈타인
""",
    },
    {
        "question": "네이버의 창립자는 언제 태어났나요?",
        "answer": """이 질문에 추가 질문이 필요한가요: 예.
추가 질문: 네이버의 창립자는 누구인가요?
중간 답변: 네이버는 이해진에 의해 창립되었습니다.
추가 질문: 이해진은 언제 태어났나요?
중간 답변: 이해진은 1967년 6월 22일에 태어났습니다.
최종 답변은: 1967년 6월 22일
""",
    },
    {
        "question": "율곡 이이의 어머니가 태어난 해의 통치하던 왕은 누구인가요?",
        "answer": """이 질문에 추가 질문이 필요한가요: 예.
추가 질문: 율곡 이이의 어머니는 누구인가요?
중간 답변: 율곡 이이의 어머니는 신사임당입니다.
추가 질문: 신사임당은 언제 태어났나요?
중간 답변: 신사임당은 1504년에 태어났습니다.
추가 질문: 1504년에 조선을 통치한 왕은 누구인가요?
중간 답변: 1504년에 조선을 통치한 왕은 연산군입니다.
최종 답변은: 연산군
""",
    },
    {
        "question": "올드보이와 기생충의 감독이 같은 나라 출신인가요?",
        "answer": """이 질문에 추가 질문이 필요한가요: 예.
추가 질문: 올드보이의 감독은 누구인가요?
중간 답변: 올드보이의 감독은 박찬욱입니다.
추가 질문: 박찬욱은 어느 나라 출신인가요?
중간 답변: 박찬욱은 대한민국 출신입니다.
추가 질문: 기생충의 감독은 누구인가요?
중간 답변: 기생충의 감독은 봉준호입니다.
추가 질문: 봉준호는 어느 나라 출신인가요?
중간 답변: 봉준호는 대한민국 출신입니다.
최종 답변은: 예
""",
    },
]

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question:\n{question}\nAnswer:",
    input_variables=["question"],
)

question = "Google이 창립된 연도에 Bill Gates의 나이는 몇 살인가요?"
final_prompt = prompt.format(question=question)
print(final_prompt)

# 출력
'''
Question:
스티브 잡스와 아인슈타인 중 누가 더 오래 살았나요?
Answer:
이 질문에 추가 질문이 필요한가요: 예.
추가 질문: 스티브 잡스는 몇 살에 사망했나요?
중간 답변: 스티브 잡스는 56세에 사망했습니다.
추가 질문: 아인슈타인은 몇 살에 사망했나요?
중간 답변: 아인슈타인은 76세에 사망했습니다.
최종 답변은: 아인슈타인


Question:
네이버의 창립자는 언제 태어났나요?
Answer:
이 질문에 추가 질문이 필요한가요: 예.
추가 질문: 네이버의 창립자는 누구인가요?
중간 답변: 네이버는 이해진에 의해 창립되었습니다.
추가 질문: 이해진은 언제 태어났나요?
중간 답변: 이해진은 1967년 6월 22일에 태어났습니다.
최종 답변은: 1967년 6월 22일


Question:
율곡 이이의 어머니가 태어난 해의 통치하던 왕은 누구인가요?
Answer:
이 질문에 추가 질문이 필요한가요: 예.
추가 질문: 율곡 이이의 어머니는 누구인가요?
중간 답변: 율곡 이이의 어머니는 신사임당입니다.
추가 질문: 신사임당은 언제 태어났나요?
중간 답변: 신사임당은 1504년에 태어났습니다.
추가 질문: 1504년에 조선을 통치한 왕은 누구인가요?
중간 답변: 1504년에 조선을 통치한 왕은 연산군입니다.
최종 답변은: 연산군


Question:
올드보이와 기생충의 감독이 같은 나라 출신인가요?
Answer:
이 질문에 추가 질문이 필요한가요: 예.
추가 질문: 올드보이의 감독은 누구인가요?
중간 답변: 올드보이의 감독은 박찬욱입니다.
추가 질문: 박찬욱은 어느 나라 출신인가요?
중간 답변: 박찬욱은 대한민국 출신입니다.
추가 질문: 기생충의 감독은 누구인가요?
중간 답변: 기생충의 감독은 봉준호입니다.
추가 질문: 봉준호는 어느 나라 출신인가요?
중간 답변: 봉준호는 대한민국 출신입니다.
최종 답변은: 예


Question:
Google이 창립된 연도에 Bill Gates의 나이는 몇 살인가요?
Answer:
'''
```

## Example Selector

예제가 많을 경우, 프롬프트로 보낼 예제를 유사도 측정을 통해 제한할 수 있다.
이를 위해 본 교재에서는 `Chroma` DB를 사용하고 있다.

```python
from langchain_core.example_selectors import (
    MaxMarginalRelevanceExampleSelector,
    SemanticSimilarityExampleSelector,
)
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Vector DB 생성 (저장소 이름, 임베딩 클래스)
chroma = Chroma("example_selector", OpenAIEmbeddings())

example_selector = SemanticSimilarityExampleSelector.from_examples(
    # 여기에는 선택 가능한 예시 목록이 있습니다.
    examples,
    # 여기에는 의미적 유사성을 측정하는 데 사용되는 임베딩을 생성하는 임베딩 클래스가 있습니다.
    OpenAIEmbeddings(),
    # 여기에는 임베딩을 저장하고 유사성 검색을 수행하는 데 사용되는 VectorStore 클래스가 있습니다.
    Chroma,
    # 이것은 생성할 예시의 수입니다.
    k=1,
)

prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    suffix="Question:\n{question}\nAnswer:",
    input_variables=["question"],
)

question = "Google이 창립된 연도에 Bill Gates의 나이는 몇 살인가요?"
example_selector_prompt = prompt.format(question=question)
print(example_selector_prompt)
```

## FewShotChatMessagePromptTemplate

퓨샷 프롬프트를 하며, `ChatPromptTemplate`을 사용하기 위해 `FewShotChatMessagePromptTemplate` 있다고 한다.

```python
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_core.example_selectors import (
    SemanticSimilarityExampleSelector,
)
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

chroma = Chroma("fewshot_chat", OpenAIEmbeddings())

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{instruction}:\n{input}"),
        ("ai", "{answer}"),
    ]
)

example_selector = SemanticSimilarityExampleSelector.from_examples(
    # 여기에는 선택 가능한 예시 목록이 있습니다.
    examples,
    # 여기에는 의미적 유사성을 측정하는 데 사용되는 임베딩을 생성하는 임베딩 클래스가 있습니다.
    OpenAIEmbeddings(),
    # 여기에는 임베딩을 저장하고 유사성 검색을 수행하는 데 사용되는 VectorStore 클래스가 있습니다.
    chroma,
    # 이것은 생성할 예시의 수입니다.
    k=1,
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
)
```

# LangChain Hub

위와 같이 직접 모든 프롬프트를 작성할 수도 있지만, 다른 사람이 만들어둔 프롬프트를 [LangChain Hub](https://smith.langchain.com/hub)에서 불러와서 사용할 수도 있다.
- repo 아이디 값 : 해당 프롬프트의 최신 버전
- commit id 추가 : 해당 프롬프트의 특정 버전

```python
from langchain import hub

# 가장 최신 버전의 프롬프트를 가져옵니다.
prompt = hub.pull("rlm/rag-prompt")

# 특정 버전의 프롬프트를 가져오려면 버전 해시를 지정하세요
prompt = hub.pull("rlm/rag-prompt:50442af1")
```

`hub.push`를 통해 자신의 프롬프트를 허브에 업로드 할 수도 있다고 한다.