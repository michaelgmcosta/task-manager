from .test_utils import AuthenticatedAPITest
from rest_framework import status


class TaskTest(AuthenticatedAPITest):
    
    def setUp(self):
        super().setUp()

    def create_task(self, **overrides):
        data = {
            "title": "task",
            "description": "test task",
            "completed": False
        }
        data.update(overrides)

        response = self.client.post("/api/tasks/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response

    def test_create_task(self):
        """
        Garante a criação de uma tarefa.
        """
        response = self.create_task()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        """
        Garante a atualização de uma tarefa.
        """
        task = self.create_task()
        response = self.client.patch(f"/api/tasks/{task.data["id"]}/", {
            "completed": True
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["completed"], True)

    def test_delete_task(self):
        """
        Garante a deleção de uma tarefa.
        """
        task = self.create_task()
        delete_response = self.client.delete(f"/api/tasks/{task.data["id"]}/")

        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_tasks(self):
        """
        Garante a obtenção de uma lista de tarefas.
        """
        self.create_task()
        self.create_task(title="another task")

        response = self.client.get("/api/tasks/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_task(self):
        """
        Garante a obtenção de uma tarefa por id.
        """
        task = self.create_task()

        response = self.client.get(f"/api/tasks/{task.data["id"]}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "task")

    