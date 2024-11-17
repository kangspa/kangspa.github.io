---
title: "댓글 연동 및 방문자 수 확인"
tags:
    - giscus
    - goatcounter
date: "2024-11-17"
thumbnail: "https://i.ibb.co/V9j2Qsg/giscus-Wl0-X3byd-az-U68-1.webp"
---

사실상 해당 테마의 docs 파일에서 확인 가능한 `Comment System.md` 과 `Visitor Counter.md` 내용을 보고 따라했다.
간단히 상세 단계를 한글로 작성했다 정도?

---
## Giscus를 활용한 댓글 연동

해당 블로그에서 댓글은 Giscus를 활용했는데, 이는 Github 레포지토리의 discussions 내용을 각 포스팅 하위에 댓글처럼 보여주는 앱이다.
그렇기에 별도의 DB를 필요로 하지 않아서 좋다!

1. 현재 만들어둔 블로그 레포지토리(`username`.github.io)의
`Settings`→`General`→`Features` 에서 `Discussions`를 체크해준다.
![Image1](/assets/img/Project/GitBlog/post-03/1.png)

2. 현재 만들어둔 블로그 레포지토리(`username`.github.io)에 [Giscus](https://github.com/apps/giscus)를 설치해준다.
![Image2](/assets/img/Project/GitBlog/post-03/2.png)
![Image3](/assets/img/Project/GitBlog/post-03/3.png)
스크린샷 촬영한 계정은 깡통계정이라 레포지토리가 없어서 `All repositories`만 나오는 것 같은데, `username`.github.io 로 레포지토리 만들었다면 선택 가능하다.
물론 그냥 `All repositories`로 해도 지장은 없을 것 같다.

3. [Giscus Guide](https://giscus.app/ko)에 접속해서, 자신의 저장소(`username`.github.io)를 입력해준다.
지금까지 진행한 모든 단계는 사실 해당 가이드라인에 잘 나와있다.
![Image4](/assets/img/Project/GitBlog/post-03/4.png)

4. `Discussion 카테고리`를 `Q&A`로 설정해준다.
![Image5](/assets/img/Project/GitBlog/post-03/5.png)

5. 하단에 생성된 `giscus script`의 값 일부를 `_config.yml`에 복사해서 넣는다.
위에서부터 순서대로 작성해주면 된다.
![Image6](/assets/img/Project/GitBlog/post-03/6.png)
![Image7](/assets/img/Project/GitBlog/post-03/7.png)

이렇게 하면 Giscus를 활용해서 Github 블로그에 댓글 만드는 건 끝났는데, 실제로 되는지는 해당 포스팅 하단에 댓글 달고 확인해봐야 할 것 같다. → 이상없이 Discussions에 작성되는 것 확인 완료!
기본적으로 Github 레포지토리의 discussions에 의견을 남기는 형식인만큼, 댓글을 남기려면 Github에 로그인해야 가능하다.

---

## GoatCount로 방문자 수 표시

이건 워낙 간단해서..여기 같이 쓰는 것도 있다.

1. [GoatCounter 회원가입](https://www.goatcounter.com/signup)을 일단 진행한다.
![Image8](/assets/img/Project/GitBlog/post-03/8.png)
    - Code : goatcounter 대시보드에 접속할 일종의 아이디?
    - Site domain : 방문자 수 확인할 도메인 주소
    - Email address : goatcounter 가입 이메일 주소
    - Password : 8자리 이상 비밀번호
    - Fill in 9 here : 그냥 9 쓰면 됩니다.(사람 확인)

2. 가입한 이메일로 수신한 확인용 링크를 클릭하면 가입완료된다.
필자는 스팸메일함에 있는줄 모르고 왜 가입이 안되나 헤맸다.
![Image9](/assets/img/Project/GitBlog/post-03/9.png)

3. `Setting`로 이동해서 `Allow adding visitor counts on your website`를 체크해준다.
![Image10](/assets/img/Project/GitBlog/post-03/10.png)

4. 가입할 때 작성한 `Code`값을 `_config.yml`의 `goatcounter_code` 값으로 넣어준다.
![Image11](/assets/img/Project/GitBlog/post-03/11.png)

이렇게 하면 끝...
추가로 `Setting`에서 특정IP는 방문자수 체크에 무시할 수 있는데, `Add your current IP` 클릭하면 현재 접속해있는 IP값 그대로 넣을 수 있다.
블로그 운영자 IP는 방문자 수 체크에서 무시하려고 넣어둔 기능인 것 같다.
추가로 `Data Collection` 탭의 `Region`에 한국 코드가 없기에 KR만 추가해줌으로써 해당 세팅은 끝냈다.

아마 각 포스팅별 조회수를 보여주기 위한 연동 시스템인 것 같다.
![Image12](/assets/img/Project/GitBlog/post-03/12.png)