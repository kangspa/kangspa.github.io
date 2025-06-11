---
title: "SpriteSheet 활용에 사용된 cv2 함수 알아보기"
tags:
    - spritesheet
    - cv2
    - 이미지처리
date: "2025-06-11"
thumbnail: "/assets/img/DATA & AI/Computer Vision/post-01/thumbnail.png"
---

`phaser`를 활용해서 게임을 만드려는데, 무료로 구한 스프라이트 시트가 로드가 잘 되지 않았다. 프레임별 사이즈가 다르거나 space가 잘 맞지 않는 등 문제가 있어, 필요한 프레임만 추출해서 사용하기 위해 파이썬으로 스프라이트 시트를 다루는 모듈을 만들어보았다.
상세 내용은 [Github의 sprite-sheet](https://github.com/kangspa/sprite-sheet)에 `README`로 작성해둬서, 말 그대로 cv2로 사용한 함수 등에 대해 어떤 식으로 작동하는지 정리했다.

# cv2.imread

```python
img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
```
이미지를 읽어들일 때 사용한다. 이 때 `cv2.IMREAD_UNCHANGED`는 이미지를 변환없이 그대로 읽어들이는데, 투명도까지 있는 png 이미지 등을 읽어들일 때 사용한다.

# cv2.rectangle

```python
cv2.rectangle(img, (x, y), (x2, y2), (0, 255, 0), 2)
```

이미지 위에 네모난 상자를 그려준다.
`(x, y)`는 네모 중 좌측 상단 좌표, `(x2, y2)`는 네모 중 우측 상단 좌표이다.
4번째 인자인 `(0, 255, 0)`는 네모의 색상값, 5번째 인자는 선의 두께이다.

# cv2.distanceTransform

```python
dist_transform = cv2.distanceTransform(mask, cv2.DIST_L2, 5)
```

이미지에서 각 물체 간 거리를 계산할 때 사용되는 함수이다.
입력되는 `mask`는 이진 이미지로, 배경은 0, 배경이 아닌 물체는 255로 이진화되어야 한다.
이후 255 픽셀 간 거리가 입력된 이미지(2차원 배열)를 return해준다.

두번째 인자는 거리 계산 방식으로, 입력 값은 아래와 같다.

- `cv2.DIST_L1` – 맨하탄 거리 (Manhattan)
- `cv2.DIST_L2` – 유클리드 거리 (Euclidean)
- `cv2.DIST_C` – 첼비셰프 거리 (Chessboard)

세번째 인자는 거리 계산에 사용할 마스크의 크기로, 3, 5, `cv2.DIST_MASK_PRECISE` 중 하나를 입력해서 사용한다.

# cv2.findContours

```python
contours, _ = cv2.findContours(object_region, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

이미지에서 컨투어(윤곽선, 테두리)를 검출하는 함수이다.
입력되는 이미지는 이진화 이미지여야한다.
두번째 인자인 `cv2.RETR_EXTERNAL`을 통해, 외곽선을 추출하여 주로 해당 값만 사용한다.

세번째 인자는 외곽선 좌표값들을 어떻게 추출할 것인지에 대한 기준값으로, 아래와 같다.
- `cv2.CHAIN_APPROX_NONE`: 모든 점들을 전부 저장
- `cv2.CHAIN_APPROX_SIMPLE`: 수평, 수직, 대각선 선분은 양 끝점만 저장.

해당 함수를 통한 `return` 값은 `contours`, `hierarchy` 2가지로, 외곽선 정보만 추출해서 사용할 때는 `contours`만 유의미하게 사용하면 된다.

## cv2.boundingRect

```python
x, y, w, h = cv2.boundingRect(contour)
```

입력한 컨투어 값에 축에 정렬된 형태로 접하는 사각형(AABB)에 대한 정보값을 x, y, w, h 형태로 return 해준다.

## cv2.minAreaRect

```python
(center_x, center_y), (width, height), angle = cv2.minAreaRect(contour)
```

입력한 컨투어 값에 최소 외접하는 사각형(OBB)에 대한 정보값을 (center_x, center_y), (width, height), angle 형태로 return 해준다.
해당 프로젝트에서 사용되진 않았으나, 컨투어로 사각형 좌표값 추출 시 사용되는 함수 중 하나라 함께 첨부한다.

# cv2.inRange

```python
mask = cv2.inRange(image, background_color, background_color)
```

이미지 내에서 특정 범위 내의 값은 255로, 나머지는 0으로 반환해주는 함수이다.
두번째 인자가 최소 임계값, 세번째 인자가 최대 임계값에 해당된다.
위의 예제는 이미지 내에서 배경색에 해당되는 부분은 전부 255로, 나머지(오브젝트)는 0으로 변경해주는 방식으로 진행된다.

입력하는 색상의 형태는 image의 채널값과 일치해야한다.

# cv2.bitwise_not

```python
object_mask = cv2.bitwise_not(mask)
```

이미지 내에서 0과 255 픽셀 값을 반전시켜준다.