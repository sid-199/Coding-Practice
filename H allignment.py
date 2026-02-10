w=int(input("Enter odd no.:"))

for i in range(w):
    print(('H'*i).rjust(w-1) + 'H' + ('H'*i).ljust(w-1))

for i in range(w+1):
    print(('H'*w).center(w*2) + ('H'*w).center(w*6))

for i in range((w+1)//2):
    print(('H'*w*5).center(w*6))

for i in range(w+1):
    print(('H'*w).center(w*2) + ('H'*w).center(w*6))


for i in range(w):
    print((('H'*(w-i-1)).rjust(w) + 'H' + ('H'*(w-i-1)).ljust(w)).rjust(w*6))

