---
title: "LangChain & LLM 사용하기"
tag:
    - OpenAI
    - API
date: "2024-12-07"
thumbnail: "/assets/img/DATA & AI/Natural Language Processing/post-04/thumbnail.png"
---

단순히 어떤 식으로 사용하는지 등 [랭체인LangChain 노트](https://wikidocs.net/book/14314)의 'CH01' 에 있는 내용 그대로 따라하며 진행한 내용을 작성한다.

# LangChain 이용해서 Query 보내고 답변받기

다른 기능 없이, 단순히 [`ChatGPT`](https://chatgpt.com/)에서 사용하듯 질문 보내고 답변을 받는 방법은 아래와 같다.
여기서 사용되는 `model_name`의 모델은 <https://platform.openai.com/docs/models> 페이지에서 확인 가능하고, 필자는 가격을 조금이라도 아끼며 쓰기 위해 `gpt-4o-mini`를 사용하여 진행하였다.

```python
from langchain_openai import ChatOpenAI

# 객체 생성
llm = ChatOpenAI(
    temperature=0.1,  # 창의성 (0.0 ~ 2.0)
    model_name="gpt-4o-mini",  # 모델명
)

# 질의내용
question = "스리랑카의 수도는 어디인가요?"

# 질의
response = llm.invoke(question)
```
- temperature : 낮을수록 집중되고 결정론적 / 높을수록 무작위성
- max_tokens : 완성에 생성할 토큰 최대 개수
- model_name : 모델명 (참고 : <https://platform.openai.com/docs/models>)

위와 같이 전달하면 `json` 형태로 응답을 받을 수 있는데, `response.content`가 답변에 해당하는 부분이다.

```python
print(response.content)
# 스리랑카의 수도는 스리자야와르데네푸라코테입니다. 그러나 상업과 행정의 중심지인 콜롬보도 중요한 도시로 여겨집니다.
```

`response.response_metadata` 은 답변에 대한 메타데이터, 즉 정보가 담겨있는 부분이다.
그 중에서 `LogProb`, 주어진 텍스트에 대한 모델의 **토큰 확률의 로그 값**을 보고자 한다면, 아래와 같이 `ChatOpenAI`를 선언해주면 된다.

```python
# 객체 생성
llm_with_logprob = ChatOpenAI(
    temperature=0.1,  # 창의성 (0.0 ~ 2.0)
    max_tokens=2048,  # 최대 토큰수
    model_name="gpt-4o-mini",  # 모델명
).bind(logprobs=True)
```

해당 값은 `response.response_metadata['logprobs']`에서 별도로 볼 수 있으며, 각 토큰을 예측할 확률을 별도로 볼 수 있다.

# LangChain 스트리밍 출력

앞서 `ChatOpenAI`에 `invoke` 메소드를 통해 답변을 받았다면, `stream`을 이용하면 실시간으로 쿼리에 대한 답변을 받을 수 있다.

```python
answer = llm.stream("대한민국의 아름다운 관광지 10곳과 주소를 알려주세요!")

# 스트리밍 방식으로 각 토큰을 출력합니다. (실시간 출력)
for token in answer:
    print(token.content, end="", flush=True)
```

직접 확인해보면 답변을 한번에 출력하지 않고, 토큰별로 띄워주는 것을 볼 수 있다.

# MultiModal 처리

OpenAI 모델 중 `gpt-4o` 와 `gpt-4o-turbo`는 이미지 인식 기능이 추가된 모델이라고 한다.
<https://openai.com/api/pricing/> 를 보면 `gpt-4o-mini`도 `Vision pricing calculator`가 있는 것으로 보아, `gpt-4o-mini` 모델도 이미지 인식 기능이 있는 것으로 보인다.
단, 해상도에 대해 내부적으로 처리하는 알고리즘이 다른지 `gpt-4o`의 금액이 더 적게 나와서 `gpt-4o` 모델을 사용하여 진행해보았다.

```python
from langchain_teddynote.models import MultiModal
from langchain_teddynote.messages import stream_response

# 객체 생성
llm = ChatOpenAI(
    temperature=0.1,  # 창의성 (0.0 ~ 2.0)
    max_tokens=2048,  # 최대 토큰수
    model_name="gpt-4o",  # 모델명
)

# 멀티모달 객체 생성
multimodal_llm = MultiModal(llm)

# 샘플 이미지 주소(웹사이트로 부터 바로 인식)
IMAGE_URL = "https://t3.ftcdn.net/jpg/03/77/33/96/360_F_377339633_Rtv9I77sSmSNcev8bEcnVxTHrXB4nRJ5.jpg"

# 이미지 파일로 부터 질의
answer = multimodal_llm.stream(IMAGE_URL)
# 스트리밍 방식으로 각 토큰을 출력합니다. (실시간 출력)
stream_response(answer)
```

해당 모델에 프롬프트를 추가한다면, 아래와 같이 작성해주면 된다.

```python
system_prompt = """gpt에 부여하는 역할 관련 내용. 시스템 프롬프트"""

user_prompt = """사용자가 요구하는 내용. 일반적인 Query에 해당"""

# 멀티모달 객체 생성
multimodal_llm_with_prompt = MultiModal(
    llm, system_prompt=system_prompt, user_prompt=user_prompt
)
```