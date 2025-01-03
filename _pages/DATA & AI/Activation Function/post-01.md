---
title: "ReLU 함수에 대해"
tags:
   - ReLU
   - 활성함수
date: "2024-11-26"
thumbnail: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/ReLU_and_GELU.svg/220px-ReLU_and_GELU.svg.png"
---
<a style="font-size:0.9rem" href="https://en.wikipedia.org/wiki/Rectifier_(neural_networks)">- 출처 : Rectifier (neural networks)</a>

***"0보다 클 경우 입력을 그대로 출력하고, 0이하일 경우 0을 출력하는 비선형 함수 (max(0, x))"***
계산 효율성이 높고 모델 학습 시간을 단축시키는데 도움이 된다.

### 탄생 배경
Sigmoid 사용 시, 기울기 최대가 0.25 라서, 값이 점점 작아지며 0에 가깝게 수렴하면 기울기 소실 문제(Vanishing Gradient problem)이 발생한다. 이를 방지하고자 만들어진 함수이다.

### 장점
1. 비선형성
    신경망이 복잡한 문제를 줄여준다.
2. 계산효율성
    단순 형태로 인해 계산 부담이 적고, 이로인해 학습이 빠르다. (tanh 대비 6배 빠름)
3. 기울기 소실 문제 완화
    0보다 큰 값은 그대로 출력해줌으로써 기울기 소실문제를 완화시켜준다.
4. 희소성
    0 이하 입력은 0을 출력함으로써 신경망의 희소성을 증가시킨다. (모델 일반화 능력 향상)

### 단점
**죽은 ReLU 문제** : 0 이하 입력에 대해 항상 0을 출력함으로써 일부 뉴런이 활성화되지 않는 문제 발생 가능성이 있다.

---

- 출처
  - <https://datasciencebeehive.tistory.com/102>
  - <https://velog.io/@lighthouse97/기울기-소실-문제와-ReLU-함수>