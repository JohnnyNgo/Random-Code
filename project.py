#Johnny Ngo

block = int(input())
spaces = ''

for i in range(0,block):
    if i == 0:
        print('+-+')
    print(spaces + '| |')
    if i == block-1:
        print(spaces + '+-+')
    else:
        print(spaces + '+-+-+')
    spaces += '  '
    
    
