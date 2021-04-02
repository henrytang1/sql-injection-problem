import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { Link } from 'react-router-dom'
import axios from 'axios';
import "./Login.css";

const Login = () => {
    const [team_id, setTeamID] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const [color, setColor] = useState("red");

    function validateForm() {
        return team_id.length > 0 && password.length > 0;
    }

    function handleSubmit(event) {
        event.preventDefault();
        axios.get('./api/login', {
                params: {
                    username: team_id,
                    password: password,
                }
            }).then((response) => {
                console.log(response)
                if (response.data === "Too many requests") {
                    setMessage('You have submitted too many requests. Try again in a few minutes.')
                    setColor("red")
                } else if (response.data === "Not Correct") {
                    setMessage('Your lucky code is '+ response.data)
                    setColor("green")
                } else {
                    setMessage("Incorrect Credentials")
                    setColor("red")
                }
            });
    }

    return (
        <div className="Login">
            <div className = "center">
                <h2>Login</h2>
                <p style={{color: color}}> {message} </p>
            </div>
            <Form onSubmit={handleSubmit}>
                <Form.Group size="lg" controlId="team_id">
                    <Form.Label>Team ID</Form.Label>
                    <Form.Control
                        autoFocus
                        value={team_id}
                        onChange={(e) => setTeamID(e.target.value)}
                    />
                </Form.Group>
                <Form.Group size="lg" controlId="password">
                    <Form.Label>Password</Form.Label>
                    <Form.Control
                        type="password"
                        value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    />
                </Form.Group>
                <Button block size="lg" type="submit" disabled={!validateForm()}>
                    Login
                </Button>
            </Form>
            <a href="/forgot">Forgot my password</a>
        </div>
    );
}

export default Login;