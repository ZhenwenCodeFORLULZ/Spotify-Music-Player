import React, {Component} from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
export default class App extends Component{
    constructor(props){
        super(props);
        this.state = {

        }
    }
    render(){
        //return <h1>{this.props.name}</h1>
        return (
        <div>
        <HomePage/>
        </div>
        );
        
    }
}

const appDiv = document.getElementById("app")
render(<App/>, appDiv)