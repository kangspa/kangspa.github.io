---
title: 로드밸런서의 역할
tags:
    - 로드밸런서
    - 분산 부하
    - AWS
date: "2024-12-01"
thumbnail: "https://post-phinf.pstatic.net/MjAxOTEyMTBfMjE3/MDAxNTc1OTU0ODk1ODQ3.-GJxkoK7Apn4l0K5L1OXN4NFGsseRoaNhW2r0KIQJdog.0BchcWEI-WS-uEb3iRRrD0JyO_6eZoIWh7xf4f4J2fMg.JPEG/%EB%A1%9C%EB%93%9C%EB%B0%B8%EB%9F%B0%EC%84%9C_%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98.jpg?type=w1200"
---
<a style="font-size:0.9rem" href="https://m.post.naver.com/viewer/postView.naver?volumeNo=27046347&memberNo=2521903">- 출처 : 로드밸런서(Load Balancer)의 개념과 특징</a

로드밸런서란, 서버에 가해지는 부하를 분산해주는 장치 또는 기술을 통칭하는 말이다.
클라이언트와 서버풀(Server Pool, 분산 네트워크를 구성하는 서버들의 그룹) 사이에 위치한다.

- 증가한 트래픽에 대처하는 2가지 방법, **Scale-up & Scale-out**
    - Scale-up : 서버 자체 성능을 확장하는 것
    - Scale-out : 기존 서버와 동일 or 낮은 성능 서버를 증설하여 운영 -> 이 때 로드밸런싱이 필요!

## 로드밸런싱 알고리즘 종류
- Round Robin Method : 서버에 들어온 요청을 순서대로 돌아가며 배정
- Weighted Round Robin Method : 각각의 서버에 가중치를 매기고 가중치 높은 서버에 클라이언트 요청 우선 배분
- IP Hash Method : 클라이언트의 IP 주소를 특정 서버로 매핑하여 요청을 처리하는 방식
- Least Connection Method : 요청이 들어온 시점에 가장 적은 연결상태를 보이는 서버에 우선 트래픽 배분
- Least Response Time Method : 서버의 현재 연결 상태와 응답시간을 모두 고려하여 트래픽 배분

## L4 로드밸런서 & L7 로드밸런서
- 부하 분산에 가장 많이 활용되는 2 종류
- L4 로드밸런서부터 포트 정보를 바탕으로 로드를 분산하는 것이 가능하다!
- **L4 로드밸런서** : 네트워크 계층(IP, IPX), 트랜스포트 계층(TCP, UDP)의 정보를 바탕으로 로드를 분산하여, IP 주소나 포트번호, MAC주소, 전송 프로토콜에 따라 트래픽 나누는 것이 가능!
- **L7 로드밸런서** : 애플리케이션 계층(HTTP, FTP, SMTP)에서 로드를 분산하기 때문에 HTTP 헤더, 쿠키 등과 같은 사용자의 요청을 기준으로 특정 서버에 트래픽 분산하는 것이 가능

## API 게이트웨이와 차이점
- API 게이트웨이
    - 클라이언트의 요청을 적절한 내부 서비스로 라우팅하는 역할을 함.
    - API 관리와 라우팅에 초점을 맞춤. -> 요청을 적절한 서비스로 라우팅하는 역할이기 때문!
    - 인증, 인가, 요청 변환 등의 추가적 기능을 제공 -> JWT 토큰을 사용하여 사용자 인증 처리 가능!
- 반면 로드밸런서는 트래픽 분산과 서버 부하관리에 중점을 두기에 추가적인 기능은 제공하지 않는다.

---

- 출처 및 참고
    - [로드밸런서의 개념과 특징](https://m.post.naver.com/viewer/postView.naver?volumeNo=27046347&memberNo=2521903)
    - [로드 밸런싱이란 무엇인가요?](https://aws.amazon.com/ko/what-is/load-balancing/)
    - [API 게이트웨이와 로드 밸런서의 역할과 차이점](https://f-lab.kr/insight/api-gateway-and-load-balancer)