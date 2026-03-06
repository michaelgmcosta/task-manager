import type { Task } from "../types/task"

interface Props {
    tasks: Task[]
}

export const TaskList = ({tasks}: Props) => {
    return (
        <ul>
            {tasks.map(task => (
                <li key={task.id}>
                    {task.created_at} | {task.title} - {"Completed: "}{task.completed ? "✔" : "❌"}
                </li>
            ))}
        </ul>
    );
};