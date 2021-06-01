import inspect
from _tools._python_parser import _ParseFunctionComplexity


def complexity(obj):
    def wrapper(*args, **kwargs):
        source_code = inspect.getsource(obj)
        obj(*args, **kwargs)
        complexity_code = _ParseFunctionComplexity(source_code)
        complexity_code.print_function()
        return complexity_code
    return wrapper


if __name__ == '__main__':
    items = [4, 5, 6, 8]

    @complexity
    def constant_algo_1(items):
        total = items[0] * items[0]
        return total


    @complexity
    def linear_algo_1(items):
        total = 0
        for item in items:
            total += item
        return total


    @complexity
    def linear_algo_2(items):
        total = 0
        for item in items:
            total += item
        for item in items:
            total += item
        return total

    constant_algo_1(items)
    linear_algo_1(items)
    linear_algo_2(items)