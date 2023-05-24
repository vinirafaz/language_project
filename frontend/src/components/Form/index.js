import React, { useState } from 'react';
import './Form.css';
import TextField from "../TextField";
import Button from "../Button";
import axios from 'axios';

const Form = (props) => {
    const [campo1, setCampo1] = useState('');
    const [campo2, setCampo2] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();

        const data = {
            username: campo1,
            password: campo2
        }

        axios.post('http://127.0.0.1:8000/api/v1/login', data)
            .then((response) => {
                console.log(response);
            })
            .catch((error) => {
                console.log(error);
            });

    }


    return (
        <section>
            <form onSubmit={handleSubmit} >
                <TextField label="Login" required={true} type="text" value={campo1} onChange={(event) => setCampo1(event.target.value) } />
                
                <TextField label="Senha" required={true} type="password" value={campo2} onChange={(event) => setCampo2(event.target.value)} />
                <Button label="Entrar" />
            </form>
        </section>
    )
}

export default Form;