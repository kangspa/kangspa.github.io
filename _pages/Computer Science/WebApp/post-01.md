---
title: "Jekyll 테마 적용"
tags:
    - 시작
    - jekyll
    - satellite
date: "2024-11-15"
thumbnail: "/assets/img/Computer Science/WebApp/post-01/thumbnail.png"
---

**`jekyll-theme-satellite` 테마를 적용하여 현재 블로그를 만들었다.**
메인페이지 : [jekyll-theme-satellite](https://jekyll-themes.com/byanko55/jekyll-theme-satellite)

1. 해당 url에서 이미지와 같은 버튼 둘 중 하나를 눌러, Github 페이지로 이동한다.
![Image1](/assets/img/Computer Science/WebApp/post-01/1.png)

2. Fork를 해서 자신의 Github에 해당 레포지토리를 복사해준다.
이 때, 레포지토리 이름은 `(자신의 계정명).github.io` 로 해준다.
![Image2](/assets/img/Computer Science/WebApp/post-01/2.png)

3. Settings > Pages > Branch 에서 메인이 되는 브랜치 선택(master) 후 save 해주면 된다.
![Image3](/assets/img/Computer Science/WebApp/post-01/3.png)

일정 시간이 지난 후 `(자신의 계정명).github.io`으로 페이지가 열린다.
아무래도 변경 사항을 커밋했다고 해서 바로바로 반영이 되지 않으니 속도가 중요하다면 Gitblog는 좋지 못한 선택일 것 같다.

계정 당 하나의 페이지(~.github.io)만 호스팅 지원해주는 것 같으니, 다른 성격의 개인 페이지를 열고 싶다면 또다른 계정 사용이 필요하다.

무엇보다 서버 단에서 구동되는 언어는 지원 안해준다고 전에 봤던 것으로 기억하니, 직접 개인 페이지를 제작하고 싶다면 JS로 해야하는게 필수.

---

위와 같이 Github에서만 모든 과정을 진행하니, 자신만의 페이지로 꾸밀 때 404 에러가 발생하는 것 같다.
아래 추가 작성한 내용을 참고하여 `Readme.md`의 `Installaion`을 전부 따르는게 좋을 것 같다.

- 참고 : [Jekyll 테마 404 에러 해결](https://kangspa.github.io/Computer Science/WebApp/post-06.html)