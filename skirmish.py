with open("skirmish.txt", "r", encoding='utf8') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    # lines = [line for line in lines if line != ""]

    # lines = [line for line in lines if not ',' in line and not '#' in line]
    lines = [line.upper() for line in lines]

    # lines = [line for line in lines if len(line) > 10]
    # lines = [line for line in lines if line[1] == '.']

    everyOther = True
    temp = lines.copy()
    lines = []
    translate = {}
    for i in range(len(temp) - 2):
        line = temp[i]
        ahead = temp[i + 1]
        if everyOther:
            translate[line] = ahead
        
        everyOther = not everyOther

    translate = { key: value for key, value in sorted(translate.items(), key=lambda item: -len(item[0]))}
    print(translate)

    with open("./data/input.txt", "r") as file:
        lines = file.readlines()

        lines = [line.strip() for line in lines]

        for i in range(len(lines)):
            for key, value in translate.items():
                if key in lines[i]:
                    lines[i] = value

        with open("outie.txt", "w") as file:
            for line in lines:
                print(line)
                file.write(line + "\n")
