def part1():
    with open("day6.txt") as file:
        text = file.read()
    signal = list(text)
    found = 0
    for index, i in enumerate(signal):
        unique = [signal[index], signal[index+1], signal[index+2], signal[index+3]]
        if len(unique) == len(set(unique)):
            found = index+4
            break
    print(found)


part1()
def part2():
    with open("day6.txt") as file:
        text = file.read()
    signal = list(text)
    found = 0
    for index, i in enumerate(signal):
        unique = [signal[index], signal[index+1], signal[index+2], signal[index+3], signal[index+4], signal[index+5], signal[index+6], signal[index+7], signal[index+8], signal[index+9], signal[index+10], signal[index+11], signal[index+ 12], signal[index+13]]
        if len(unique) == len(set(unique)):
            found = index + 14
            break
    print(found)

part2()