import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { Link } from 'react-router-dom'
import axios from 'axios';
import "./Login.css";

const Forgot = () => {
    const [team_id, setTeamID] = useState("");
    const [message, setMessage] = useState("");
    const [color, setColor] = useState("red");

    function validateForm() {
        return team_id.length > 0;
    }

    function handleSubmit(event) {
        event.preventDefault();
        axios.get('./api/exists', {
            params: {
                username: team_id,
            }
        }).then((response) => {
            // console.log(response)
            if (response.data === "Use a browser"){
                setMessage('Use a browser. Using the command line is not allowed.')
                setColor("red")
            } if (response.data === "Exists") {
                setMessage("A reset link has been sent to this email.")
                setColor("green")
            } else if (response.data === "Too many requests") {
                setMessage('You have submitted too many requests. Try again in a few minutes.')
                setColor("red")
            } else {
                setMessage("This email does not exist in the database.")
                setColor("red")
            }
        });
    }

    return (
        <div className="Login">
            <div className = "center">
                <h2>Enter your team's username</h2>
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
                <Button block size="lg" type="submit" disabled={!validateForm()}>
                    Confirm
                </Button>
            </Form>
            <a href="/login">Return to login page</a>
        </div>
    );
}

export default Forgot;