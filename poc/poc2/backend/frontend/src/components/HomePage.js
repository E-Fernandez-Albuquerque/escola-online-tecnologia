import React, { Component } from "react";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";
import { Grid, Button, ButtonGroup, Typography } from '@material-ui/core'
import Menu from "./Menu";
import MaisUmaPagina from "./MaisUmaPagina";


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
                        <Route path="/nova" component={MaisUmaPagina}></Route>
                    </Switch>
                </Router>
            </>


        );
    }
}