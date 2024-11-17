## [Front] 리액트의 라이프사이클에 대해서 알고 있는지
- **가상 DOM**
 실제 DOM의 가벼운 복사본으로, 리액트는 컴포넌트 상태가 변경될 때 최소한의 DOM 업데이트만 수행하여 애플리케이션의 성능을 크게 향상시킴
- **리액트 컴포넌트 라이프사이클**
 컴포넌트의 생성부터 소멸까지의 과정으로, 이걸 이해해야 컴포넌트 상태 관리 및 리렌더링을 효율적으로 할 수 있다.
 크게 마운팅, 업데이터, 언마운팅 단계로 나눌 수 있으며, 다양한 라이프사이클 메소드를 사용할 수 있다.
- 이미지 : <https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/>

1. **마운트** : 컴포넌트 처음 실행 시 생성단계를 마운트(Mount)라고 표현
 - constructor : 컴포넌트 생성자 메소드. state 와 props를 접근해서 값을 할당 할 수 있다.
 - getDerivedStateFromProps : props로 받아온 것을 state에 설정하고 싶을 때 사용
    최초 마운트 시와 갱신 시 render 메서드를 호출하기 직전에 호출됨. null 반환 시 아무 것도 갱신하지 않음
 - render : 컴포넌트를 렌더링 해주는 메서드로, 클래스 컴포넌트에서 구현돼야하는 유일한 메서드
 - componentDidMount : DOM에 접근하여 사용 가능, AJAX 요청 및 DOM에 속성을 읽거나 변경하는 작업 진행
    첫번째 렌더링이 된 직후 호출되는 메서드로, 이 시점에 화면이 구현되어 있는 상태
2. **업데이트** : 컴포넌트의 업데이트에 사용됨.
 - getDerivedStateFromProps : 업데이트 시에도 render 전에 메서드가 실행 됨.
 - shouldComponentUpdate : 컴포넌트를 리렌더링 할지 결정하는 메서드. props 또는 state가 새로운 값으로 갱신되어 렌더링 발생하기 직전에 호출됨.
    기본값은 true로 return false를 하면 render를 취소할수 있다. (성능최적화 용도)
 - render : 마운트 때와 동일
 - getSnapshotBeforeUpdate : 가장 마지막 렌더링된 결과가 DOM에 반영되기 전에 호출되며, DOM 상태 변경 되기 전 값을 반환하여 componentDidUpdate 에서 인자로 받아서 사용 가능
 - componentDidUpdate : 갱신이 일어난직후 호출되며, 최초 렌더링에서는 호출되지 않는다.
3. **언마운트** : 컴포넌트가 화면에서 제거되는 것을 의미
 - componentWillUnmount : 컴포넌트가 사라지기 직전에 호출하고, DOM에 등록했던 이벤트들을 제거해주는 용도로 주로 사용

- 출처
 - [리액트의 핵심](https://f-lab.kr/insight/react-core-concepts?gad_source=1&gclid=Cj0KCQjwn9y1BhC2ARIsAG5IY-6fYBVVKkyERp30alu04q0H_CwPbiQe1XRdfxuD2rFRC08P1LuDUVYaAogQEALw_wcB)
 - [React 컴포넌트의 생명 주기](https://shape-coding.tistory.com/entry/React-React-컴포넌트의-생명-주기-Life-Cycle)

- 참고할만한 자료
 - [Hook 에 관한 추가 설명](https://velog.io/@minbr0ther/React.js-리액트-라이프사이클life-cycle-순서-역할)
 - <https://ko.legacy.reactjs.org/docs/state-and-lifecycle.html>