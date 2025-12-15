"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""
import datetime as dt
from typing import Union

class Homework:
    """
    The homework class.

    Attributes:
        text (str): The task name.
        deadline (datetime.timedelta): The deadline period.
        created (datetime.datetime): The creation timestamp.
    """
    text: str
    deadline: dt.timedelta
    created: dt.datetime

    def __init__(self, tasks: str, num_days: int):
        self.text = tasks
        self.deadline = dt.timedelta(days=num_days)
        self.created = dt.datetime.now()

    def is_active(self) -> bool:
        """Checks if the homework does not have an expired deadline."""

        if self.created + self.deadline < dt.datetime.now():
            return False

        return True

class Student():
    """
    The Student class.

    Attributes:
        last_name (str): The last name.
        first_name (str): The first name.
    """
    last_name: str
    first_name: str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework: Homework) -> Union[Homework, None]:
        """
        Request Homework object and returns it, if Homework is expired, 
        prints 'You are late' and returns None.
        """

        if homework.is_active():
            return homework

        # If the homework is not active then return None
        print('You are late')
        return None

class Teacher():
    """
    The Teacher class.

    Attributes:
        last_name (str): The last name.
        first_name (str): The first name.
    """
    last_name: str
    first_name: str

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(task_text: str, num_days: int) -> Homework:
        """Request task text and number of days to complete, returns Homework object."""

        return Homework(task_text, num_days)


if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    teacher.last_name  # Daniil
    student.first_name  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
