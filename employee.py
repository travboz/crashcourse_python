class Employee:
    """Modelling an employee."""
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary

    def give_raise(self, amount=''):
        if amount:
            self.salary += amount
        else:
            self.salary += 5000