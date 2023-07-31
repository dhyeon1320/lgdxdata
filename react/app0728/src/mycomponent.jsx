import React, {Component} from "react";

class MyComponent extends Component{
    render(){
        return(
            <div>성은 {this.props.name}이다.</div>
        )
    }
}

export default MyComponent