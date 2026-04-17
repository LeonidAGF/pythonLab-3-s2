from typing import Iterator, Callable

from src.Source import TaskSource
from src.task import Task


class TaskQueue:
    """
        очередь задач
    """

    def __init__(self, source: TaskSource) -> None:
        """
            ункция для инициализации атрибутов
        """
        self.source: TaskSource = source

    def __iter__(self) -> Iterator[Task]:
        """
            функция для итерации по задачам из источника
        """

        for task in self.source.get_tasks():
            yield task

    def filtration(self, func: Callable[[Task], bool]) -> Iterator[Task]:
        """
            функция реализующая ленивый фильтр
        """
        for task in self:
            if func(task):
                yield task
