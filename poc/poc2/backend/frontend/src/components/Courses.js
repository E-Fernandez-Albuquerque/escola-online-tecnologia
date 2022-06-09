import React, { Component } from 'react'

export default class Courses extends Component {
    constructor(props) {
        super(props)
        this.state = {
            imageCourse: '../static/courses/coursesImages/485508.jpg',
            password: "",
        }
    }

    render() {
        return (
            <div className='image'>
                <img src={this.state.imageCourse}></img>
            </div>
        )
    }
}