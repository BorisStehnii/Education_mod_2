class Open:

    count = 0

    def __init__(self, name_file, command="r"):
        self.name_file = name_file
        self.command = command
        Open.count += 1

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

    def __enter__(self):
        self.file = open(self.name_file, self.command)

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):

        with open("magazine.txt", "a+") as file_magazine:
            file_magazine.write(f"{self.file.name}, {Open.count}\n")

        self.file.close()
        return None


if __name__ == "__main__":
    with Open("file_11.txt", "w") as file_:
        pass
        # print(file_.readline())
    print(file_.closed)
    with Open("file_11.txt", "w") as file_:
        pass
    with Open("file_11.txt", "w") as file_:
        pass
