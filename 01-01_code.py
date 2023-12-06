with open("C:\Users\sebas\Desktop\Code\Adventofcode_2023\01_input.txt") as file:
    n = 0
    while line := file.readline():
        first = -1
        last = -1
        for a in line:
            if a.isdigit() and first == -1:
                first = a
            elif a.isdigit() and first != -1:
                last = a
        n += first*10 + last
    print(f"Summe: {n}")