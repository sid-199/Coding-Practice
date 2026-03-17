def mutate_string(string, position, character):
    

    result=string[:position]+character+string[position+1:]
    print (result)

x=string=input()

y=position=int(input())
z= character=input()
mutate_string(x,y,z)