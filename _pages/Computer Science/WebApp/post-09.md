---
title: "vite 프로젝트"
tag:
    - vite
    - build
    - module js
    - firebase
date: "2025-01-27"
thumbnail: "https://miro.medium.com/v2/resize:fit:1200/1*udvSMrSVGOgD4fxjMJHbOw.jpeg"
---

`vite` 는 간단히 말하자면 build를 도와주는 툴이다.
실제 서버에서 사용되는 파일들의 최적화와 경량화를 도와줘서, 서버 구동 속도를 빠르게 만들어준다.

`vite`의 시작은 <https://ko.vite.dev/guide/> 공식 doc을 참고해서 따라가주면 되는데, 필자는 firebase로 프로젝트를 만들었기에 여기에 vite 적용하는 부분만 작성한다.

`vite` 사용 시 한가지 번거로운 점은 자바스크립트를 작성하고 적용할 때, `type="module"`로 적용해야 한다는 것이다.

## module js

일반적으로 jquery를 사용할 때, 아래처럼 별도의 스크립트 소스를 먼저 불러오고, jquery를 적용한 js 코드를 불러온다.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="app.js"></script>
```

하지만 module로 불러올 경우, 위와 같은 상황에서 `app.js`는 jquery 문법을 사용하지 못 한다.
서로 별개의 javascript 코드라서 그렇다고 한다.

그렇다면 module 로 불러오는 javascript 코드에서는 어떻게 cdn 등 외부 코드를 불러와서 사용할 수 있을까?
아래와 같이 import 구문으로 불러와서 사용이 가능하다고 한다.

```javascript
import $ from "jquery";

$("#title").on("click");
```

이렇게 작성된 코드는 html에서 불러올 때, `type="module"`을 붙여주고 불러오면 된다.

```html
<script type="module" src="app.js"></script>
```

`vite`는 이렇게 module로 작성된 javascript 코드들에 대해 build 할 때 대상으로 잡고 패키징해준다.
즉, `type="module"`로 적용하지 않은 js 파일들은 build 대상에 포함되지 않아 별도의 조치를 해두지 않으면 html 파일만 패키징되고, 확인 안 할 경우 그냥 그렇게 배포되버린다...

## vite build

그렇다면 어떻게 `build`가 이루어지는지 보자.
기본적으로 루트 디렉터리에 `index.html`이 있어야 한다. 그럼 `vite`는 해당 파일을 기준으로 사용되는 파일들을 패키징 하기 시작한다.
그렇게 패키징된 파일들은 'dist'라는 폴더 내에 만들어진다. 만들어진 파일들을 살펴보면, 기본적으로 절대경로로 작성된 부분은 상대경로로 변경되고, js 코드들은 전부 변수명들이 변경되어 쉽게 해석이 어려워진다.

이런 변경사항 없이, 그냥 무조건 옮기고 싶다 하는 파일들이 있다면, 처음부터 'public' 폴더 안에 넣어두면 된다.
`vite build`는 public 폴더 내부의 내용은 그대로 'dist' 폴더로 복사한다. 나는 js로 로드해서 사용하는 html, header나 footer를 여기에 넣었다.
추가로 기본적인 템플릿을 그대로 사용하다보니 module로 작성되지 않은 js 파일들도 여기에 넣어둬서, `vite build` 시 누락되지 않도록 하였다.

'public' 폴더 안에 작성해둔 파일을 참조할 때는, 'public'은 제외하고, 절대경로로 명시하여 접근하면 된다.
이후 로컬에서 테스트 진행할 때, `vite` 명령어로 실행해서 확인하면, 'public' 폴더 안의 파일에 대해 이상없이 접근한 것을 볼 수 있다.
즉, `/public/image.png` 가 아니라, `/image.png` 로만 작성해둬도 로컬에서 테스트 및 배포할 때 경로가 꼬이는 일이 없다.

## vite.config.js

`firebase.json`처럼 `vite`를 build 할 때 여러 설정 값들을 작성해둘 수 있는 파일이다.
필자는 아래와 같이 작성하여 사용하였다.

```javascript
import { defineConfig } from 'vite';
import { resolve } from 'path'

export default defineConfig({
  base: './',
  build: {
    outDir: 'dist',
    emptyOutDir: true,
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        notfound: resolve(__dirname, '404.html'),
        profile: resolve(__dirname, 'page/profile.html'),
      }
    }
  },
  optimizeDeps: {
    include: ['firebase/app', 'firebase/auth', 'jquery'],
  },
});
```

`base`는 현재 메인이 되는 루트 디렉터리, `build.outDir`은 `vite build` 후 결과물을 저장할 폴더명, `build.emptyOutDir`은 `vite build` 진행 시 결과물 저장할 폴더를 비우고 build할 것인지 정하는 값이다.
`rollupOptions.input`은 사용하는 파일들을 명시해둔 값이라고 생각하면 편하다. 해당 부분을 작성해두지 않으니 `index.html`을 제외한 다른 html 파일들이 build 되지 않아 작성하여 사용하였다.
필자는 html 파일들만 명시해두는 용도로 사용하였지만, 아마 찾아보면 다른 파일들도 build 대상으로 명시하는데 사용 가능할 것으로 보인다.
`optimizeDeps.include`는 module js에서 import 한 외부 패키지들을 명시해두는 부분이다.
즉, `npm install jquery`를 한 후, module js에서 `import $ from "jquery";`를 명시하여 사용 중이라면, `optimizeDeps.include`에 jquery를 작성해둬야 이상없이 jquery 문법이 작동한다.
다른 패키지에 대해서도 배열 내 값으로 쭉쭉 추가해나가면 된다.

## firebase에 적용

firebase에서는 public 폴더를 기준으로 deploy가 이루어졌는데, ["firebase.json rewrite 작성"](/Computer Science/WebApp/post-08.html) 내용을 참고하면 알 수 있듯이 `firebase.json`에서 `hosting.public` 값을 dist로 바꾸면 dist 폴더 기준으로 deploy를 할 수 있다.