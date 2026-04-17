from typing import Iterator

from Source import TaskSource
from task import Task


class TaskQueue:
    """

    """

    def __init__(self, source: TaskSource,status:str='none',priopity:int = 0) -> None:
        """

        """
        self.source: TaskSource = source
        self.status = status
        self.priopity = priopity

    def __iter__(self) -> Iterator[Task]:
        """

        """

        for task in self.source.get_tasks():
           filtered:int = 1
           if (self.status!=task.status and self.status!='none') or (self.priopity!=task.priority and self.priopity!=0):
               filtered = 0
           if filtered==1:
                yield task