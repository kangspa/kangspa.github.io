---
title: "Browsing-Game : React + Phaser를 활용한 블로그 탐색용 게임 제작"
tag:
    - vite
    - react
    - phaser
    - firebase
date: "2025-06-13"
thumbnail: "/assets/img/Computer Science/WebApp/post-10/thumbnail.png"
---

해당 프로젝트는 Vite를 이용해서 빌드하고, Firebase로 배포하였습니다.
배포된 주소 : <https://browsing-game.web.app/>
해당 프로젝트의 Github : <https://github.com/kangspa/browsing-game>

# 프로젝트 만들기

```bash
npm create vite
```
명령을 통해 vite 프로젝트를 만들면서, `React`, `TypeScript`를 선택해준다.

```bash
> npx
> create-vite

│
◇  Project name:
│  browsing-game
│
◇  Select a framework:
│  React
│
◇  Select a variant:
│  TypeScript
│
◇  Scaffolding project in E:\browsing-game...
│
└  Done. Now run:

  cd browsing-game
  npm install
  npm run dev
```

이후 `firebase init`을 통해서 Firebase Console의 프로젝트와 현재 개설한 프로젝트를 연결해준다.
생성된 `firebase.json` 내용을 아래와 같이 수정해주면 완성된다.
`rewrites` 키 작성된 내용을 보면 알 수 있듯이, 해당 프로젝트는 페이지 이동이 필요 없어서 SPA로 설계 후 진행하였다. 

```json
{
  "hosting": {
    "site": "browsing-game",
    "public": "dist",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "/",
        "function": "app"
      }
    ]
  }
}
```

- 메타데이터 수정은 `index.html`의 `head` 태그를 수정해주면 된다.

# App.tsx

해당 파일에서 `App` 함수를 export하여 `main.tsx`에서 로드하는 것을 알 수 있다. 즉, `App` 함수의 return으로 렌더하고자하는 html 구조를 작성해주면 된다.

JSX 문법 사용이 가능해서, 아래와 같이 특정 요소를 반복문 등을 통해 한번에 로드하고 추가할 수 있다.

```tsx
<div className="frame-table">
    {allFrames.map((frame, i) => (
    <div className="frame-row" key={i}>
        <div
        className={frame.type === 'block' ? 'blockFrame' : 'pipeFrame'}
        style={{ backgroundPosition: `-${frame.x}px -${frame.y}px` }}
        />
        <div className="desc">{frame.desc}</div>
    </div>
    ))}
</div>
```

Phaser 게임을 로드할 요소를 `<Game onPipeEnter={handlePipeEnter} />` 태그로 추가했는데, `hadlePipeEnter` 값을 받아온다는 의미이다. Phaser에서 전달해주는 값을 `App.tsx`까지 전달하기 위해서 사용되었다.

아래 내용은 컴포넌트가 처음 렌더링될 때 한번 실행해주기 위해 작성되었다.
만약 []에 다른 함수 등이 들어가 있다면, 해당 값에 따라 작동 시기가 변경된다.

```tsx
useEffect(() => {
  if (iframeRef.current) iframeRef.current.src = TARGET_URL;
}, []);
```

# Game.tsx

Phaser 초기화를 위해 작성된 파일로, 게임 scene 부분과 `App.tsx`를 연결하는 파일이다.
`App.tsx`의 `<Game onPipeEnter={handlePipeEnter} />`에서 봤듯이, `onPipeEnter` 라는 값을 받아오는 것을 볼 수 있다.
그래서 해당 파일에서는 처음에 아래와 같이 작성해줌으로써, `onPipeEnter` 값을 받아온다.

```tsx
type GameProps = {
  onPipeEnter?: (url: string) => void;
};

const Game: React.FC<GameProps> = ({ onPipeEnter }) => {
  const gameRef = useRef<HTMLDivElement | null>(null);
```

이후 `useEffect`에서 `MainScene` 요소에서 `onPipeEnter`를 받아옴으로써 `Mainscene.ts`와 연결해준다.

`config` 내부 설정값들은 [Phaser.js 로 간단한 플랫폼 게임 설계](/Computer%20Science/Programming/post-08.html) 내용을 참고한다.
이 때 `scene` 값은 `MainScene`에서 변화하는 `onPipeEnter` 값을 지속적으로 유지하기 위해 별도로 선언 후 입력해줬다.

# Mainscene.ts

본격적으로 제작하려는 게임 화면에 대해 작성하는 부분이다.
Mainscene에서 사용할 변수들을 우선 선언해준다.

