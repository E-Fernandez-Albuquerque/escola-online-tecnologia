import React, { Component } from 'react'
import Menu from './Menu'
import { Button, TextField, Typography } from '@material-ui/core'



export default class Login extends Component {
    constructor(props) {
        super(props)
        this.state = {
            email: "",
            password: "",
        }
        this.handleEmail = this.handleEmail.bind(this)
        this.handlePswd = this.handlePswd.bind(this)
        this.loginButtonClicked = this.loginButtonClicked.bind(this)
    }



    render() {
        return (
            <div className='container-login'>
                <div className='login-image'>
                    <img src='../static/images/login.jpg'></img>
                </div>
                <div className='login-form'>
                    <Typography className='login-text' variant='h4' component='h4' align='center'>Acessando o mundo da <b>Tecnologia</b></Typography>
                    <TextField className="login-input" label='Email' placeholder='example@mail.com' value={this.state.email} variant='outlined' onChange={this.handleEmail}></TextField>
                    <TextField className="login-input" label='Senha' type="password" placeholder="Senha" value={this.state.password} variant='outlined' onChange={this.handlePswd}></TextField>
                    <Button className="login-button" variant='contained' color='primary' onClick={this.loginButtonClicked}>Login</Button>
                    <a id='signup' href='/cadastro'>Sem conta? Cadastre-se aqui!</a>
                </div>
            </div>

        )
    }

    handleEmail(e) {
        this.setState({
            email: e.target.value
        })
    }

    handlePswd(e) {
        this.setState({
            password: e.target.value
        })
    }

    loginButtonClicked() {
        fetch('/user/login')
        .then((response) => response.json())
        .then(console.log(this.state))
    }
}