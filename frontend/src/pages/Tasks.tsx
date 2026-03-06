import { useEffect, useState } from "react";
import { api } from "../services/api";
import type { Task } from "../types/task";
import { TaskList } from "../components/TasksList";

export const Tasks = () => {
    const [tasks, setTasks] = useState<Task[]>([]);

    useEffect(() => {
        api.get("/tasks/").then(res => setTasks(res.data));
    }, []);

    return (
        <div>
            <h2>Minhas Tarefas</h2>
            <TaskList tasks={tasks}/>
        </div>
    )
}