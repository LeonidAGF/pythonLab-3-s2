import random
from typing import Dict
from src.task import Task
from src.cat_function import cat


class SourceFromFile:
    """
        Источник задач из файла
    """

    def __init__(self, path: str, seed=None) -> None:
        """
            Инициализатор для источника задач из файла
        """
        self.path = path
        self.seed = seed

    def get_tasks(self) -> list[Task] | None:
        """
            функция получения задач
        """
        tasks: list[Task] = []
        random.seed(None)
        if self.seed is not None:
            random.seed(self.seed)
        try:
            data: Dict[str, str] = {}
            data["text"] = cat(self.path)
            task: Task = Task(random.randint(10000, 99999),'description', data,random.randint(1, 2))
            tasks.append(task)
            random.seed(None)
            return tasks
        except Exception:
            random.seed(None)
            return None
