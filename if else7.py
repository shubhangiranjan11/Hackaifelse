# year=int(input("any number"))
# if year%4==0:
#     if year%100:
#         if year%400:
#             print("its a leap year")
#         else:
#             print("not")
#     else:
#         print("not leap year")
# else:
#     print("is not leap year")




year=int(input("any number"))
if year%4==0 and year%100!=0:
    print("its a leap year")
elif year%100==0:
    print("its a leap year")
elif year%400==0:
    print("its a leap year")
else:
    print("not a leap year")


