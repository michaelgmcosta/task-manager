import { useState } from "react"
import { login } from "../services/auth";

export const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        await login(username, password);
        window.location.href = "/tasks";
    };

    return (
        <div>
            <h2>Login</h2>
            <input 
                placeholder="Usuário"
                onChange={e => setUsername(e.target.value)}
            />
            <input 
                type="password"
                placeholder="Senha"
                onChange={e => setPassword(e.target.value)}
            />
            <button onClick={handleLogin}>Entrar</button>
        </div>
    );
}