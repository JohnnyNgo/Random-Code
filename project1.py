from pathlib import Path
import shutil
previous_list = []
interesting_list = []
step = 1
done = False

#Note: 'things' are the paths

def append_interesting():
    '''put the search/second step result into the interesting list and prints it out'''
    interesting_list.append(things)
    print(things)

def recursive_dir(main:Path):
    '''Takes in directory, checks if theres files and print those first, then checks folders and loops this function again'''
    paths = list(main.iterdir())
    paths.sort()
    for x_dir in paths:
        if x_dir.is_file():
            print(x_dir)
            previous_list.append(x_dir)
    for x_dir in paths:
        if x_dir.is_dir():
            recursive_dir(x_dir)

def read_firstline(things:Path):
    ''' Attempts to open file and read it, if it fails, it isn't a text file '''
    try:
        infile = open(things, 'r')
        text = infile.readline()
        print(text[:-1])
        infile.close()
    except:
        print("NOT TEXT")

def dupe(things:Path):
    '''Takes paths and creates a .dup of them'''
    i = str(things)
    i.replace('\\','\\\\')
    newlocation = i + '.dup'
    shutil.copy(things, newlocation)

def find_text(things:Path, t:str):
    'Takes in path, opens if its a file and checks if text is in the file'
    try:
        infile = open(things, 'r')
        content = infile.read()
        infile.close()
        if t in content:
            append_interesting()
    except:
        pass
                
if __name__ == '__main__':
    while not done:
        x = input()
        if step == 3:
            try:
                if x == 'F':
                    for things in interesting_list:
                        read_firstline(things)
                    done = True
                elif x == 'T':
                    for things in interesting_list:
                        things.touch()
                    done = True
                elif x == 'D':
                    for things in interesting_list:
                        dupe(things)
                    done = True
                else:
                    print('ERROR')
            except:
                print('ERROR')
        if step == 2:
            try:
                if x == 'A':
                    interesting_list = previous_list
                    for things in interesting_list:
                        print(things)
                    step = 3
                else:
                    x = x.split()
                    if x[0] == 'T':
                        text = '' 
                        for x1 in range(len(x)):
                            if x1 != 0:
                                text += x[x1] + " "
                        text = text.strip()
                        for things in previous_list:
                            find_text(things, text)
                            step = 3
                        if interesting_list == []:
                            done = True
                    elif len(x) == 2:
                        if x[0] == 'N':
                            for things in previous_list:
                                if x[1] == things.name:
                                    append_interesting()
                                    step = 3
                            if interesting_list == []:
                                done = True
                        elif x[0] == 'E':
                            for things in previous_list:
                                if x[1][0] != '.':
                                    start = '.' + x[1]
                                else:
                                    start = x[1]
                                if start == things.suffix:
                                    append_interesting()
                                    step = 3
                            if interesting_list == []:
                                done = True
                        elif x[0] == '<':
                            for things in previous_list:
                                if things.stat().st_size < int(x[1]):
                                    append_interesting()
                                    step = 3
                            if interesting_list == []:
                                done = True
                        elif x[0] == '>':
                            for things in previous_list:
                                if things.stat().st_size > int(x[1]):
                                    append_interesting()
                                    step = 3
                            if interesting_list == []:
                                done = True
                        else:
                            print('ERROR')
                    else:
                        print('ERROR')
            except:
                print('ERROR')
                step = 2
        if step == 1:
            try:
                previous_list = []
                x[2:].replace('\\','\\\\')
                p = Path(x[2:])
                if x[0] == 'D':
                    previous_list = []
                    for d in p.iterdir():
                        if d.is_file():
                            print(d)
                            previous_list.append(d)
                    step = 2
                elif x[0] == 'R':
                    previous_list = []
                    recursive_dir(p)
                    step = 2
                else:
                    print('ERROR')
            except:
                print('ERROR')
                step = 1
    

