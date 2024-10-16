import React ,{Component} from "react";
import {render} from "react-dom";

export default class App extends Component {
    constructor(props) {
        super(props);
        }
        render() {
            return (
                <div>
                    <h1>Hello, World!</h1>
                    <p>This is a React App</p>
                </div>
            );
        }
}

const appDiv = document.getElementById('app');
render(<App/>, appDiv);