---
title: 전략 패턴의 의미와 사용하는 상황
tags:
    - 디자인패턴
    - 전략패턴
date: "2024-12-04"
thumbnail: "https://refactoring.guru/images/patterns/content/strategy/strategy.png"
---
<a style="font-size:0.9rem" href="https://refactoring.guru/ko/design-patterns/strategy">- 출처 : refactoring.guru</a>

객체의 행위를 바꾸고 싶은 경우, '직접' 수정하지 않고 '캡슐화한 알고리즘'을 컨텍스트 안에서 바꿔주면서 상호 교체가 가능하게 만드는 패턴.

- 사용하는 상황
    - 알고리즘이 여러 버전 또는 변형이 필요할 때 클래스화를 통해 관리
    - 알고리즘 코드가 노출되면 안되는 데이터에 액세스 하거나 데이터를 활용할 때 (캡슐화)
    - 알고리즘 동작이 런타임에 실시간으로 교체 되어야 할 때

- 출처 : <https://inpa.tistory.com/entry/GOF-💠-전략Strategy-패턴-제대로-배워보자>