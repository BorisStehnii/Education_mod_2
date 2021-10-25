class CustomException(Exception):

    def __init__(self, msg, *args):
        super().__init__(self, *args)
        self.msg = msg
        with open("logs.txt", "a") as logs_file:
            logs_file.write(self.msg)


raise CustomException("you wrong\n")
