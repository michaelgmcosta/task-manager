import './App.css'
import { Login } from './pages/Login'
import { Tasks } from './pages/Tasks'
import { useAuth } from './hooks/userAuth'
import { Navigate, Route, Routes } from 'react-router-dom';

function App() {
  const {isAuthenticated} = useAuth();

  return (
    <Routes>
      <Route path="/login" element={<Login/>}/>
      <Route path="/tasks" element={isAuthenticated ? <Tasks/> : <Navigate to={"/login"} />}/>
      <Route path="*" element={<Navigate to={"/tasks"} />}/>
    </Routes>
  )
}

export default App;
