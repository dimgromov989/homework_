def log(filename=None):
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""

    def decorator_for_logging(function):
        def wrapper(*args, **kwargs):
            start_message = f"Функция {function.__name__} начала свою работу\n"
            if filename is not None:
                with open(filename, mode="a", encoding="utf-8") as file:
                    file.write(start_message)
            else:
                print(start_message, end="")
            try:
                result = function(*args, **kwargs)
                end_message = f"{function.__name__} ok, with result: {result}\n"
                success = True
            except Exception as e:
                end_message = f"{function.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                success = False
            if filename is not None:
                with open(filename, mode="a", encoding="utf-8") as file:
                    file.write(end_message)
            else:
                print(end_message, end="")
            if success:
                return result
            else:
                pass

        return wrapper

    return decorator_for_logging


@log(filename="my_log.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 6)
