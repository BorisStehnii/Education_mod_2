def count_lines(name):
    with open(name, "r") as file:
        return len(file.readline())


def count_chars(name):
    count = 0
    with open(name, "r") as file:
        for line in file:
            count += len(line)
    return count


def test(name):
    res_1 = count_chars(name)
    res_2 = count_lines(name)
    return [res_1, res_2]
