## [Python] 파이썬이 싱글 스레드 언어인 이유
파이썬은 GIL, Global Interpreter Lock을 갖고 있어서, 여러 개의 스레드가 파이썬 바이트코드를 한번에 하나만 사용할 수 있게 락이 걸려있는 상태이다.
cpu는 동시에 하나의 코어만 사용하여 하나의 프로세스 내의 스레드를 처리하는데, GIL 로 인해 한번에 하나씩만 처리하는 것이다.
즉 멀티 태스킹에 가까운 파이썬의 구동 방식은 싱글 스레드 언어이다.

- 출처
  - <https://bloofer.net/114>
  - <https://frozenpond.tistory.com/124>

- [파이썬 멀티 스레드와 멀티 프로세스 구현](https://monkey3199.github.io/develop/python/2018/12/04/python-pararrel.html)
- [파이썬에서 GIL 삭제하겠다는 뉴스](https://www.itworld.co.kr/news/302737)