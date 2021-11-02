def arg_rules(type_, max_length, contains):

    def validates(func):

        def words_replacement(string_):

            if not isinstance(string_, type_) or len(string_) > max_length:
                slogan = False
            else:
                for parameter in contains:
                    if parameter not in string_:
                        slogan = False
                        return slogan
                slogan = func(string_)
            return slogan
        return words_replacement
    return validates


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"


# print(create_slogan("johndoe0@gm"))
assert create_slogan('joe05gm') is False
assert create_slogan('joe05@gmffffffffffff') is False
assert create_slogan("S@SH05") == "S@SH05 drinks pepsi in his brand new BMW!"
