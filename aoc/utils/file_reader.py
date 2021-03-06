import os

def path_join(path, file_path):
    return os.path.join(path, file_path)

def read_file_line(path, delimiter=" "):
    print("File path: {}".format(path))
    ret = []
    count = 1

    with open(path) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.strip()
            ret.append(line)
            count += 1

    print("File read counts: {}".format(count))

    return ret
