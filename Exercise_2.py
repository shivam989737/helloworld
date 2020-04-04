# a=int(input("enter 1st no="))
# b=int(input("enter 2nd no="))
# c=int(input("enter 3rd no="))
# total=a+b+c
# average=total/3
# print("Total is {total} average is {average}".format(total,average))

first_number,second_number,third_number=input("Enter the first , second , third numbers :").split(",")
# print("Average of three number :{}+{}+{}".format(int(first_number),int(second_number),int(third_number)))
print(f"average : {(int(first_number)+int(second_number)+int(third_number))/3}")