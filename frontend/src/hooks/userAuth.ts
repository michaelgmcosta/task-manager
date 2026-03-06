export const useAuth = () => {
    const isAuthenticated = !!localStorage.getItem("access");

    const logout = () => {
        localStorage.clear();
        window.location.href = "/";
    };

    return { isAuthenticated, logout };
}