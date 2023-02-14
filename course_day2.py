gross=int(input("Your gross salary:"))
kids=int(input("How many children do you have?"))

if gross < 1000 :
    tax = 10 - kids
elif gross < 2000 :
    tax = 12 - kids
elif gross < 4000 :
    tax = 14 - kids / 2
else:
    tax = 18 - kids / 2

if tax < 0 :
    tax = 0

net = gross - gross * ( tax * 0.01 )
print(net)


#if gross < 2000 :
#   if gross < 1000 :
#       tax = 10
#    else :
#       tax = 12
#   tax -= kids
#else :
#   if gross < 4000 :
#       tax = 14
#   else :
#       tax = 18
#   tax -= kids / 2
#
#net = gross - gross * ( tax * 0.01)
#print(net)
#
