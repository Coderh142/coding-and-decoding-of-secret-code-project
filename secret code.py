import random as r

choice = int(input(("FOR CONDING PRESS 1 OR FOR DECONDING PRESS 0: ")))

if (choice == 1):

   print("********* CODING *************")

   code  = input("Enter the value: ")

   if (len(code) >= 3):

     string = ("jdhsfehfjnfdkjaljvjbfdkjwbvkjwXJKSCNWMDWKL")   # LIST
     rand = r.sample(string, 3)         # It takes 3 random latters from string list
     join_fun = "".join(rand)             # We used it for joining 

     code = join_fun + code[1::] + code[0] + join_fun   # Without join we can't join STRINGS & LISTS
     print(code) 

   else:
     code = code[::-1]
     print(code)


else: 
    print("********* DECODING *************")
 
    code  = input("Enter the value: ")
    
    if (len(code) >= 3):
        code = code[:-3]       # Remove last 3 latters    
        code = code[-1] + code[3:]   # Add last & then Remove firt 3 & Go to the last
        code = code[:-1]
        print(code)
        
    else:
     code = code[::-1]
     print(code)