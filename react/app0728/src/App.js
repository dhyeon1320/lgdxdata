import logo from './logo.svg';
import './App.css';
import MyComponent from "./mycomponent";
import Sample from "./Sample";
import EventComponent from './EventComponent';

function App() {
  let msg = "자바스크립트 데이터"
  // if 사용 불가 - 삼항 연산자 사용
  let userid = undefined;

  let style = {
    backgroundColor: 'pink',
    color: 'aquamarine',
    fontSize: '48px'
  }
  return (
    <>
      {/* <h></h>
      <h1>Hello React</h1>
      <h2>안녕하세요</h2>
      <h1>msg</h1>     {/* {} 안 써서 msg라는 글자가 출력됨*/}
      {/*<h2>{msg}</h2>     {/*{} 써서 msg의 내용 출력됨*/}
      {/*<p>{userid ? userid : "로그인"}</p>
      <div style={style}>스타일 적용</div>*/}

      <MyComponent name = "Kim"/>
      <Sample age = "22" >샘플데이터</Sample>
      <EventComponent />

    </>
  );
}

export default App;
