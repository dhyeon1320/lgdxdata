function Sample(props){
    // JavaScript의 구조 분해 할당
    // = 오른쪽에 객체 설정하고 왼쪽에서 {}안에 변수 설정하면 변수 이름과 동일한 객체 속성이 나눠서 대입됨
    const {age, children} = props;
    return(
        <>
            <div>함수형 컴포넌트 시작</div>
            <div>나이는 {age} 태그 내용은{children}</div>
            <div>함수형 컴포넌트 끝</div>
        </>
    )
}
export default Sample;