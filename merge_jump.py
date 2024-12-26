import os
import argparse

IGNORE = ('#','@','READ')
BUFFER_FRAME = 3

def main():
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description='Process .tas files.')
    parser.add_argument('--file', type=str, help='Path to source file to process')
    parser.add_argument('--folder', type=str, help='Path to the folder containing .tas files to process')
    args = parser.parse_args()

    if args.file:
        if not os.path.isfile(args.file):
            print("file name is not file.")
        elif not args.file.endswith('.tas'):
            print("file file is not '.tas'.")
        else:
            rewrite(args.file)
    elif args.folder:
        if not os.path.isdir(args.folder):
            print("folder name is not folder.")
        else:
            for file in os.listdir(args.folder):
                if not file.endswith('.tas'):
                    continue
                rewrite(os.path.join(args.folder, file))
    else:
        print("Please provide --file or --folder.")

class Input:
    def __init__(self, string:str):
        self.frame = 0
        self.direction = ''
        self.jump = False
        self.others = []
        elements = string.strip().split(',')
        if elements[0].isdigit():
            self.frame = int(elements[0])
        else:
            return
        for char in elements[1:]:
            if char.upper()=='J':
                self.jump = not self.jump
            elif char.upper()=='L':
                self.direction = 'L' if (self.direction != 'R') else ''
            elif char.upper()=='R':
                self.direction = 'R' if (self.direction != 'L') else ''
            else:
                self.others.append(char.upper())

    # def __init__(self, frame:int, direction:str, jump:bool, others:list):
    #     self.frame = frame
    #     self.direction = direction
    #     self.jump = jump
    #     self.others = others

    def __bool__(self):
        return self.frame>0
    
    def __str__(self):
        elements = []
        elements.append(f"{self.frame:>4}")
        if self.direction:
            elements.append(self.direction)
        if self.jump:
            elements.append('J')
        elements.extend(self.others)
        return ','.join(elements)+'\n'
    
    def __eq__(self, value):
        if not self.direction==value.direction:
            return False
        if not self.jump==value.jump:
            return False
        if not set(self.others)==set(value.others):
            return False
        return True

    
def rewrite(file_path:str):
    # make direction of jump unique for easy editing
    def merge_jump(inputs:list[Input]):
        frame = 0
        direction = ''
        for input in inputs[::-1]:
            if not direction and frame<BUFFER_FRAME and input.direction:
                direction = input.direction
                break
            frame += input.frame
        result = []
        for input in inputs:
            input.direction = direction
            if result and input==result[-1]:
                result[-1].frame += input.frame
            else:
                result.append(input)
        return result

    lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        line = file.readline()
        last_jump = []
        input = Input('')
        while line:
            if not line.strip().upper().startswith(IGNORE):
                input = Input(line)
            else:
                input = Input('')

            if input.jump:
                last_jump.append(input)
            elif last_jump:
                lines.extend(merge_jump(last_jump))
                last_jump = []
            
            if line.strip().upper().startswith(IGNORE):
                lines.append(line)
            elif input and not input.jump:
                lines.append(input)

            line = file.readline()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            # print(line, end='')
            file.write(str(line))

if __name__ == '__main__':
    main()
