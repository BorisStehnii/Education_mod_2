def count_lines(file):
    count = 0
    for _ in file:
        count += 1
    return count


def count_chars(file):
    count = 0
    for line in file:
        count += len(line)
    return count


def test(file):
    res_1 = count_lines(file)
    file.seek(0)
    res_2 = count_chars(file)
    return [res_1, res_2]
