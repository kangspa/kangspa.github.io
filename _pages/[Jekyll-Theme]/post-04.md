---
title: "좌측 하단의 Contact 아이콘 및 링크 수정"
tags:
    - jekyll
    - satellite
date: "2024-11-17"
thumbnail: "/assets/img/Jekyll-Theme/post-04/thumbnail.png"
---

썸네일에서 볼 수 있는 해당 테마 좌측 하단의 아이콘은, 제작자가 사용자에게 연락할 수 있는 링크를 달아둔 곳이다.
기본은 `Github`, `Email`, `Twitter`, `Instagram`, `Facebook`, `LinkedIn` 로, 연결 주소만 간단히 바꾼다면 `_config.yml`에서 `유저명`만 수정해주면 된다.
![Image1](/assets/img/Jekyll-Theme/post-04/1.png)

하지만 필자는 SNS를 기본적으로 안 하기도 하고, 그나마 있는 계정도 개인 일상 등을 올리기보다 덕질용으로 사용하다보니, 이 부분을 바꿀 필요가 있었다.
애초에 해당 블로그를 만든 이유가 단순 블로그 포스팅보다 학습 내용 정리를 위한 블로그이다보니, 추후 제작할 포트폴리오 페이지와 연결을 위해 미리 시도해보았다.

- 참고로 단순히 보여주지 않는게 목적이라면 `_config.yml` 에서 해당 값을 비워두기만 해도 된다.
![Image2](/assets/img/Jekyll-Theme/post-04/2.png)

가장 먼저 시도한 것은 티스토리 블로그 링크를 해당 위치에 띄우는 것이다.
관련 코드는 `_includes/sidebar.html`에 있으며, 다른거 필요없이 링크만 변경하는게 목적이라면 변경하려는 태그의 href 속성만 변경해주면 된다.
![Image3](/assets/img/Jekyll-Theme/post-04/3.png)

이미지의 href 부분을 `www.naver.com` 변경하고, `_config.yml`의 `twitter_username`을 아무 값이나 입력해둔다면,
좌측 하단의 트위터 이미지를 클릭 시 네이버로 연결되는 것을 볼 수 있다.

이제 아이콘을 변경해줄 차례.
아이콘은 svg 태그를 수정해주면 되는데, 티스토리 블로그 링크를 연동할 생각이기에 티스토리 svg 아이콘이 필요했다.
애초부터 img 태그로 png 아이콘을 넣어도 되겠지만, 색상 등을 일치시키기 위해 다른 블로거가 업로드 해둔 svg 아이콘을 사용하였다.

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 408.4 408.4"><g><circle class="cls-1" cx="58.18" cy="58.18" r="58.18"/><circle class="cls-1" cx="204.2" cy="58.18" r="58.18"/><circle class="cls-1" cx="204.2" cy="204.2" r="58.18"/><circle class="cls-1" cx="204.2" cy="350.22" r="58.18"/><circle class="cls-1" cx="350.22" cy="58.18" r="58.18"/></g></svg>
```
- 출처 : [https://marshall-ku.tistory.com/203](https://marshall-ku.tistory.com/203)

사실 이미지 적용하고 href 변경해서 링크 바꿨으면 이제 끝났긴하다.
다만 필자는 기본틀을 최대한 해치지 않는 선에서 진행하고 싶기도 했고, 변수명?이 아직 twitter인 점도 불편하기도 하여 아예 아래와 같이 전부 바꿨다.

```html
{% if site.tistory_username %}
    <li><a aria-label="My Tistory" href="https://{{ site.tistory_username }}.tistory.com/">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 408.4 408.4"><g><circle class="cls-1" cx="58.18" cy="58.18" r="58.18"/><circle class="cls-1" cx="204.2" cy="58.18" r="58.18"/><circle class="cls-1" cx="204.2" cy="204.2" r="58.18"/><circle class="cls-1" cx="204.2" cy="350.22" r="58.18"/><circle class="cls-1" cx="350.22" cy="58.18" r="58.18"/></g></svg>
    </a></li>
{% endif %}
```

이렇게 바꿀 경우, `_config.yml`에서 `twitter_username` 이름을 `tistory_username` 으로 바꿔주면되고, 해당 값으로 티스토리 사용자명을 입력해주면 된다.
![Image4](/assets/img/Jekyll-Theme/post-04/4.png)

마지막으로 아이콘 순서까지만 변경하고 마쳤는데, 현재는 해당 블로그는
`Github`, `LinkedIn`, `Instagram`, `Facebook`, `Tistory`, `Email`
순서이다. 방법은 그냥 `.contact-list`의 자식 요소를 위아래로 바꿔주면 끝.
![Image5](/assets/img/Jekyll-Theme/post-04/5.png)

참고로 티스토리 블로그는 여기와 다르게 개인 취미 생활 내용이나 스터디 내용이라도 일기 형식으로 상대적으로 간단한 내용들을 작성할 예정이다.