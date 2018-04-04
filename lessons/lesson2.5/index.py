# import os

# print(os.environ)
# print('Hello', os.environ['USER'])
# os.environ['TOKEN'] = 'secure token'
# print('TOKEN: ', os.environ['TOKEN'])

# for name, value in os.environ.items():
#     print('{}: {}'.format(name, value))


import sys

print('This is stdout', file=sys.stdout)
print('This is stderr', file=sys.stderr)

with open('file.log', mode='w') as f:
    print('this is code in file', file=f)

s = input()
print(s)    
