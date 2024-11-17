## [Network] RESTful API 에 관해서
- **API** : Application Programming Interface, 프로그램 간 상호작용하기위한 규약
- **REST** : Representational State Transfer, 대규모 고성능 통신을 안정적으로 지원할 수 있다.
 - 특징
  1. Uniform : URI로 지정한 리소스에 대한 조작을 통일되고 한정적인 인터페이스로 수행하는 아키텍처 스타일
  2. Stateless : 무상태성으로, 작업을 위한 상태정보를 따로 저장하고 관리하지 않음
  3. Cacheable : 웹 기존 인프라를 그대로 사용가능하여, HTTP가 가진 캐싱 기능까지 적용 가능
  4. Self-descriptiveness : REST API 메시지만 보고도 쉽게 이해 가능한 '자체 표현 구조'
  5. Client-Server : REST 서버는 API 제공, 클라이언트는 사용자 인증 or 컨텍스트를 직접 관리하는 구조로 역할이 구분되어, 서로 간 의존성이 줄어들고 독립성 유지됨
  6. 계층형 구조 : 다중 계층으로 구성될 수 있으며 구조상 유연성을 둘 수도 있고, 네트워크 기반의 중간매체를 사용할 수 있게 함.
- **설계 과정**
 1. 자원 정의
 2. 행위 정의
 3. 표현 정의
 4. 상태 코드 정의
 5. API 문서화
- **요소**
 1. Resource : 자원, URI
   - 웹 상에 존재하는 데이터나 정보와 같은 모든 것, 명사 사용을 권장(하단의 설계 가이드 참고)
 2. Verb : 행위, HTTP Method
   - 자원에 대한 행위(조회, 생성, 수정, 삭제)를 의미
   a. **GET** : 자원 조회, URL 주소 끝에 파라미터로 포함되어 전송(query string)
        - 캐시 가능, 길이제한(브라우저에 따름), 보안문제(파라미터가 노출됨), 요청 시에만 사용
   b. **POST** : 자원 생성, HTTP 메시지 body에 데이터를 담아서 전송함
        - 캐시 불가, 길이제한 없음, 파라미터가 드러나지 않아 보안 필요 시 사용(암호화 안 할 경우 보안이 좋진 않음)
      - 보통 HTMl form 을 통해 서버로 전송됨
   c. **PUT** : 자원 수정
   d. **DELETE** : 자원 삭제
   e. **PATCH** : 자원 일부를 수정
   - GET 과 POST 의 차이 (출처:<https://noahlogs.tistory.com/35>)
      1. GET은 데이터 요청 시, POST는 새로 생성 혹은 업데이트 시 사용
      2. GET은 URL 파라미터에 데이터를 담아서 HTTP 메시지에 body가 없고, POST는 body에 데이터를 담기에 HTTP 메시지에 body가 있다.
      3. GET은 멱등이며, POST는 멱등이 아니다. | **멱등?** 연산을 여러번 적용해도 결과가 달라지지 않는 성질
   - PUT 과 PATCH 의 차이 : PUT은 '전체 리소스', PATCH는 '일부 리소스' 수정에 사용된다.
 3. Representations : 표현, 데이터 통신을 위해 주고받는 '데이터 형식(JSON, XML, HTML)'을 의미한다.
- **상태 코드(Status Code)** : 클라이언트에게 요청의 성공 또는 실패를 알려줌
- **API 문서화** : 클라이언트 개발자나 다른 개발자가 API를 쉽게 이해하고 사용하도록 문서화 필요

- 출처
 - <https://adjh54.tistory.com/150>
 - <https://aws.amazon.com/ko/what-is/restful-api/>
- 설계 가이드
 - <https://inpa.tistory.com/entry/WEB-🌐-REST-API-정리>
 - <https://velog.io/@couchcoding/개발-초보를-위한-RESTful-API-설계-가이드>
 - <https://sanghaklee.tistory.com/57>