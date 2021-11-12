
from functools import wraps
import time


def log_file(method):
    @wraps(method)
    def log_magazine(self, *args):
        with open(f"{self.__class__.__name__}.log", "a+") as file_magazine:
            file_magazine.write(f"{time.strftime('%c')} >> {self.name_file} | {self.__class__.count}\n")

        return method(self)
    return log_magazine


class Open:

    count = 0

    def __init__(self, name_file, command="r"):
        self.name_file = name_file
        self.command = command
        self.__class__.count += 1

    @log_file
    def __enter__(self):
        self.file = open(self.name_file, self.command)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return None

    def count_lines(self):
        count = 0
        for _ in self.file:
            count += 1
        return count

    def count_chars(self):
        count = 0
        for line in self.file:
            count += len(line)
        return count


if __name__ == "__main__":
    with Open("file_11.txt", "w") as file_:
        pass
        # print(file_.readline())
    print(file_.closed)
    with Open("file_11.txt", "w") as file_:
        pass
    with Open("file_11.txt", "w") as file_:
        pass
