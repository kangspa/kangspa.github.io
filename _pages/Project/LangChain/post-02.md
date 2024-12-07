---
title: "LangChain 시작 전 준비"
tag:
    - OpenAI
    - LangSmith
    - API
date: "2024-12-07"
thumbnail: "/assets/img/Project/LangChain/post-02/thumbnail.png"
---

`LangChain`은 LLM 모델에 여러 기능 추가를 좀 더 쉽게 해줄 수 있게 만들어주는 프레임워크이다.
즉 기본이 되는 LLM 모델을 사용해야하는데, 별도로 로컬 모델을 사용하는게 아니라면 OpenAI의 `ChatGPT` 같은 모델을 불러와서 사용해야한다.

# OpenAI 결제 수단 등록 및 Credit 추가

[`ChatGPT`](https://chatgpt.com/) 로 접속하는게 아니라, [`OpenAI`](https://platform.openai.com/) 사이트로 접속하면 회원가입 후 로그인하여 API 키를 발급받을 수 있다.

![Image1](/assets/img/Project/LangChain/post-02/1.png)
1. 로그인까지 끝냈다면, 좌측 위의 '톱니바퀴'를 눌러 페이지를 이동한다.
2. 좌측에서 'Billing' 페이지로 이동해준다.
3. 'Payment method'를 클릭하여 결제 수단을 등록해준다.
4. 'Add to credit balance'를 클릭하여 API 사용할 비용을 미리 결제해둔다.

당연하지만 달러로 환산되어 나가는만큼, 많이 사용하게 될 사람은 환율 보고 유리할 때 잘 결제해주면 조금이라도 금액을 아낄 수 있을 것이다.
필자는 어차피 실습 용도로 결제하는만큼 "$10" 만 우선 결제하고 진행하였다.

# OpenAI 결제 한도 정하기

결제 수단 등록이 끝났다면 진행에 문제는 없으나, 서비스가 아니라 실습 용도라면, 그리고 본인 지갑 사정을 생각한다면 Limit을 정해주는게 좋을 것이다.

![Image2](/assets/img/Project/LangChain/post-02/2.png)
1. 'Limits' 페이지로 이동해준다.
2. 'Set a Budget Alert' 금액을 설정하여, 현재 사용 금액이 얼마가 되었을 때 메일로 알림을 줄 것인지 설정해준다.
3. 'Enable Budget Limit' 금액을 설정하여, 현재 사용 금액이 얼마가 되었을 때 API 요청이 거부되도록 할 것인지 설정해준다.

`Caution`이 적혀있듯이, 'Enable Budget Limit' 금액을 설정해두면 서비스 이용에 제한이 될 수 있으므로, 주의하라고 되어있다.
말했듯이 실습 용도라면 무시하고 자신의 지갑 사정 생각해서 설정해두면 된다.

해당 설정은 'Organization', 즉 단체별 설정이었는데, 'Project'별로도 API 키를 발급받고 'Limits' 설정이 가능하다.
필자의 경우 혹시 몰라서 'Project'의 'Limits'도 위와 같이 설정을 완료해뒀다.

# OpenAI API 키 발급받기

설정이 끝났다면, 이제 사용하기 위한 API 키를 발급받아야합니다.

![Image3](/assets/img/Project/LangChain/post-02/3.png)
1. 'API keys' 페이지로 이동한다.
2. 'Create new secret key'를 눌러, API 키 발급을 시작한다.
![Image4](/assets/img/Project/LangChain/post-02/4.png)
3. 발급받을 키의 이름을 지정한다.
4. 해당 키를 사용할 'Project'를 지정해준다.
5. 'Create secret key'를 통해 API 키 발급을 받는다.
    해당 API 키는 복사한 후, 외부 유출에 주의하며 보관할 수 있도록 주의한다.
    간단히 [테디노트님의 랭체인 깃허브](https://github.com/teddylee777/langchain-kr)를 로컬에 clone 해뒀다면, `.env`에 해당 키를 `OPENAI_API_KEY` 로 저장해두면 된다.

필요에 따라 해당 키에 권한을 얼마나 부여할지도 지정할 수 있다.
실습 진행에 있어 어떤 모델을 어떤 용도로 쓰게 될지 모르니 제한하지 않지만, 상황에 따라 유동적으로 지정해서 쓰면 될 것 같다.

# LangSmith 추적 설정

LangSmith는 LLM 애플레이션 개발에 있어 다양한 추적 기능을 제공해준다.
간단히 얼마만큼의 토큰을 사용했는지, 어떤 에러가 발생했는지 등을 확인하게 도와준다고 생각하면 좋다.
[`LangSmith`](https://smith.langchain.com/) 사이트에 접속하여 회원가입 후 이메일 인증을 우선 진행해줘야 한다.

![Image5](/assets/img/Project/LangChain/post-02/5.png)
인증까지 끝나면, 좌측 배너에서 톱니바퀴를 눌러 개인 페이지로 이동해준다.

![Image6](/assets/img/Project/LangChain/post-02/6.png)
가운데에서 'Personal' 클릭 후, 좌측 위의 'Create API Key'를 통해 개인 키를 발급받으면 된다.

OpenAI API 키 발급받을 때처럼, 해당 키도 복사 후 `.env`에 저장해주면 된다.
단, 저장 시에는 [해당 내용](https://wikidocs.net/250954)을 참고하여, `LANGCHAIN_TRACING_V2`, `LANGCHAIN_ENDPOINT`, `LANGCHAIN_API_KEY`, `LANGCHAIN_PROJECT` 변수를 다 입력해준다. 이후에는 아래와 같이 `.env` 내용을 불러오기만 하면, 환경 변수 설정이 되며 추적이 활성화된다고 한다.

```python
from dotenv import load_dotenv

load_dotenv()
```

## langchain-teddynote 로 LangSmith 간단 설정

해당 교재 저자가 일련의 과정을 편하게 하기 위해, `LANGCHAIN_API_KEY`만 저장해두면 추적 활성화를 쉽게 하기 위한 패키지를 만들어서 배포하고 있다고 한다.
`pip install langchain-teddynote`를 통해 패키지 설치 후, 아래 코드를 진행하면 된다고 한다.

```python
from langchain_teddynote import logging

# 프로젝트 이름을 입력합니다.
logging.langsmith("원하는 프로젝트명")
```

앞서 일련의 변수들을 전부 저장하고 관리하기 어렵다면 해당 패키지를 사용하는 것도 좋을 것이다.