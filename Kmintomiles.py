#This variable takes kilometers
kilometers = float(input("Enter value in kilometers: "))
#This is conversing factor
conv_fac = 0.621371
miles = kilometers*conv_fac
#This prints the final answer
print("%0.2f kilometers is equal to %0.2f miles"%(kilometers,miles))
