def part1():
    with open("day6.txt") as file:
        text = file.read()
    signal = list(text)
    found = 0
    for index, i in enumerate(signal[0:-3], start=1):
        if i != signal[index+1] and i != signal[index+2] and i != signal[index+2]:
            found = index
            break
    print(found)

part1()