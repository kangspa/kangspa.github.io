---
title: Phaser.js 로 간단한 플랫폼 게임 설계
tags:
    - Phaser
    - 게임
date: "2025-06-11"
thumbnail: "https://cdn.phaser.io/tutorials/making-your-first-phaser-3-game/tutorial_header.png"
---

해당 내용은 [Making your first Phaser 3 game](https://phaser.io/tutorials/making-your-first-phaser-3-game/part1) 내용 중 [Part10](https://phaser.io/tutorials/making-your-first-phaser-3-game/part10)의 코드 관련 내용만 정리하였습니다.

# Phaser 요소 만들기

```javascript
var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 300 },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

var game = new Phaser.Game(config);
```

위와 같이 config를 설정하고 phaser를 초기화하면, 기본으로 `body` 태그 안에 게임 화면을 로드한다.
특정 요소에 로드하고 싶다면, `parent` key 값을 통해 어떤 ID를 가진 요소 안에 렌더링할지 정할 수 있다.

- `type` : Phaser가 사용할 렌더링 방식
- `width`, `height` : 렌더할 게임화면의 크기
- `physics` : 물리 엔진 관련 설정 (`default`는 물리 엔진 종류)
    - `arcade` key 하위에 중력 작용 방향 및 크기를 정해준다. (위 값은 아래 방향으로 300의 중력 작용)
- `scene` : 게임의 각 단계를 정의한다.
    - `preload` : asset(이미지 등) 로딩
    - `create` : 게임 내 설정 및 초기 값 등 로드
    - `update` : 프레임마다 호출되어야 하는 루프 함수

# preload

```javascript
function preload ()
{
    this.load.image('sky', 'assets/sky.png');
    this.load.image('ground', 'assets/platform.png');
    this.load.image('star', 'assets/star.png');
    this.load.image('bomb', 'assets/bomb.png');
    this.load.spritesheet('dude', 'assets/dude.png', { frameWidth: 32, frameHeight: 48 });
}
```

게임에서 사용할 이미지나 스프라이트시트를 불러온다.
첫번째 인자는 아래에서 불러올 때 사용할 이름(임의로 설정), 두번째 인자는 해당 asset의 경로이다.
spritesheet의 경우 각 프레임별 크기 및 프레임별 간격 등 추가 인자 설정이 가능하다.

### spritesheet(스프라이트시트)란?

여러 이미지를 각각 로드하는 것보다, 하나의 이미지에서 필요한 부분만 별도로 잘라서 사용하는게 로딩에 부담이 덜하여 사용하는 방식.
주로 연속된 프레임이 필요한 캐릭터 애니메이션 등에서 사용된다.

phaser에서는 spritesheet 로드할 때, 프레임별 이미지 크기가 동일할 경우 위와 같이 `frameWidth`, `frameHeight`을 작성해서 로드할 수 있다.
위와 같이 작성할 경우 spritesheet의 첫번째 위치부터 32x48 크기로 이미지를 잘라서 프레임으로 구분한다는 의미이다.
추가로 `startFrame`, `endFrame`으로 로드할 프레임을 제한할 수도 있고, `margin`을 통해 시트 이미지의 여백이 있다면 해당 값 설정, `spacing` 등을 통해 프레임 별 간격 설정도 가능하다.

## 고정된 프레임이 아닌 경우

`.load.atlas` 로 서로 다른 크기, 좌표에 존재하는 프레임들을 로드할 수 있다.
단, 각 프레임에 대한 정보가 제대로 입력되어 있는 `json` 파일이 필요하다.

```json
{
  "frames": {
    "walk_1": { "frame": { "x": 0, "y": 0, "w": 32, "h": 48 } },
    "walk_2": { "frame": { "x": 32, "y": 0, "w": 32, "h": 48 } },
    ...
  },
  "meta": {
    "image": "player.png"
  }
}
```
위와 같이 각 프레임별 명칭 및 해당 프레임의 시작 좌표와 너비, 높이가 작성되어 있으면, 아래와 같이 작성해서 로드할 수 있다.

```javascript
this.load.atlas('player', 'assets/player.png', 'assets/player.json');
```

# create

```javascript
function create ()
{
    //  A simple background for our game
    this.add.image(400, 300, 'sky');

    //  The platforms group contains the ground and the 2 ledges we can jump on
    platforms = this.physics.add.staticGroup();

    //  Here we create the ground.
    //  Scale it to fit the width of the game (the original sprite is 400x32 in size)
    platforms.create(400, 568, 'ground').setScale(2).refreshBody();

    //  Now let's create some ledges
    platforms.create(600, 400, 'ground');
    platforms.create(50, 250, 'ground');
    platforms.create(750, 220, 'ground');
```

`this.add.image` 는 말 그대로 이미지를 넣는 용도로, 해당 코드에서는 백그라운드 이미지 추가에 사용된다.

`platforms`로 `staticGroup`을 만들어서, 동일한 속성을 부여할 요소들을 위와 같이 만들 수 있다.
`staticGroup`은 고정된 물체를 로드하는 것으로, 플레이어와 충돌해도 움직이지 않는 물체 등에 사용된다.
단순히 `group`으로 만들 경우, 별도의 설정을 하지 않으면 플레이어와 충돌 시 움직이게 되는 것을 볼 수 있다.

`.create`의 인자 순서는 해당 요소를 추가할 x 좌표, y 좌표, 어떤 asset을 추가할 것인지 이름(`preload`에서 로드 시 작성한 명칭)을 작성해주면 된다.
이 때 주의할 점으로 좌표 값은 asset의 중심 기준이므로 헷갈리면 안된다. (`.atlas` 등으로 spritesheet 로드시 작성되는 값은 프레임 좌측 상단 기준이라 헷갈린다.)

`.setScale(2)` 는 로드하는 asset을 2배 크기로 키우는 것으로, 이후 캐릭터와의 충돌범위 오류가 발생하지 않도록 하기 위해 `.refreshBody`를 통해 2배 크기가 제대로 적용되도록 해준다.

```javascript
    // The player and its settings
    player = this.physics.add.sprite(100, 450, 'dude');

    //  Player physics properties. Give the little guy a slight bounce.
    player.setBounce(0.2);
    player.setCollideWorldBounds(true);

    //  Our player animations, turning, walking left and walking right.
    this.anims.create({
        key: 'left',
        frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
        frameRate: 10,
        repeat: -1
    });

    this.anims.create({
        key: 'turn',
        frames: [ { key: 'dude', frame: 4 } ],
        frameRate: 20
    });

    this.anims.create({
        key: 'right',
        frames: this.anims.generateFrameNumbers('dude', { start: 5, end: 8 }),
        frameRate: 10,
        repeat: -1
    });
```

`this.physics.add.sprite` 를 통해 스프라이트 시트에서 로드한 asset을 입력한 좌표의 위치에 로드할 수 있다. 위와 같이 작성할 경우, 기본으로 0번째 프레임의 이미지를 그대로 로드하고, 특정 프레임을 첫번째로 로드하고 싶다면 `player.setFrame(6);`과 같이 작성해서 6번째 프레임의 이미지를 로드할 수도 있다.

`.setBounce` 는 플레이어가 얼마나 튕길지 정해주며, 1로 설정하면 완전 탄성을 가진 물체처럼 설정된다.
`.setCollideWorldBounds` 는 렌더된 화면 밖으로 못 나가게 설정해줄 수 있는데, `false`일 경우 화면 밖으로 플레이어를 보낼 수 있다.

`this.anim.create`은 캐릭터의 애니메이션을 설정하는데 사용된다. 반복되는 애니메이션 설정이 필요할 경우 , `repeat: -1`을 통해 루프 설정이 가능하다.
`this.anims.generateFrameNumbers('dude', { start: 5, end: 8 })` 같은 경우, 해당 애니메이션은 `dude` asset의 5~8까지의 프레임을 순서대로 사용한다는 의미이다.

```javascript
    //  Input Events
    cursors = this.input.keyboard.createCursorKeys();
```

키보드 이벤트 추가를 위해 추가하며, 추후 `update` 함수에서 키보드 이벤트 설정 시 해당 변수를 사용한다.

```javascript
    //  Some stars to collect, 12 in total, evenly spaced 70 pixels apart along the x axis
    stars = this.physics.add.group({
        key: 'star',
        repeat: 11,
        setXY: { x: 12, y: 0, stepX: 70 }
    });

    stars.children.iterate(function (child) {

        //  Give each star a slightly different bounce
        child.setBounceY(Phaser.Math.FloatBetween(0.4, 0.8));

    });

    bombs = this.physics.add.group();

    //  The score
    scoreText = this.add.text(16, 16, 'score: 0', { fontSize: '32px', fill: '#000' });
```

앞서 말했듯이 `this.physics.add.group` 를 통해 플레이어와 상호작용할 asset을 추가해준다. 이 때 동일한 asset("start")를 11번 추가하기 위해 위와 같이 작성해줬다.
또한 `stars.children.iterate` 함수를 통해 starts의 자식 요소들을 순차적으로 순회할 수 있는데, 위에서는 이를 통해 `.setBounceY` 설정을 추가해준다.
이 경우 각 "star"에 대해 0.4~0.8 사이의 랜덤한 값들을 추가해준다.

추후 상황에 따라 추가로 적용될 `bombs`와 `scoreText`를 추가해준다.

```javascript
    //  Collide the player and the stars with the platforms
    this.physics.add.collider(player, platforms);
    this.physics.add.collider(stars, platforms);
    this.physics.add.collider(bombs, platforms);

    //  Checks to see if the player overlaps with any of the stars, if he does call the collectStar function
    this.physics.add.overlap(player, stars, collectStar, null, this);

    this.physics.add.collider(player, bombs, hitBomb, null, this);
}
```

`.collider`는 작성한 두 요소에 대해 충돌 판정을 추가해준다. 즉 처음 작성되는 두 요소에 대해서는 충돌이 발생해, 위의 경우 player, stars, bombs는 platforms을 밟을 수 있게 해준다.
3번째는 콜백함수에 해당하는데, `this.physics.add.collider(player, bombs, hitBomb, null, this);` 는 player와 bombs가 충돌할 경우 `hitBomb` 함수를 발생시킨다.
4번째 인자인 `null` 은 조건에 따라 충돌 여부 판단하는 `processCallback`으로, `null`은 조건 없이 무조건 `callback`을 실행한다는 의미이다.
5번째 인자인 `this`는 `callbackContext`로 콜백함수의 적용 범위라고 한다.

`.overlap`은 충돌 판정이 아니라, 겹침 판정이다. 즉, player와 starts가 겹칠 경우에 대해 설정하는 것으로, 위 경우 `collectStar` 콜백함수가 발생하도록 작성해준다.

## hitBomb

```javascript
function hitBomb (player, bomb)
{
    this.physics.pause();

    player.setTint(0xff0000);

    player.anims.play('turn');

    gameOver = true;
}
```

플레이어 색상을 변경시켜주고, 애니메이션을 `turn`으로 바꿔주며, `gameOver` 값을 `true`로 변경해주는 콜백함수임을 알 수 있다.

## collectStar

```javascript
function collectStar (player, star)
{
    star.disableBody(true, true);

    //  Add and update the score
    score += 10;
    scoreText.setText('Score: ' + score);

    if (stars.countActive(true) === 0)
    {
        //  A new batch of stars to collect
        stars.children.iterate(function (child) {

            child.enableBody(true, child.x, 0, true, true);

        });

        var x = (player.x < 400) ? Phaser.Math.Between(400, 800) : Phaser.Math.Between(0, 400);

        var bomb = bombs.create(x, 16, 'bomb');
        bomb.setBounce(1);
        bomb.setCollideWorldBounds(true);
        bomb.setVelocity(Phaser.Math.Between(-200, 200), 20);
        bomb.allowGravity = false;

    }
}
```

player와 star가 겹칠 경우, 해당 star는 사라지고 score를 10점 올리며, 앞서 `scoreText`의 텍스트를 변경해준다.
이 때, `.disableBody(true, true)` 는 첫번째는 물리 속성 제거, 두번째는 렌더링 제거에 해당한다.

그리고 만약, 활성화된 star의 갯수가 0개가 된다면 모든 star를 다시 활성화 시켜준다.
또한 플레이어 기준 반대편에서 탄성있는 bomb를 하나 추가해준다. 이 때 `.setVelocity`를 통해 x좌표 이동 속도 및 y좌표 이동 속도를 설정해준다.
`.allowGravity`는 중력 적용은 안했는데, `.setVelocity`로 인해 중력 적용이 안되도 알아서 움직이게 되는 것을 볼 수 있다.

# update

```javascript
function update ()
{
    if (gameOver)
    {
        return;
    }

    if (cursors.left.isDown)
    {
        player.setVelocityX(-160);

        player.anims.play('left', true);
    }
    else if (cursors.right.isDown)
    {
        player.setVelocityX(160);

        player.anims.play('right', true);
    }
    else
    {
        player.setVelocityX(0);

        player.anims.play('turn');
    }

    if (cursors.up.isDown && player.body.touching.down)
    {
        player.setVelocityY(-330);
    }
}
```

`gameOver`가 될 경우, 키보드 조작이 불가능하도록 return을 통해 `update` 함수를 끝내는 것을 볼 수 있다.
`cursors.left.isDown`, `cursors.right.isDown`은 키보드의 좌측, 우측이 눌릴 경우에 대한 설정으로, 이 때 X좌표 이동 속도 및 어떤 애니메이션을 재생할 것인지 추가해준다.
else를 통해 아무런 키가 입력되지 않았을 경우 `turn` 애니메이션을 재생하며 x좌표 이동을 안 시켜주는 것을 볼 수 있다.
player가 점프하는 것을 추가했는데, 바닥에 닿아있을 때만 점프하도록 하기 위해 `(cursors.up.isDown && player.body.touching.down)` 를 함께 조건문으로 적용한 것을 볼 수 있다.