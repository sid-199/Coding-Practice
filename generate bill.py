def bill(x,y,z):
    pri_pizza=100
    pri_puffs=20
    pri_cooldrink=10

    sum=x*pri_pizza+y*pri_puffs+z*pri_cooldrink

    return f"Bill Detail: \n  No of pizzas:{x} \n  No of puffs:{y} \n  No of cooldrinks:{z} \n  Total bill:{sum}  \nEnjoy The Show!!!"


piz=int(input("Enter no. of pizzas: "))

puf=int(input("Enter no. of puffs: "))

cold=int(input("Enter no. of cooldrinks: "))


f=open("bill_gen.txt","w")
f.write(bill(piz,puf,cold))

f.close()
print("bill added in file..")