import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

data = str(input())
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

result = ''
for ele in alpha:
    data = data.replace(ele, ' ')
print(len(data))
