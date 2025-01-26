---
title: "출력파서"
tag:
    - parser
    - LangChain
date: "2024-12-08"
thumbnail: "/assets/img/DATA & AI/Natural Language Processing/post-08/thumbnail.png"
---

출력 파서는, LangChain에서 언어 모델(LLM)이 출력한 내용을 구조화된 형태로 변환하는 컴포넌트이다.
원하는 형식으로 구조화할 수 있다는 점에서 유용하다.

# PydanticOutputParser

사용자가 필요로 하는 정보를 명확하고 체계적인 형태로 제공하기 위해 사용 가능한 출력 파서이다.
`PydanticOutputParser`를 포함한 대부분의 `OutputParser` 는 아래와 같은 2가지 핵심 메서드가 구현되어야 한다.
- `get_format_instructions()` : 언어 모델이 출력해야할 정보의 형식을 정의하는 지침(instruction).
    이 때 설정하는 지침에 따라 언어 모델은 출력을 구조화하고, 특정 데이터 모델에 맞게 변환할 수 있다.
- `parse()` : 언어 모델의 출력을 특정 구조로 분석하고 변환하는 메서드.

예를 들어, 메일을 입력한다고 했을 때, 다음과 같이 출력을 요구하도록 정의할 수 있는 것이다.

```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from itertools import chain
from langchain_core.prompts import PromptTemplate

class EmailSummary(BaseModel):
    person: str = Field(description="메일을 보낸 사람")
    email: str = Field(description="메일을 보낸 사람의 이메일 주소")
    subject: str = Field(description="메일 제목")
    summary: str = Field(description="메일 본문을 요약한 텍스트")
    date: str = Field(description="메일 본문에 언급된 미팅 날짜와 시간")

# PydanticOutputParser 생성
parser = PydanticOutputParser(pydantic_object=EmailSummary)

prompt = PromptTemplate.from_template(
"""
You are a helpful assistant. Please answer the following questions in KOREAN.

QUESTION:
{question}

EMAIL CONVERSATION:
{email_conversation}

FORMAT:
{format}
"""
)

# format 에 PydanticOutputParser의 부분 포맷팅(partial) 추가
prompt = prompt.partial(format=parser.get_format_instructions())

llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
chain = prompt | llm
```

이러면 정의해둔 구조에 맞춰 json 형식으로 응답을 출력해주는 것을 볼 수 있다.
애초에 아래처럼 parser를 추가해서 체인을 구성할 경우, 정의해뒀던 객체 형태로 출력해준다.

```python
# 출력 파서를 추가하여 전체 체인을 재구성합니다.
chain = prompt | llm | parser

# chain 을 실행하고 결과를 출력합니다.
response = chain.invoke(
    {
        "email_conversation": email_conversation,
        "question": "이메일 내용중 주요 내용을 추출해 주세요.",
    }
)

# 결과는 EmailSummary 객체 형태로 출력됩니다.
response
```

혹은 아래처럼 `.with_structured_output()`를 모델 선언 시 붙여둔다면, 해당 파서로 결과를 출력해준다.

```python
llm_with_structered = ChatOpenAI(
    temperature=0, model_name="gpt-4o-mini"
).with_structured_output(EmailSummary)
```

# CommaSeparatedListOutputParser

'콤마 구분자 출력 파서'라고 부르는 해당 출력 파서는, 쉼표로 구분된 항목 목록을 반환할 필요가 있을 때 유용하다.

```python
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 콤마로 구분된 리스트 출력 파서 초기화
output_parser = CommaSeparatedListOutputParser()

# 출력 형식 지침 가져오기
format_instructions = output_parser.get_format_instructions()
# 프롬프트 템플릿 설정
prompt = PromptTemplate(
    # 주제에 대한 다섯 가지를 나열하라는 템플릿
    template="List five {subject}.\n{format_instructions}",
    input_variables=["subject"],  # 입력 변수로 'subject' 사용
    # 부분 변수로 형식 지침 사용
    partial_variables={"format_instructions": format_instructions},
)

# ChatOpenAI 모델 초기화
model = ChatOpenAI(temperature=0)

# 프롬프트, 모델, 출력 파서를 연결하여 체인 생성
chain = prompt | model | output_parser

# "대한민국 관광명소"에 대한 체인 호출 실행
chain.invoke({"subject": "대한민국 관광명소"})
"""
['경복궁', '인사동', '부산 해운대해수욕장', '제주도', '남산타워']
"""
```

# StructuredOutputParser

`dict` 형식으로 출력을 받고자 할 때 유용하다. 파라미터 수가 상대적으로 적은, 가벼운 모델에 사용되는 출력 파서이다.

```python
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 사용자의 질문에 대한 답변
response_schemas = [
    ResponseSchema(name="answer", description="사용자의 질문에 대한 답변"),
    ResponseSchema(
        name="source",
        description="사용자의 질문에 답하기 위해 사용된 `출처`, `웹사이트주소` 이여야 합니다.",
    ),
]
# 응답 스키마를 기반으로 한 구조화된 출력 파서 초기화
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
```
- `ResponseSchema` : 사용자 질문에 대한 답변과 사용된 소스에 대한 설명을 포함하는 응답 스키마 정의
- `StructuredOutputParser`를 `response_schemas`를 이용하여 정의된 응답 스키마에 따라 출력하도록 구조화한다.

