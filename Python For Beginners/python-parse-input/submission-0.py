from typing import List

def read_integers() -> List[int]:
    user_input = input()
    list_i = user_input.split(",")
    list_f = []
    for num in list_i:
        list_f.append(int(num))
    return list_f

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
