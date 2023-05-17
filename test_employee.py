from employee import Employee

def test_give_default_raise():
    """Test that a single response is stored properly."""
    initial_salary = 75_000
    emp1 = Employee("Harold", "Haroldson", initial_salary)
    emp1.give_raise()

    assert emp1.salary == (initial_salary + 5_000)

def test_give_custom_raise():
    """Test that a single response is stored properly."""
    initial_salary = 75_000
    emp1 = Employee("Harold", "Haroldson", initial_salary)
    emp1.give_raise(10_000)

    assert emp1.salary == (initial_salary + 10_000)