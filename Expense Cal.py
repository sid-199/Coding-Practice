#Expense counter0
items=[]
prices=[]

while True:
    ask=input("If you want to stop press'1' otherwise press'0' ")
    if ask== '0':
        item_name=input("Enter name of item= ")
        items.append(item_name)
        price=input(f"Price of {item_name}= "    "Rs")
        if price.isdigit:
            prices.append(price)
        else:
            print(f"{price} is not Number")
        
       
       
    elif ask=='1':
        break
    else:
        print("Give correct response")


Ask=input("If you want your expense list enter '1' otherwise enter '0' ")
if Ask=='1':  
    if len(items)==0:
        print("No expenses")
    else:
        for item_name, price in zip(items,prices):
            print(f"{item_name} cost= {price}Rs")

      

        ask_again=input("If you want sum expense please press '1' otherwise press '0'")
        if ask_again=='1':
            prices=[float(x) for x in prices]
            price_sum=sum(prices)
            if price_sum == 0:
                print("No expenses")
            else:
                print(f"Your expense is {price_sum}Rs")
print("Thank You for your Response")