이후 아래와 같이 사용하면 된다.

```python
# 출력 형식 지시사항을 파싱합니다.
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    # 사용자의 질문에 최대한 답변하도록 템플릿을 설정합니다.
    template="answer the users question as best as possible.\n{format_instructions}\n{question}",
    # 입력 변수로 'question'을 사용합니다.
    input_variables=["question"],
    # 부분 변수로 'format_instructions'을 사용합니다.
    partial_variables={"format_instructions": format_instructions},
)
model = ChatOpenAI(temperature=0)  # ChatOpenAI 모델 초기화
chain = prompt | model | output_parser  # 프롬프트, 모델, 출력 파서를 연결
```

# JsonOutputParser

사용자가 원하는 JSON 스키마를 지정할 수 있게 하여, 해당 스키마에 맞춰 LLM에서 데이터를 조회하여 결과를 도출해준다.
LLM이 데이터를 보다 정확하고 효율적으로 처리하기 위해서는, 파라미터 수가 충분한 무거운 모델이여야 한다.

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

# OpenAI 객체를 생성합니다.
model = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

# 원하는 데이터 구조를 정의합니다.
class Topic(BaseModel):
    description: str = Field(description="주제에 대한 간결한 설명")
    hashtags: str = Field(description="해시태그 형식의 키워드(2개 이상)")

# 질의 작성
question = "지구 온난화의 심각성 대해 알려주세요."

# 파서를 설정하고 프롬프트 템플릿에 지시사항을 주입합니다.
parser = JsonOutputParser(pydantic_object=Topic)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 친절한 AI 어시스턴트 입니다. 질문에 간결하게 답변하세요."),
        ("user", "#Format: {format_instructions}\n\n#Question: {question}"),
    ]
)
prompt = prompt.partial(format_instructions=parser.get_format_instructions())
chain = prompt | model | parser  # 체인을 구성합니다.
chain.invoke({"question": question})  # 체인을 호출하여 쿼리 실행
```

데이터 구조 정의 없이(pydantic 없이), 사용할 경우에도 json 반환하도록 요청할 수 있지만, 스키마에 대한 구체적 정보를 제공하지는 않는다.

# PandasDataFrameOutputParser

임의의 데이터프레임을 정의하면 해당 구조에 맞춰 출력해준다. (Pandas DataFrame)
아래 예제는 `gpt-4o-mini`로 진행하면 오류가 발생해서, 교재처럼 `gpt-3.5-turbo`를 사용해서 진행하였다.

```python
import pprint
from typing import Any, Dict

import pandas as pd
from langchain.output_parsers import PandasDataFrameOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# ChatOpenAI 모델 초기화 (gpt-3.5-turbo 모델 사용을 권장합니다)
model = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# 출력 목적으로만 사용됩니다.
def format_parser_output(parser_output: Dict[str, Any]) -> None:
    # 파서 출력의 키들을 순회합니다.
    for key in parser_output.keys():
        # 각 키의 값을 딕셔너리로 변환합니다.
        parser_output[key] = parser_output[key].to_dict()
    # 예쁘게 출력합니다.
    return pprint.PrettyPrinter(width=4, compact=True).pprint(parser_output)

# 원하는 Pandas DataFrame을 정의합니다.
df = pd.read_csv("./data/titanic.csv")

# 파서를 설정하고 프롬프트 템플릿에 지시사항을 주입합니다.
parser = PandasDataFrameOutputParser(dataframe=df)

# 파서의 지시사항을 출력합니다.
print(parser.get_format_instructions())

# 열 작업 예시입니다.
df_query = "Age column 을 조회해 주세요."

# 프롬프트 템플릿을 설정합니다.
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],  # 입력 변수 설정
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },  # 부분 변수 설정
)

# 체인 생성
chain = prompt | model | parser

# 체인 실행
parser_output = chain.invoke({"query": df_query})

# 출력
format_parser_output(parser_output)
```

# DatetimeOutputParser

출력을 `datetime` 형식으로 파싱하는데 사용 가능하다.
해당 시간에 대한 포맷 형식은 <https://docs.python.org/3/library/datetime.html#format-codes> 참고하면 좋다.

```python
from langchain.output_parsers import DatetimeOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# 날짜 및 시간 출력 파서
output_parser = DatetimeOutputParser()
output_parser.format = "%Y-%m-%d"

# 사용자 질문에 대한 답변 템플릿
template = """Answer the users question:\n\n#Format Instructions: \n{format_instructions}\n\n#Question: \n{question}\n\n#Answer:"""

prompt = PromptTemplate.from_template(
    template,
    partial_variables={
        "format_instructions": output_parser.get_format_instructions()
    },  # 지침을 템플릿에 적용
)

ed!# Chain 을 생성합니다.
chain = prompt | ChatOpenAI() | output_parser

# 체인을 호출하여 질문에 대한 답변을 받습니다.
output = chain.invoke({"question": "Google 이 창업한 연도는?"})
```

이외에 `EnumOutputParser` 와 `OutputFixingParser` 가 존재한다.
- `EnumOutputParser` : class로 각 속성 값 선언을 해둔 후, 특정 텍스트에 해당하는 값을 출력해주는 파서
- `OutputFixingParser` : 다른 파서와 같이 사용해서, 파싱 과정에서 발생할 수 있는 오류를 자동으로 수정하는 기능을 제공해준다.