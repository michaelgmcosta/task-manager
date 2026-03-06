import { api } from "./api";

export const login = async (username: string, password: string) => {
    const response = await api.post("/auth/login/", {
        username,
        password
    })

    localStorage.setItem("access", response.data.access)
    localStorage.setItem("refresh", response.data.refresh)
}