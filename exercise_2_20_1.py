class Open:

    def __init__(self, name_file, command="r"):
        self.name_file = name_file
        self.command = command

    def __enter__(self):
        self.file = open(self.name_file, self.command)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return None


if __name__ == "__main__":
    with Open("file_11.txt") as file_:
        pass
        # print(file_.readline())
    print(file_.closed)