```ts
private targetUrl = 'https://kangspa.github.io/'; // 대상 URL

private player!: Phaser.Physics.Arcade.Sprite;
private cursors!: Phaser.Types.Input.Keyboard.CursorKeys;
private lastDirection: 'left' | 'right' = 'right';

private platforms!: Phaser.Physics.Arcade.StaticGroup;
private pipeH!: Phaser.Physics.Arcade.Sprite;
private pipeR!: Phaser.Physics.Arcade.Sprite;
private pipes!: Phaser.Physics.Arcade.StaticGroup;
private onPipeEnter?: (url: string) => void;
private isEnteringPipe = false;

private urlList!: string[]; // URL 목록을 저장할 프로퍼티
private pageCount!: number; // 페이지 수를 저장할 프로퍼티
private currentPage!: number; // 현재 페이지를 저장할 프로퍼티

constructor(onPipeEnter?: (url: string) => void) {
  super('MainScene');
  this.onPipeEnter = onPipeEnter;
}
```

## preload

`preload` 단계에서는 asset들을 로드해주는데, 특이사항으로 url을 웹크롤링하여 list 형태로 만든다는 것이다.

```ts
preload() {
  this.load.image('sky', '/sky.png');
  this.load.image('grass', '/grass.png');
  this.load.image('cloud', '/cloud.png');
  this.load.spritesheet('blocks', '/usedBlock.png', { frameWidth: 16, frameHeight: 16 });
  this.load.spritesheet('pipes', '/usedPipe.png', { frameWidth: 32, frameHeight: 32 });
  this.load.spritesheet('mario', '/merged_output.png', { frameWidth: 17, frameHeight: 16 });
}

private async loadUrls() {
  this.urlList = await fetchAndParseHTML(this.targetUrl);
  this.pageCount = Math.ceil(this.urlList.length / 5) - 1;
  this.currentPage = 0; // 현재 페이지 초기화
  console.log('Fetched URLs in scene:', this.urlList);
}
```

`fetchAndParseHTML`은 별도의 파일로 만들어뒀는데, 현재 블로그의 글 목록을 반환해주는 함수이다.
추가로 페이지네이션 작업을 위해 전체 페이지 수(pageCount) 및 현재 페이지(currentPage)를 초기화해서 저장한다. 블로그의 currentPage와는 다르게 0으로 초기화했는데, urlList에서 현재 조회해야하는 index 계산이 편하게 하기 위해서 0으로 초기화했다.

## create

`create` 함수에서 platform 및 player 추가는 [튜토리얼](/Computer%20Science/Programming/post-08.html)과 다를 것 없다.
블럭의 경우, 작동 방식은 전부 동일하다.

아래는 블럭 요소를 추가하여 플레이어와 상호작용(충돌) 시 발생하는 콜백함수를 작성한 것이다.

```ts
const nextBlock = this.physics.add.staticSprite(288, 150, 'blocks', 5);
this.physics.add.collider(this.player, nextBlock, (obj1, obj2) => {
  const player = obj1 as Phaser.Physics.Arcade.Sprite;
  const block = obj2 as Phaser.Physics.Arcade.Sprite;

  const body = player.body as Phaser.Physics.Arcade.Body;
  if (body.touching.up && !this.isEnteringPipe) {
    // 블록 튕기기 애니메이션
    this.tweens.add({
      targets: block,
      y: block.y - 8,
      duration: 100,
      yoyo: true,
      ease: 'Power1',
    });

    const iframe = document.querySelector('iframe') as HTMLIFrameElement;
    iframe?.contentWindow?.postMessage('click-next', 'https://kangspa.github.io');
    if (this.pageCount !== this.currentPage) this.currentPage++;
  };
});
```

충돌 애니메이션이므로 `.collider`를 사용하고, 콜백함수에 해당하는 두 요소를 인자로 추가해준다.

다른 방향에서 충돌 시에는 작동하지 않았으면 해서, `body.touching.up`을 통해 플레이어의 위에 방향이 충돌할 경우로 조건을 걸었다.
이 때, 페이지네이션 관여하는 블럭은 메인페이지에서만 작동해야하므로 `!this.isEnteringPipe` 조건을 추가해뒀다.

상호작용된 것을 확실히 알도록 `.tweens.add`로 애니메이션을 추가해줬다.
`yoyo: true` 설정을 함으로써 블럭이 y 기준 8만큼 올라가도 다시 내려오도록 해준다.

