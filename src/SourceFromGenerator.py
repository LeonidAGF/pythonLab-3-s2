import random
from typing import Dict
from src.task import Task
from src.generator import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array


class SourceFromGenerator:
    """
        Источник задач из генераоров массивов
    """

    def __init__(self, type: int, seed=None) -> None:
        """
            Инициализатор источника задач из файлов
        """
        if type < 1 or type > 5:
            raise Exception
        self.type = type
        self.seed = seed

    def get_tasks(self) -> list[Task] | None:
        """
            Функция получения задач из генераторов
        """

        random.seed(None)
        if self.seed is not None:
            random.seed(self.seed)

        tasks: list[Task] = []

        for col in range(0, random.randint(2, 10)):

            data: Dict[str, list] = {}
            match self.type:
                case 1:
                    data["numbers"] = rand_int_array(random.randint(5, 20), 1, 50)
                case 2:
                    data["numbers"] = nearly_sorted(random.randint(5, 20), 5)
                case 3:
                    data["numbers"] = many_duplicates(random.randint(5, 20))
                case 4:
                    data["numbers"] = reverse_sorted(random.randint(5, 20))
                case 5:
                    data["numbers"] = rand_float_array(random.randint(5, 20))

            el: Task = Task(random.randint(10000, 99999),'description', data,random.randint(1, 2))
            tasks.append(el)

        random.seed(None)
        return tasks
