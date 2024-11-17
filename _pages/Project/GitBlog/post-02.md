---
title: "폰트 변경하기"
tags:
    - jekyll 폰트
    - D2Coding
date: "2024-11-15"
thumbnail: "/assets/img/Project/GitBlog/post-02/thumbnail.png"
---

# Follow the guidance
---
개인적으로 D2Coding 폰트를 접한 뒤로, 해당 폰트를 즐겨 사용하기에 해당 블로그도 D2Coding 폰트를 적용하였다.
메인페이지 : [d2codingfont](https://github.com/naver/d2codingfont?tab=readme-ov-file)

1. 해당 url에서 최신 버전 폰트 다운로드
![Image1](/assets/img/Project/GitBlog/post-02/1.png)

2. 필요한 폰트를 `/assets/fonts/` 하위에 넣어둔다.
저는 일반 폰트와 Bold 폰트만 다운받아서 넣어뒀습니다.
![Image2](/assets/img/Project/GitBlog/post-02/2.png)

3. `_includes/head.html` 에서 `<style>` 태그 안에 `@font-face`를 작성해준다.
전 일반 폰트는 400, Bold는 600으로 font-weight을 작성했는데, 기존 폰트들이 h 태그에 적용하는건 600, a, p 적용은 400으로 해둬서 맞춰서 해봤습니다.
참고로 다른 폰트를 선호해서 다운받았는데 다른 확장자라면, format 안의 내용을 해당 확장자로 바꾸셔야 합니다.

    ```scss
    @font-face {
        font-family: 'D2Coding';
        font-style: normal;
        font-weight: 400;
        font-display: optional;
        src: local('D2Coding'),
             url("{{ site.baseurl }}/assets/fonts/D2Coding-Ver1.3.2-20180524.ttf") format("truetype");
    }

    @font-face {
        font-family: 'D2CodingBold';
        font-style: normal;
        font-weight: 600;
        font-display: optional;
        src: local('D2CodingBold'),
             url("{{ site.baseurl }}/assets/fonts/D2CodingBold-Ver1.3.2-20180524.ttf") format("truetype");
    }
    ```

4. 해당 파일 하단에 `<script>` 태그 안에 `FontFaceObserver` 와 이걸 load 하는걸 작성해주면 된다.
D2Coding 폰트를 찾을 `FontFaceObserver`를 선언해주고, load 하는건 Promise.all() 안에 작성해줬다.

    ```javascript
    const D2CNObserver = new FontFaceObserver('D2Coding');
    const D2CBObserver = new FontFaceObserver('D2CodingBold');

    Promise.all([
            D2CNObserver.load(),
            D2CBObserver.load(),
            nunitoObserver.load(),
            righteousObserver.load(),
            latoObserver.load(),
        ]).then(function(){
            document.documentElement.className += " fonts-loaded";
        });
    ```

5. `assets/css/style.scss` 에서 `font-family` 적용된 부분에 D2Coding 폰트들을 추가해준다.
`D2Coding`과 `sans-serif`를 제외한 다른 폰트들은 지워도 될 것 같지만, 추후 폰트를 변경할 수도 있을 것 같아 저는 남겨뒀습니다. 용량을 많이 차지하는 것도 아니니까요.

    ```scss
    .fonts-loaded {
      a, span, p { font-family:"D2Coding", "Nunito Sans", 'Lucida Sans', sans-serif; }
      h1, h2, h3 { font-family:"D2Coding", "Lato", Helvetica, sans-serif; }
      mark { font-family:"D2CodingBold", 'Righteous', sans-serif; }
    }
    
    a { text-decoration:none; }
    a, span, p, h1, h2, h3, i { color:#3A241A; }
    a, span, p { font-family:"D2Coding", 'Lucida Sans', sans-serif; }
    h1, h2, h3, mark {
      margin:0;
      font-family:"D2CodingBold", Helvetica, sans-serif;
    }
    ```

다른 블로그 글들 보면 간단하게 scss 파일 별도로 만들어서 거기서 body 태그에 폰트 적용되도록 많이 하더라구요.
빠르고 간단한 방법은 그게 좋긴할텐데, 그냥 기존 코드들 뜯어보고 고치는걸 선호해서 이렇게 진행했습니다. 기본 틀을 해치기 싫기도 했구요.

구글에서 지원하는 외부 폰트를 적용하려면 간단히 `@import` 써서 적용할수도 있습니다.
다만 인터넷에서 외부 폰트를 다운받아서 연결해야할 경우, 로딩이 좀 더 오래 걸릴수도 있다고 합니다.

```scss
@import url(https://fonts.googleapis.com/earlyaccess/nanumgothiccoding.css);
```