js 문법으로는 iframe 내부 요소에 직접 클릭 등의 이벤트 요소를 발생시킬 수가 없어서, `postMessage`를 통해 정해진 메세지를 전송하고 블로그에서 수신하면 해당 메세지에 따라 블로그 내에서 이벤트가 발생하도록 하였다. 직접 이벤트 요소를 발생시킬 수 없는 이유는 cors 문제로 인해 그런 것 같은데, Github 페이지에서 관련 문제 해결을 어떻게 할지 모르겠어서 이와 같은 편법을 동원하였다. (현재 블로그가 Github page로 hosting 중이다.)
현재 jekyll 테마에서 어디를 수정해야될지 참고하려면 [browsing-game의 깃헙 페이지](https://github.com/kangspa/browsing-game?tab=readme-ov-file#iframe%EA%B3%BC%EC%9D%98-%EC%83%81%ED%98%B8%EC%9E%91%EC%9A%A9)를 참고한다.

파이프의 경우 3종류가 있는데, 각 페이지 진입을 위한 파이프는 인덱스 값을 고유하게 갖도록 하기 위해 `as PipeWithIndex`로 pipe를 선언하며 `pipes.create`을 하였다.

```ts
interface PipeWithIndex extends Phaser.Physics.Arcade.Sprite {
  pipeIndex: number;
}
...
const pipePositions = [350, 446, 542, 638, 734];
pipePositions.forEach((x, i) => {
  const pipe = this.pipes.create(x, 202, 'pipes', i) as PipeWithIndex;
  pipe.setImmovable(true);
  pipe.pipeIndex = i; // 사용자 정의 프로퍼티로 index 저장
});
```

`MainScene` 선언 전에 보면 알 수 있듯이, `PipeWithIndex`는 말 그대로 인덱스 값을 각각 갖고 있도록 하기 위해 추가해준 인터페이스이다.

## update

현재 사용한 마리오 스프라이트 시트의 경우, 정지 상태에서 좌우 이미지가 다르다.

그래서 키보드의 마지막 입력이 좌인지, 우인지에 따라서 `lastDirection` 값을 저장해주고, 거기에 맞춰서 캐릭터 이미지를 몇번째 프레임의 이미지를 쓰는지 정해준다.

```ts
if (this.cursors.left?.isDown) {
  this.player.setVelocityX(-160);
  this.player.anims.play('left', true);
  this.lastDirection = 'left';
} else if (this.cursors.right?.isDown) {
  this.player.setVelocityX(160);
  this.player.anims.play('right', true);
  this.lastDirection = 'right';
} else {
  this.player.setVelocityX(0);
  this.player.anims.stop();
  if (this.lastDirection === 'left') {
    this.player.setFrame(5);
  } else {
    this.player.setFrame(6);
  }
}
```

만약 플레이어가 윗쪽 방향키를 누른다면, 300만큼 점프를 하도록 해준다. 아래방향키를 눌렀다면, 어느 위치에서 아래 방향키를 눌렀는지에 따라 다른 이벤트가 발생하도록 작성해준다.

```ts
const body = this.player.body as Phaser.Physics.Arcade.Body;
if (this.cursors.up?.isDown && body.onFloor()) {
    this.player.setVelocityY(-300);
}

if (this.cursors.down?.isDown && body.blocked.down) {
  const playerBounds = this.player.getBounds();

  for (const pipe of this.pipes.getChildren()) {
    const p = pipe as PipeWithIndex;
    const pipeBounds = p.getBounds();

    const isOnPipe =
      playerBounds.bottom === pipeBounds.top &&
      playerBounds.right > pipeBounds.left &&
      playerBounds.left < pipeBounds.right;

    if (isOnPipe && !this.isEnteringPipe) {
      this.isEnteringPipe = true;
      const index = p.pipeIndex;
      const url = this.urlList[index + this.currentPage * 5];
      this.onPipeEnter?.(url);
      this.playPipeTransitionAnimation();
      break; // 다른 파이프 검사하지 않음
    }
  }
  // pipeH에 진입 이벤트 발생하는지 확인
  const pipeHBounds = this.pipeH.getBounds();
  const isOnPipeH =
    playerBounds.bottom === pipeHBounds.top &&
    playerBounds.right > pipeHBounds.left &&
    playerBounds.left < pipeHBounds.right;
  if (isOnPipeH && this.isEnteringPipe) {
    this.isEnteringPipe = false;
    const iframe = document.querySelector('iframe') as HTMLIFrameElement;
    iframe?.contentWindow?.postMessage('go-back', 'https://kangspa.github.io');
    this.playPipeTransitionAnimation();
  }
  // pipeR에 진입 이벤트 발생하는지 확인
  const pipeRBounds = this.pipeR.getBounds();
  const isOnPipeR =
    playerBounds.bottom === pipeRBounds.top &&
    playerBounds.right > pipeRBounds.left &&
    playerBounds.left < pipeRBounds.right;
  if (isOnPipeR) window.location.reload();
};
```

페이지로 이동하는 파이프에서 눌렀다면, `onPipeEnter`의 url 값만 변경해주고, 이 값은 타고타고 `App.tsx`에서 인식하여 iframe에 url 값을 변경해준다. 이 때 for 문으로 pipe들을 검사하는데, break을 하지 않으면 다른 파이프도 계속 검사하게 되므로 잊지말고 break을 해줘야한다.

`pipeH`는 게임 화면 상 가장 좌측의 파이프로, 현재 다른 post 안에 있을 경우 `postMessage`로 'go-back' 명령을 전송한다. iframe에서는 해당 명령 수신 시 뒤로가기를 하는데, 이렇게 해야 페이지네이션 중 마지막 탐색하던 페이지로 이동하기에 뒤로가기로 구현하였다.

`pipeR`은 플레이어가 나타나는 블럭으로, 만약 해당 위치에서 아래 방향키 클릭 시에는 현재 화면을 새로고침해준다.
게임과 iframe이 서로 맞지 않는 등의 오류가 발생할 경우, 이를 게임 내에서 초기화하기 위해 만들어뒀다.

발견됐던 오류는 포스트 이동 후 뒤로가기 했을 때, 페이지네이션 버튼 이동 시 글 목록이 하나도 나오지 않는 오류가 있었다. 원래 존재하는 페이지인데 글은 없는 경우가 있었는데, 해당 오류는 현재 플로그 js 중 `subject.js`에 아래 부분을 수정하여 해결하였다.

```js
        window.addEventListener("load", (event) => {
            // Load last visited page number
            if (event.persisted 
            || (window.performance && window.performance.navigation.type == 2)) {
                currentPage = Number(localStorage.getItem(pageKey)); // 117번째 줄 : localStorage에서 가져올 때 Number로 제대로 변환해서 currentPage에 저장하도록 수정
            }
```
해당 부분에서 `currentPage` 변수의 type이 제대로 일치하지 않아서 페이지네이션으로 currentPage 값을 + 나 - 할 때 오류가 발생했던 것으로 추정된다.

# 기타 사항

최대한 게임 화면과 iframe이 한 화면에 다 나올 수 있도록 높이를 조절하여 넣어뒀다. 물론 브라우저 화면을 작게 쓸 경우에는 어쩔 수 없겠지만, 위아래 높이는 다 채웠다는 가정 하에 900 px 이내로는 깔끔하게 보일 것이다.
좌우 너비의 경우, 1300px 기준으로 더 클 경우에는 우측에 간단한 설명이 나오도록, 더 작을 경우에는 게임 렌더 화면 하단에 나오도록 미디어 쿼리를 작성해두었다.

```css
#app {
  display: flex;
  flex-direction: column; /* 기본: 수직 정렬 */
  align-items: center;
  gap: 2rem; /* 요소 간 간격 */
}
#descript {
  width: 600px;
}

/* 화면 너비가 1300px 이상일 때는 수평 정렬 */
@media (min-width: 1300px) {
  #app {
    flex-direction: row;
    align-items: flex-start; /* 위쪽 정렬 */
    justify-content: center;
  }

  #main,
  #descript {
    flex: 0 0 auto; /* 너비 고정 */
  }
  #descript {
    width: 400px;
  }
}
```

또한 iframe은 원래 직접 조작도 가능한데, 해당 페이지에서는 iframe을 직접 조작하면 변수 값들이 꼬일 수가 있으므로 게임으로만 조작해야 됐다.
그래서 `.iframe-overlay` 요소를 iframe과 같이 뒀는데, 이를 투명화시켜 직접 마우스로 iframe 요소를 조작하지 못하게 하였다.

```tsx
<div className="iframe-wrapper" style={{ marginTop: '2rem', position: 'relative', width: '800px', height: '500px' }}>
    <iframe
    id="browser"
    ref={iframeRef}
    title="External Site"
    width="800"
    height="500"
    style={{ border: '1px solid #ccc' }}
    />
    <div className="iframe-overlay" />
</div>
```        
```css
.iframe-wrapper {
  position: relative;
  width: 800px;
  height: 500px;
}

.iframe-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 10;
  background-color: transparent; /* 완전 투명 */
  pointer-events: all; /* 마우스 이벤트를 가로채기 */
}
```

수정 못한 부분으로는 iframe 내부에서는 댓글 관련 내용들을 볼 수 없다는 것이다. 해당 부분은 giscus를 사용하다보니 CSP 정책으로 인해 발생하는 오류다.
현재 내 페이지에 적용된 Giscus 관련 보안 정책을 어디서 수정해야할지 알 수 없어 우선 마무리한다.