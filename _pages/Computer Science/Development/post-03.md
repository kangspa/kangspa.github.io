---
title: "poetry 사용방법"
tag:
    - 가상환경
    - env
    - poetry
date: "2024-12-06"
thumbnail: "/assets/img/Computer Science/Development/post-03/thumbnail.png"
---

[랭체인LangChain 노트](https://wikidocs.net/book/14314) 실습 시작을 위해 [테디노트님의 랭체인 깃허브](https://github.com/teddylee777/langchain-kr)에서 레포지토리를 fork 하고 설치하려고 보면, `poetry`로 가상환경을 구성하는 것을 볼 수 있다.

원래 `miniconda`를 활용하여 가상환경 구성을 해오던 필자에게, `poetry`는 익숙치 않은 방법이었다. 다행히 기업 면접 전 과제로 한번 접하게 되며 공부한 적 있어, 당시 참고했던 블로그 글과 경험을 살려 프로젝트 시작 전 `poetry`에 대해 정리해본다.

# 그래서 poetry가 무엇인가?

파이썬은 많은 라이브러리를 다루고, 각각의 버전에 맞춰 진행 가능한 프로젝트가 달라지는 경우가 많다. 매번 라이브러리 버전을 맞추기 위해 삭제하고, 설치하고 하다보면 불편하기도 하고 서로 충돌을 일으킬 수도 있어 이를 편하게 다루기 위해 가상환경을 구축하고 해당 환경별로 프로젝트를 진행하는 경우가 대부분이다.

이를 위해 앞서 말했듯 `conda`환경을 많이 사용했는데, 사용해본 사람들을 알겠지만 `anaconda`환경은 굉장히 무겁다...그래서 `miniconda`가 나와줬지만, 그래도 별도의 설치를 요구하고 기본 라이브러리를 전부 설치해준단 점에서 `venv`를 사용하는 것보다 무겁긴하다.

`venv`는 파이썬에서 기본으로 내장된 모듈이라 별도의 설치없이 활용 가능하다. 이를 좀 더 사용하기 편하게, 그리고 **의존성 관리**를 효율적으로 하기위해 만들어진 모듈이 `poetry`이다.

### poetry 특징 : 의존성 해결과 잠금

방금 말했듯이, 의존성 관리를 효율적으로 하기 좋은 모듈이다. poetry를 사용하게 되면 `pyproject.toml` 과 `poetry.lock` 파일을 접하게 되는데, 이 파일들을 통해 특정 라이브러리의 버전 관련 정보를 확인하고, 설치해준다.
즉, `pip`을 통해 설치하는 것과 달리 최신 버전으로 설치를 진행하려해도 해당 버전이 `pyproject.toml` 과 `poetry.lock` 에서 명시되어 있지 않다면 진행되지 않는 것이다.

다른 장점도 많지만, 특별히 `poetry`만의 장점이자 특징이라 하면 이게 크지 않을까 싶다. 사실 사용 경험 자체가 적다보니 다른 장점은 크게 체감을 못했다...

## poetry 설치

- 참고
    - <https://python-poetry.org/docs/#installing-with-the-official-installer>
    - [[Python] 윈도우에서 poetry 설치하기](https://velog.io/@pikamon/Python-4)

설치 시에는 위 2개 링크를 참고하며 진행했었다. 하나는 공식 문서고, 아래 블로그 글은 공식 문서의 경로를 넣어서 진행이 안되서 찾게 된 글이었다.
지금 참고 링크 들어가보면 pipx 설치 방법이 있고, 검색해보니 `pip install poetry` 도 지원하는 듯하니 굳이 이렇게 할 필요가 없을 것도 같다.
실제로 테디노트님이 환경설정 올려두신 걸 보면 `pip3 install poetry`로 진행하고 있다.

1. `powershell`에서 하단 커맨드를 진행해준다.
    ```shell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```
2. poetry의 `PATH` 설정을 해준다.
    **환경 변수** 설정을 들어가서, `사용자 환경 변수` 에 `%APPDATA%\Python\Scripts` 를 추가해준다.
    ![Image1](/assets/img/Computer Science/Development/post-03/1.png)

3. 이후 `powershell` 종료 후 다시 열면, `poetry --version`으로 버전이 나오는 것을 볼 수 있다.
    필자는 이 때부터 커맨드 터미널에서도 `poetry` 명령어 사용이 가능했던 것으로 기억한다.

# poetry 시작

사실 [랭체인LangChain 노트](https://wikidocs.net/book/14314) 실습을 위해서라면, 테디노트님 레포지토리에 `pyproject.toml`이 명시되어 있는만큼 바로 `poetry shell`로 가상환경 활성화, `poetry update`로 패키지 일괄 업데이트를 진행해주면 된다.

다만, 본 포스팅은 `poetry`를 어떻게 다룰지 간단히작성 중인 글인만큼 당시 어떻게 환경을 구성해나갔는지 간단히만 작성한다.

1. 프로젝트 진행하고자 하는 위치에서 `poetry init` 명령어를 진행해준다.
    필자는 **VSCode**에서 터미널 열고 진행하다보니 기본적으로 프로젝트 환경이라서 바로 이렇게 진행했는데, 사용자에 따라 새로 프로젝트부터 만들어야하는 경우도 있을 것이다.
    이 경우에는 `poetry new <project name>` 를 작성하면 해당 프로젝트명으로 폴더가 만들어지고, 아래와 같이 디렉토리가 자동 구성된다고 한다.
    ```
    my_project
    ├── pyproject.toml
    ├── README.md
    ├── my_project
    │   └── __init__.py
    └── tests
        └── __init__.py
    ```

2. `poetry add <package_name>`을 통해 해당 가상환경에서 사용할 패키지들을 추가해준다.
    이러면 자동으로 `pyproject.toml`에 해당 패키지가 `<package_name> = "^<version>"` 식으로 추가된다.
    즉, 해당 가상환경은 명시된 `<version>` 이상을 사용한다는 것이다.

3. 필요에 따라 `poetry remove <package_name>`로 명시된 패키지를 삭제할 수 있다.

필자는 이 정도만 사용해서 원하는 환경 구축을 하고, `poetry shell`로 해당 환경을 사용하였다.
알아보면 더욱 많은 기능들이 있다는 것을 알 수 있었기에, `린팅 추가` 및 `Pypi 배포`를 추가로 알아보려면 [python - poetry 설치부터 project initializing, 활용하기](https://velog.io/@qlgks1/python-poetry-설치부터-project-initializing-활용하기) 글을 보는 것도 좋을 것 같다.

---

- 참고 및 출처
    - <https://python-poetry.org/docs/#installing-with-the-official-installer>
    - [[Python] 윈도우에서 poetry 설치하기](https://velog.io/@pikamon/Python-4)
    - [python - poetry 설치부터 project initializing, 활용하기](https://velog.io/@qlgks1/python-poetry-설치부터-project-initializing-활용하기)
    - [[가상환경 관리] poetry 사용법 정리](https://velog.io/@eenzeenee/poetry-사용법-정리)
    - [Python env와 Poetry를 이용한 가상환경 버전 관리](https://modulabs.co.kr/blog/python-env-poetry)