import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";
import { Grid, Button, ButtonGroup, Typography } from '@material-ui/core'
import Menu from "./Menu";
import Login from "./Login";
import About from "./About";
import Courses from "./Courses";
import SignUp from "./SignUp";

export default class HomePage extends Component {
    constructor(props) {
        super(props)
    }

    renderHomePage() {
        return (
            <Grid container spacing={3}>
                <Grid item xs={12} align='center'>
                    <Typography variant='h3' component='h3'>
                        Escola online de tecnologia
                    </Typography>
                </Grid>
            </Grid>
        )
    }

    render() {
        return (
            <>
                <Menu></Menu>
                <Router>
                    <Switch>
                        <Route exact path="/" render={() => {
                            return this.renderHomePage()
                        }}></Route>
                        <Route path="/quem-somos" component={About}></Route>
                        <Route path="/login" component={Login}></Route>
                        <Route path="/cursos" component={Courses}></Route>
                        <Route path='/cadastro' component={SignUp}></Route>
                    </Switch>
                </Router>
            </>


        );
    }
}