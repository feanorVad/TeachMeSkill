class BudgetError(ValueError):
    pass


class Department:
    def __init__(self, name, employees, budget):
        self.name = name
        self.employess = employees
        self.budget = budget

    def get_budget_plan(self):
        try:
            res = self.budget - sum(list(self.employess.values()))
            if res < 0:
                raise BudgetError("Error: too small budget")
            else:
                return res
        except Exception as e:
            return e

    def get_average_salary(self):
        return round(sum(list(self.employess.values())) / len(self.employess), 2)

    def __str__(self):
        return f'{self.name} ({len(self.employess)} - {self.get_average_salary()}), {self.budget}'

    def merge_departments(self, *args):
        try:
            res = Department(self.name, self.employess, self.budget)
            for i in range(0, len(args)):
                res.name += ' - ' + args[i].name
                res.budget += args[i].budget
                res.employess.update(args[i].employess)
            if type(res.get_budget_plan()) is BudgetError :
                raise BudgetError("Error: too small budget")
            else:
                return res
        except Exception as e:
            return e

    def __add__(self, other):
        res = Department(self.name, self.employess, self.budget)
        return res.merge_departments(other)

    def __or__(self, other):
        try:
            if type(self.get_budget_plan()) is BudgetError:
                raise BudgetError("Error: too small budget")
            if type(other.get_budget_plan()) is BudgetError:
                raise BudgetError("Error: too small budget")
            if self.get_budget_plan() == other.get_budget_plan():
                return self
            else:
                return self if self.get_budget_plan() > other.get_budget_plan() else other
        except Exception as e:
            return e



