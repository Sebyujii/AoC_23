# with open("C:\\Users\\sebas\\Desktop\\Code\\Adventofcode_2023\\01_input.txt") as file: # laptop
with open("E:\\Code\\AoC_23\\01_input_edited.txt") as file: # PC
    n = 0
    while line := file.readline():
        first = -1
        last = -1
        for a in line:
            if a.isdigit() and first == -1:
                first = int(a)
            elif a.isdigit() and first != -1:
                last = int(a)
        if last == -1:  # decke einzelne Zahlen pro Zeile ab
            last = first
        print(f"Zeilenzahl: {first*10 + last}")
        n += first*10 + last
    print(f"Summe: {n}")