"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import datetime as dt
import pytest
from python_part_2.task_clases import Teacher, Student, Homework, main as task_classes_main


def test_teacher_instance():
    """Test the creation of the Teacher object"""

    teacher = Teacher('Dmitry', 'Orlyakov')

    assert teacher.first_name == 'Dmitry'
    assert teacher.last_name == 'Orlyakov'


def test_student_instance():
    """Test the creation of the Student object"""

    student = Student('Vladislav', 'Popov')

    assert student.first_name == 'Vladislav'
    assert student.last_name == 'Popov'


def test_homework_instance():
    """Test the creation of the Homework object"""
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')

    # Test direct instantiation
    homework = Homework("Learn Python homework", 20)
    assert homework.text == 'Learn Python homework'
    assert homework.deadline == dt.timedelta(days=20)

    # Test instantiation via static method
    homework = Teacher.create_homework('Learn functions homework', 10)
    assert homework.text == 'Learn functions homework'
    assert homework.deadline == dt.timedelta(days=10)

    # Test instantiation via object reference
    homework = teacher.create_homework('Learn integrals homework', 5)
    assert homework.text == 'Learn integrals homework'
    assert homework.deadline == dt.timedelta(days=5)
    assert homework.is_active()

    # Do homework
    assert student.do_homework(homework) is homework

    # Test expired homework
    homework = teacher.create_homework('Learn OOP homework', 0)
    assert homework.text == 'Learn OOP homework'
    assert homework.deadline == dt.timedelta(days=0)
    assert not homework.is_active()

    # Do expired homework
    assert student.do_homework(homework) is None

    # Test negative days
    with pytest.raises(ValueError):
        Homework("Learn SQL homework", -20)

def test_main_function(capfd):
    """Test the main function execution"""

    task_classes_main()

    captured = capfd.readouterr()

    assert "You are late" in captured.out
