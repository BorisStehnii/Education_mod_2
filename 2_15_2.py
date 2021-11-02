def stop_words(list_):

    def words_(func):

        def words_replacement(*args):
            string_ = func(*args)
            print(string_)
            for word in list_:
                count_ = string_.count(word)
                string_ = string_.replace(word, "*", count_)
            return string_
        return words_replacement
    return words_


@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi BMW in his brand new BMW!"


print(create_slogan("Boris"))
