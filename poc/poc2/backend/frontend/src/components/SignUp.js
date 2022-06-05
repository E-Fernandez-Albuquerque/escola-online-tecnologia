import React, { Component } from 'react'
import Menu from './Menu'
import { Button, TextField, Typography } from '@material-ui/core'



export default class SignUp extends Component {
    constructor(props) {
        super(props)
        this.state = {
            email: "",
            password: "",
        }
        this.handleEmail = this.handleEmail.bind(this)
        this.handlePswd = this.handlePswd.bind(this)
        this.signUpButtonClicked = this.signUpButtonClicked.bind(this)
    }



    render() {
        return (
            <div className='container-login'>
                <div className='login-image'>
                    <img src='../static/images/login.jpg'></img>
                </div>
                <div className='login-form'>
                    <Typography className='login-text' variant='h4' component='h4' align='center'>Crie a sua conta</Typography>
                    <TextField className="login-input" label='Email' placeholder='example@mail.com' value={this.state.email} variant='outlined' onChange={this.handleEmail}></TextField>
                    <TextField className="login-input" label='Senha' type="password" placeholder="Senha" value={this.state.password} variant='outlined' onChange={this.handlePswd}></TextField>
                    <Button className="login-button" variant='contained' color='primary' onClick={this.signUpButtonClicked}>Cadastrar</Button>
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

    signUpButtonClicked() {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              email: this.state.email,
              password: this.state.password,
            }),
          };
        fetch('/user/cadastro', requestOptions)
        .then(() => this.props.history.push('/'))
    }
}