from typing import Iterator, Callable, Any

from Source import TaskSource
from task import Task


class TaskQueue:
    """

    """

    def __init__(self, source: TaskSource) -> None:
        """

        """
        self.source: TaskSource = source

    def __iter__(self) -> Iterator[Task]:
        """

        """

        for task in self.source.get_tasks():
            yield task

    def filtration(self, func: Callable[[Task], bool]) -> Iterator[Task]:
        """

        """
        for task in self:
            if func(task):
                yield task
