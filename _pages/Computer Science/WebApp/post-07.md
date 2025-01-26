---
title: "Firebase 프로젝트 시작하기"
tag:
    - firebase
    - start
date: "2025-01-25"
thumbnail: "https://firebase.google.com/static/images/brand-guidelines/logo-vertical.png"
---

### Firebase의 장점
- 여러 가지 백엔드 시스템 지원
- Console을 통한 빠르고 편한 관리
- 무료 호스팅 제공 & 라우팅 제공
- 통계 정보 제공

### Firebase의 단점
- 응답 서버가 느리다.
- DB에서 데이터 조회하기가 어렵다.

# Firebase Console에서 프로젝트 생성
<https://console.firebase.google.com/>에 접속하여, 프로젝트 시작을 누르고 진행하여 생성한다.
![Image1](/assets/img/Computer Science/WebApp/post-07/1.png)

전부 완료하면, 아래처럼 해당 프로젝트 페이지로 이동하게 된다.
![Image2](/assets/img/Computer Science/WebApp/post-07/2.png)

# Local 프로젝트와 Firebase 연결

## Firebase CLI 설치
아래와 같은 명령어로 firebase cli를 설치해준다.

```bash
npm install -g firebase-tools
```

## Firebase CLI 로그인
`firebase login` 로 firebase cli에서 계정 로그인을 해준다.
진행하면 브라우저가 열리며 계정을 선택할 수 있다.
![Image3](/assets/img/Computer Science/WebApp/post-07/3.png)

## Firebase init 으로 프로젝트 시작
프로젝트 생성하고자 하는 루트 디렉터리에서 `firebase init` 커맨드를 통해 시작 및 연결한다.

진행하면 처음에 어떤 목적으로 세팅하는지, 선택할 수 있다.
웹 배포를 목적으로 하는거니까 `Hosting` 으로 선택.
이 때 `SpaceBar`로 선택하고나서 `Enter`를 통해 진행해준다. (여러 개 선택이 가능)
![Image4](/assets/img/Computer Science/WebApp/post-07/4.png)

다음으로 firebase 프로젝트를 선택하면 되는데, 기존에 있는 프로젝트로 할지, 새로 만들지, GCP에서 갖고올지 정할 수 있다.
앞서 Firebase Console에서 이미 프로젝트를 생성했으므로, 첫번째의 `Use an existing project`를 선택해준다.
그러면 로그인 한 계정 기준으로 생성한 프로젝트 목록들이 나오는데, 앞서 만들었던 걸로 선택해주면 된다.
![Image5](/assets/img/Computer Science/WebApp/post-07/5.png)

다음은 기본적인 Hosting setting이다.
public directory 를 선택하라고 나오는데, default로 public이 입력되어 있어 그냥 `Enter`를 통해 진행해주면 된다.
`Configure as a single-page app (rewrite all urls to /index.html)?` 은 단일 페이지로 서비스 호스팅을 할 것인지 정하는 것이다.
여러 디렉터리별로 페이지를 만들려면 N을 하면되는데, 필자는 SPA로 해당 프로젝트를 진행할 생각이라 y로 진행하였다.
다음으로 깃헙 배포를 자동으로 할 것인지 선택하는건데, 필자도 해당 옵션은 기존에 사용해본 적이 없어, 이번에 한번 사용해보기로 하였다.
![Image6](/assets/img/Computer Science/WebApp/post-07/6.png)

y를 하면 Github 페이지가 브라우저에서 열리고, 로그인을 진행해주면 된다.
이후 연결할 Repository를 `user/repository` 형태로 작성해준다. 이 때 해당 레포는 public이여야 한다.
![Image7](/assets/img/Computer Science/WebApp/post-07/7.png)

배포 전 빌드 스크립트를 실행할지도 정할 수 있는데, 어떤 스크립트를 실행할 것인지도 정할 수 있다.
default가 (npm ci && npm run build) 이고, 무엇을 사용하여 build 하냐에 따라 다른 스크립트를 작성해줄 수도 있다.
해당 내용은 `firebase-hosting-pull-request.yml`에 작성되므로, 추후 직접 변경해줄 수도 있을 것 같다.
![Image8](/assets/img/Computer Science/WebApp/post-07/8.png)

다음은 github 배포 방식을 정하는 부분으로, 어떤 브랜치 명을 기준으로 `pull&request`, `merge` 할 것인지 정할 수 있다.
![Image9](/assets/img/Computer Science/WebApp/post-07/9.png)

## firebase-tools 설치 및 배포
`npm install -g firebase-tools`로 호스팅 배포를 위한 툴을 먼저 설치해준다.
설치가 끝나면 `firebase deploy`로 배포해주면된다.

# Firebase Hosting 도메인 확인
다시 Firebase Console로 돌아가서, `Hosting` 메뉴를 들어가준다.
이후 시작하기를 눌러주면, 앞서 진행한 내용들이 그대로 나온다.
![Image10](/assets/img/Computer Science/WebApp/post-07/10.png)

해당 과정을 전부 진행하고나면, `Hosting` 메뉴 화면이 아래처럼 바뀐다.
![Image11](/assets/img/Computer Science/WebApp/post-07/11.png)

도메인에 제공되는 url이 무료로 제공받는 도메인 주소이다. 기본으로 2가지를 제공해주고, 별도의 도메인명으로 배포가 필요하다면 추가 가능하다.

---

Git 블로그처럼 무료로 도메인을 제공해준다는 점에서 좋은 서비스라고 생각된다.
유료 프로젝트로 전환할 경우, Cloud Functions을 쓸 수도 있는데 이러한 부분은 추후 작성하겠다.