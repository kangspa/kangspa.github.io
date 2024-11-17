## [DevOps] CI/CD 의 파이프라인
- CI : Continuous Integration, 지속적 통합
  코드 변경 사항을 공유 소스 코드 레포지토리에 자동으로 자주 통합하는 사례
- CD : Continuous Delivery/Deployment, 지속적 제공/배포
  코드 변경 사항의 통합, 테스트, 제공을 나타내는 프로세스

→ 소프트웨어 개발 라이프사이클을 간소화 가속화 하여 배포를 자동화하는 것

- **파이프라인**
  1. 소스 코드 빌드
  2. 테스트
  3. 코드 통합
  4. 레포지토리에 릴리즈
  5. 소프트웨어 배포
  6. 규정 준수 및 유효성 검사
  이 중 1~3은 지속적 통합, 4는 지속적 제공, 5는 지속적 배포에 속한다.

- 간단하게 ①소스 단계 ②빌드 단계 ③배포단계 로 3가지 단계로 나누기도 한다.

- 출처
  - <https://www.redhat.com/ko/topics/devops/what-is-ci-cd>
  - <https://velog.io/@edith_0318/CICD-파이프라인>