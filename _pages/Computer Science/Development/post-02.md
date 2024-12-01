---
title: Github에서 이슈 발생 시 pull request 과정
tags:
    - Git
    - 이슈 처리
    - pull&request
date: "2024-12-01"
---

1. 새로운 Issue 생성
    이슈 내에서 각 Task 생성 가능
2. 각 Task에 대해 Open convert to issue 로 새로운 Issue 생성 가능
3. 해당 이슈 해결 
    - 로컬 레포지토리에서 clone or pull 을 해서 수정해준다.
4. 새로운 브랜치 생성 후, 각 이슈번호를 기재해서 커밋해주고, push해준다.
5. PR 생성하기
    - Compare & pull request 버튼이 레포지토리 메인에 있을텐데, 해당 버튼을 눌러서 진행해준다.
    - 만약 없을 경우, 직접 pull & request 버튼을 찾아서 브랜치 설정 후 진행 가능하다.
    - PR 도중 우측 상단에 Issue와 연동가능한 버튼을 눌러주고, 진행하면 자동으로 이슈는 닫히고 해결된 상태로 뜬다.

---

- 출처
  - <https://minny27.tistory.com/50>
  - <https://velog.io/@pgmjun/Github-협업-이것만은-알자-Issue-PR>