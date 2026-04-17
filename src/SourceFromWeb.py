from src.client import ClientBase
from src.task import Task
import random


class SourceFromWeb:
    """
        Источник задач из интернета
    """

    def __init__(self, client: ClientBase, seed=None) -> None:
        """
            Инициализатор источника задач из интернета
        """
        self.client = client
        self.seed = seed

    def get_tasks(self) -> list[Task] | None:
        """
            Функция получения задач из интернета
        """

        random.seed(None)
        if self.seed is not None:
            random.seed(self.seed)

        try:
            tasks: list[Task] = []
            if isinstance(self.client, ClientBase):
                for col in range(0, random.randint(1, 3)):
                    el: Task = self.client.get_task()
                    tasks.append(el)
            else:
                raise TypeError
            random.seed(None)
            return tasks
        except Exception:
            random.seed(None)
            return None
