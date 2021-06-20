profit=int(input("any number"))
loss=int(input("any number"))
if profit<loss:
    amount=profit-loss
    print("its losing",amount)
elif loss<profit:
    amount2=loss-profit
    print("its lossing profit",amount2)
else:
    print("there is no loss or profit")