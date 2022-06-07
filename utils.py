
def read_file(file):
    f = open(file)
    lines = f.readlines()
    new_lines = []
    for line in lines:
        line = line.replace('\n', '').replace('\r', '')
        #print(type(line))
        new_lines.append(line)
    f.close()

    return new_lines


def get_name_and_pass():
    lines = read_file("D:\\tmp\\cambly.txt")
    # print(lines)
    u = ''
    p = ''
    if len(lines) == 2:
        u = lines[0]
        p = lines[1]
    return u, p
