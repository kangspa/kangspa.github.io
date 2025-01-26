---
title: "Runnable"
tag:
    - LangChain
    - LCEL
    - Runnable
date: "2024-12-07"
thumbnail: "/assets/img/DATA & AI/Natural Language Processing/post-06/thumbnail.png"
---

`LCEL`을 `Runnable` 프로토콜을 통해 좀 더 쉽게 사용하도록 구현했다고 하는데, 어떤 `Runnable`이 있는지 알아보자.

# RunnablePassthrough

입력을 변경하지 않거나, 키를 더해서 그대로 전달한다.

```python
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough

runnable_chain = {"num": RunnablePassthrough()} | PromptTemplate.from_template("{num} 의 10배는?") | ChatOpenAI(model="gpt-4o-mini")

# dict 값이 RunnablePassthrough() 로 변경되었습니다.
runnable_chain.invoke(10)
```

입력값에 맞춰 `dict` 구조로 전달해야하지만, 전달하는 값이 1개라면 위와 같이 값만 전달하는 것도 가능하다.
`RunnablePassthrough.assign()` 을 사용하면, 전달된 인수 외에 `.assign()`에 선언된 값을 추가로 전달할 수 있다.

```python
# 입력 키: num, 할당(assign) 키: new_num
(RunnablePassthrough.assign(new_num=lambda x: x["num"] * 3)).invoke({"num": 1})
```
- **{'num': 1, 'new_num': 3}**

# RunnableParallel

여러 `Runnable` 인스턴스를 병렬로 실행하게 할 수 있으며, `Runnable` 뿐만 아니라 `chain`도 병렬로 실행할 수 있게 도와준다.

### Runnable 병렬

```python
from langchain_core.runnables import RunnableParallel

# RunnableParallel 인스턴스를 생성합니다. 이 인스턴스는 여러 Runnable 인스턴스를 병렬로 실행할 수 있습니다.
runnable = RunnableParallel(
    # RunnablePassthrough 인스턴스를 'passed' 키워드 인자로 전달합니다. 이는 입력된 데이터를 그대로 통과시키는 역할을 합니다.
    passed=RunnablePassthrough(),
    # 'extra' 키워드 인자로 RunnablePassthrough.assign을 사용하여, 'mult' 람다 함수를 할당합니다. 이 함수는 입력된 딕셔너리의 'num' 키에 해당하는 값을 3배로 증가시킵니다.
    extra=RunnablePassthrough.assign(mult=lambda x: x["num"] * 3),
    # 'modified' 키워드 인자로 람다 함수를 전달합니다. 이 함수는 입력된 딕셔너리의 'num' 키에 해당하는 값에 1을 더합니다.
    modified=lambda x: x["num"] + 1,
)

# runnable 인스턴스에 {'num': 1} 딕셔너리를 입력으로 전달하여 invoke 메소드를 호출합니다.
runnable.invoke({"num": 1})
```

### Chain 병렬

```python
chain1 = (
    {"country": RunnablePassthrough()}
    | PromptTemplate.from_template("{country} 의 수도는?")
    | ChatOpenAI(model="gpt-4o-mini")
)
chain2 = (
    {"country": RunnablePassthrough()}
    | PromptTemplate.from_template("{country} 의 면적은?")
    | ChatOpenAI(model="gpt-4o-mini")
)
combined_chain = RunnableParallel(capital=chain1, area=chain2)
combined_chain.invoke("대한민국")
```

# RunnableLambda

'Lambda' 에서 추측할 수 있듯이, 사용자 정의 함수를 맵핑 가능하다.

```python
def get_today(a):
    # 오늘 날짜를 가져오기
    return datetime.today().strftime("%b-%d")

# prompt 와 llm 을 생성합니다.
prompt = PromptTemplate.from_template(
    "{today} 가 생일인 유명인 {n} 명을 나열하세요. 생년월일을 표기해 주세요."
)
llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

# chain 을 생성합니다.
chain = (
    {"today": RunnableLambda(get_today), "n": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
```