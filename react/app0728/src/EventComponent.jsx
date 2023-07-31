import React, {Component} from "react";

class EventComponent extends Component{
    //content라는 state 생성
    state = {
        content:''
    };

    render(){
        return(
            <div>
                <h1>이벤트 연습</h1>
                <input type = "text"
                onChange = {
                    (e) => {
                        console.log(e.target.value)
                        this.setState({content:e.target.value})
                        console.log(this.state)
                    }
                }/>
            </div>
        )

    }
}

export default EventComponent;