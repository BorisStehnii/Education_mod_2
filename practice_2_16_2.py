class StrUtil:

    @staticmethod
    def clean_data(string_):
        if isinstance(string_, str):
            return " ".join(i for i in string_.split(" ") if len(i) > 0).lower()
        else:
            raise TypeError


print(StrUtil.clean_data("   I want to break free   "))
