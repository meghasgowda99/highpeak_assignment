import json

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

filename = 'input.txt'

commands = {}
ls = []
with open(filename) as fh:
    i = 0
    for line in fh:
        if(i==0):
          _, n = line.strip().split(': ', 1)
        if(i<4):
          i=i+1
          continue
        command, description = line.strip().split(': ', 1)
        commands[int(description)] = command.strip()
        ls.append(int(description))
#print(n)
#print(json.dumps(commands, indent=2, sort_keys=True))
x = bubbleSort(ls)
N = len(ls)
n = int(n)
j=0
mx = ls[N-1]-ls[0]
for i in range(N-n+1):
    if((ls[i+n-1]-ls[i]) < mx):
        mx = ls[i+n-1]-ls[i]
        j = i
print("The goodies selected for distribution are:\n", file=open("output.txt", "a"))
for i in range(n):
    print(commands[ls[j+i]],": ",ls[i], file=open("output.txt", "a"))
print("\nAnd the difference between the chosen goodie with highest price and the lowest price is ", ls[j+n-1]-ls[j], file=open("output.txt", "a"))

