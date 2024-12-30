import pytest
from student import Student  

@pytest.fixture
def student_data():
    """Set up test data."""
    return Student(name="sahil nikam", grades=[85, 90, 78])

def test_add_grade(student_data):
    student_data.add_grade(88)
    assert 88 in student_data.grades

def test_add_invalid_grade(student_data):
    with pytest.raises(ValueError):
        student_data.add_grade(105)

def test_average_grade(student_data):
    assert student_data.average_grade() == pytest.approx(84.33, rel=1e-2)

def test_highest_grade(student_data):
    assert student_data.highest_grade() == 90

def test_lowest_grade(student_data):
    assert student_data.lowest_grade() == 78

def test_average_with_no_grades():
    student = Student(name="Empty Student")
    assert student.average_grade() == 0
