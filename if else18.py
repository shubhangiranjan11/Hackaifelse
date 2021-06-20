basic_salary=int(input("any number"))
if basic_salary<=10000:
    hra = 20*basic_salary
    da = 80*basic_salary
elif basic_salary<=20000:
    hra = 25*basic_salary
    da = 90*basic_salary
elif basic_salary>20000:
    hra = 30*basic_salary
    da = 95*basic_salary
else:
    print("there is no hra or da")
salary = basic_salary + hra + da
print("the full salary is ",salary)
