with open('aaa.txt', 'w') as a_file:
    string = ''.join(["A" for _ in range(79)]) + '\n'
    for _ in range(50_000):
        a_file.write(string)

with open('bbb.txt', 'w') as b_file:
    string = ''.join(["B" for _ in range(79)]) + '\n'
    for _ in range(50_000):
        b_file.write(string)
