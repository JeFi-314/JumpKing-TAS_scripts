import os
import argparse

COMMENT = '#'

def main():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description='Process .tas files.')
    parser.add_argument('--source', type=str, help='Path to source file to process')
    parser.add_argument('--target', type=str, help='Path to the folder containing .tas files to process')
    args = parser.parse_args()

    if not args.source:
        print("Please provide --source file.")
    elif not os.path.isfile(args.source):
        print("source name is not file.")
    elif not args.source.endswith('.tas'):
        print("source file is not '.tas'.")
    elif not args.target:
        print("Please provide --target folder.")
    elif not os.path.isdir(args.target):
        print("target name is not folder.")
    else:
        ILs = read_ILs(args.source)
        update_ILs(args.target, ILs)

def read_ILs(file_path):
    """
    Reads the specified .tas file and gets ILs.
    """
    ILs = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        # skips header info
        file.readline()
        file.readline()
        file.readline()
        line = file.readline()
        area = ""
        contents = []
        while line:
            if line.startswith(COMMENT):
                ILs[area] = contents
                contents = []
                area = line.lstrip(COMMENT).strip()
            else:
                contents.append(line)
            line = file.readline()
    print(ILs.keys())
    return ILs


def update_ILs(directory_path, ILs):
    """
    Reads all .tas files in target directory and replace IL.
    """
    for file_name in os.listdir(directory_path):
        if not file_name.endswith('.tas'):
            continue
        skip = False
        with open(os.path.join(directory_path, file_name), 'r', encoding='utf-8') as file:
            line = file.readline()
            lines = []
            while line:
                if line.startswith(COMMENT):
                    lines.append(line)
                    area = line.lstrip(COMMENT).strip()
                    if area in ILs:
                        skip = True
                        lines.extend(ILs[area])
                    else:
                        skip = False
                elif not skip:
                    lines.append(line)
                line = file.readline()

        with open(os.path.join(directory_path, file_name), 'w', encoding='utf-8') as file:
            print(os.path.join(directory_path, file_name))
            for line in lines:
                # print(line, end='')
                file.write(line)

if __name__ == '__main__':
    main()
