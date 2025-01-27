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

초보 개발자에게 `vite` 사용 시 한가지 번거로운 점은 자바스크립트를 작성하고 적용할 때, `type="module"`로 적용해야 한다는 것이다.

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
`vite build`는 public 폴더 내부의 내용은 그대로 'dist' 폴더로 복사한다. 필자는 js로 로드해서 사용하는 html, header나 footer를 여기에 넣었다.
추가로 기본적인 템플릿을 그대로 사용하다보니 module로 작성되지 않은 js 파일들도 여기에 넣어둬서, `vite build` 시 누락되지 않도록 하였다.

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

## vite.config.js 작성용 js 코드

["firebase.json rewrite 작성"](/Computer Science/WebApp/post-08.html)에서 작성한 것처럼, vite.config.js도 html 파일이 많아질수록 하나하나 명시를 해줘야하여, 필자는 코드로 `vite.config.js`를 작성했다.
`firebase.json`과 차이점은 js 파일이다보니, 그냥 텍스트 작성하듯이 하고 저장을 js 파일로 저장했다는 것이다.

```javascript
// vite.config.js의 앞부분 생성
let viteTemplate = `import { defineConfig } from 'vite';
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
`;

// viteTemplate에 사용하는 html 맵핑
htmlList.forEach(htmlFile => {
  const dir = htmlFile.split('/');
  const name = dir[dir.length - 1];
  viteTemplate += `        ${name}: resolve(__dirname, 'page${htmlFile}.html'),\n`
});

// vite.config.js의 뒷부분 생성
viteTemplate += `      }
    }
  },
  optimizeDeps: {
    include: ['firebase/app', 'firebase/auth', 'jquery'],
  },
});
`;

// 최종 vite.config.js를 test.js로 저장
const viteOutput = path.join(__dirname, 'vite.config.js');
fs.writeFileSync(viteOutput, viteTemplate);
```

## firebase에 적용

firebase에서는 public 폴더를 기준으로 deploy가 이루어졌는데, ["firebase.json rewrite 작성"](/Computer Science/WebApp/post-08.html) 내용을 참고하면 알 수 있듯이 `firebase.json`에서 `hosting.public` 값을 dist로 바꾸면 dist 폴더 기준으로 deploy를 할 수 있다.

그리고 `index.html` 파일과 `404.html` 파일은 루트 디렉터리에 두는데, 해당 파일들이 public에 있으면 `vite build`에서 그냥 복사되기만 하기에 `vite`를 사용하는 이유가 없어지기 때문이다. vite에서 public 역할을 하는 폴더를 바꿀 수 있다고 알고는 있지만, 번거로운 부분이기에 굳이 그러진 않았다.

다른 html 파일들처럼 'page'나 'views'에 넣지 않은 이유는 firebase 기준 때문이다. 루트 디렉터리의 `index.html`을 기준으로 메인 화면을 열고, 존재하지 않는 페이지 접근 시에는 루트 디렉터리의 `404.html` 파일을 렌더 해준다. 즉 다른 폴더 하위에 존재하면 의도대로 작동하지 않게 된다.
해당 부분 때문에 `vite build` 이후 `404.html`에 한가지 조치를 취해줘야하는데, `404.html` 내에서 css, img, js 등 외부 파일 불러오는 부분을 전부 절대경로로 바꿔줘야한다는 것이다.
firebase에서 404 에러로 인해 `404.html`을 렌더해줄 때, 해당 에러가 발생한 path 기준으로 렌더를 해준다. 근데 404 에러가 메인에 해당하는 path가 아니라 다른 하위 path(/account 등)에서 발생한다면 해당 폴더 기준으로 다른 assets를 찾다보니 css가 적용이 안되는 등 문제가 발생했다.
그래서 필자는 파이썬으로 아래와 같이 작성하여 상대경로를 절대경로로 바꿔주는 조치를 취했다. 모든 assets을 'assets' 폴더 안에 몰아둬서 취할 수 있는 조치였다.

```python
with open('dist/404.html', 'r') as file:
    filedata = file.read()
filedata = filedata.replace('./assets', '/assets')

with open('dist/404.html', 'w') as file:
    file.write(filedata)
```

이제 나머지는 사용하기 편하게 파일 정리해서 사용하면 된다. 필자 같은 경우는 위 코드들에서 알 수 있듯이 `page` 폴더 내에 html 파일들을 몰아두고 관리하고, `firebase.json`이랑 `vite.config.js`로 명시하였다.
vanilla js 는 'assets' 하위에 몰아둬서, assets는 'public' 폴더 안에 넣어뒀고, module js는 'modulejs'를 만들어서 루트 디렉터리에 두고 관리했다. 이 때 실수가 css, img 파일들도 전부 assets 폴더 안에 넣어둬서, 그냥 복사가 됐는데, 사실 해당 파일들도 `vite build` 대상이 된다고 알고 있어 굳이 public 폴더 안에 넣어둘 필요는 없다고 알고 있다.
다만 프로젝트 당시 별도로 구매한 템플릿을 그대로 사용하면서 일부 사용되는 image 파일이나 css 파일이 누락되는게 있는지, 그대로 배포하면 에러가 발생하여 public 폴더에 넣어두고 진행하였다.

제대로 `vite`를 사용한다면 사실 public 폴더 안에 최대한 아무런 파일도 안 넣어두는게 베스트일 것이다.