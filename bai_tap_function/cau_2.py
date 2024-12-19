# Câu 2
def is_positive_integer(s):
    try:
        so = int(s)
        return so > 0
    except ValueError:
        return False
print(is_positive_integer("2325"))
print(is_positive_integer("-2336"))
print(is_positive_integer("24.5"))
print(is_positive_integer("fghj56"))
print(is_positive_integer("1"))
print(is_positive_integer("9999"))