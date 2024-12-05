---
title: "스레드와 프로세스 차이"
tags:
    - 스레드
    - 프로세스
date: "2024-11-28"
thumbnail: "https://velog.velcdn.com/images%2Fraejoonee%2Fpost%2Fb91490ed-c67b-407d-8fea-a8d6fdb22559%2F104.png"
---
<a style="font-size:0.9rem" href="https://velog.io/@raejoonee/프로세스와-스레드의-차이">- 출처 : 프로세스와 스레드의 차이</a>

### 프로세스
운영체제에서 생성되며, 메모리에 적재되어 실행되는 프로그램.

### 스레드
프로그램 하나가 프로세스 하나만 가지고 사용하기는 어려운만큼, 여러 개의 작업을 실행하기 위해 제안된 더 작은 개념.
프로세스의 코드에 정의된 절차에 따라 실행되는 특정한 수행 경로로, 스레드 간 메모리를 공유하며 작동한다.

## 차이점
**프로세스**는 하나가 강제 종료되도 다른 프로세스에 아무런 영향을 주지 않는다. (공유된 파일이 손상된 경우 제외)
**스레드**는 별도의 Stack을 사용하지만, Code/Data/Heap 메모리 영역은 공유하므로, 하나가 강제 종료되면 같은 프로세스 내의 모든 스레드가 강제 종료된다.

### 멀티 스레드와 멀티 프로세스?
- **멀티 스레드**
    단일 프로세스에 여러 스레드가 포함되는 경우로, 동일 메모리를 공유한다.
    적은 메모리와 적은 CPU 점유시간, 낮은 Context Switching 비용
- **멀티 프로세스**
    자체 메모리를 갖는 여러 프로세스가 사용하여 안정성이 높다.
    많은 메모리와 많은 CPU 점유시간, 느린 Context Switching
    → 안정성을 높이려면 멀티 프로세스를, Context Switching이 많고 빠른 처리 요구 시 멀티 스레드를 추천

- Context Switching 이란?
    문맥교환이라고도 하며, cpu가 실행하는 작업을 변경하는 것을 말함

- 출처
  - <https://velog.io/@raejoonee/프로세스와-스레드의-차이>
  - <https://somaz.tistory.com/265>
  - <https://frozenpond.tistory.com/124>