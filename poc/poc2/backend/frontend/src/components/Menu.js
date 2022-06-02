import { Button } from "@material-ui/core";
import React, { Component } from "react";

export default class Menu extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div className="menu">
                <div></div>
                <div className="center">
                    <div><a className="menu-item" href="/">Home</a></div>
                    <div><a className="menu-item" href='/nova'>Cursos</a></div>
                    <div><a className="menu-item">Quem somos</a></div>
                </div>
                <div className="login">
                    <Button variant='contained' color='primary'>Login</Button>
                </div>
            </div>
        );
    }
}