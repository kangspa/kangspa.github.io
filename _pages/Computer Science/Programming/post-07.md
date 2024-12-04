---
title: 팩토리 패턴의 의미와 장점
tags:
    - 디자인패턴
    - 팩토리패턴
date: "2024-12-04"
thumbnail: "https://refactoring.guru/images/patterns/content/factory-method/factory-method-ko.png"
---
<a style="font-size:0.9rem" href="https://refactoring.guru/ko/design-patterns/factory-method">- 출처 : refactoring.guru</a>

객체를 사용하는 코드에서 객체 생성 부분을 떼어내 추상화한 패턴.   
상속 관계에 있는 두 클래스에서 상위 클래스는 뼈대를, 하위 클래스에서 구체적 내용을 결정하는 패턴.

- 장점
    1. 생성자와 객체 간 강한 결합을 피할 수 있다.
    2. 캡슐화, 추상화를 통해 생성 객체의 구체적 타입을 감출 수 있다.
    3. 단일 책임 원칙 준수 : 객체 생성 코드를 한 곳에서 진행하여 코드 유지보수가 쉽다.
    4. 개방/폐쇄 원칙 준수 : 기존 코드를 수정하지 않고 새로운 유형의 제품 인스턴스를 프로그램에 도입할 수 있어 원칙을 만족한다.
    5. 유연성 : 상위 클래스에서는 인스턴스 생성 방식에 대해 전혀 알 필요가 없다.

- 출처 : <https://inpa.tistory.com/entry/GOF-💠-팩토리-메서드Factory-Method-패턴-제대로-배워보자>