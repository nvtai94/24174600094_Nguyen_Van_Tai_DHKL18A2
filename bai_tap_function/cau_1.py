# Câu 1
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
print(is_integer("121315121315")) 
print(is_integer("-100000100000"))
print(is_integer("24,1010"))
print(is_integer("asd256asd256"))
print(is_integer("99"))
