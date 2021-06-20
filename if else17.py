physics=int(input("any number"))
chemistry=int(input("any number"))
biology=int(input("any number"))
mathematics=int(input("any number"))
computer=int(input("any number"))

all_percentage = physics + chemistry + biology + mathematics + computer
percentage=(all_percentage/500)*100
print("marks of subjects",all_percentage)
print("total marks",percentage)
if percentage>=90:
    print("GradeA")
elif percentage>=80:
    print("GradeB")
elif percentage>=70:
    print("GradeC")
elif percentage>=60:
    print("GradeD")
elif percentage>=40:
    print("GradeE")
elif percentage<40:
    print("GradeF")
else:
    print("there is no percentage")


