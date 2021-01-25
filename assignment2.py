def rmv_duplicates (s = ""):                              #Calling the function named rmv_duplicates
  if len(s) < 2:                                          #checking if the length of the string is less than 2 to terminate the loop
    return s                                              #returning value of a single string
  elif s[0] == s[1]:                                      #check if the strings stack value is matching with the next stack value
    return rmv_duplicates(s[1:])                          #recalls the function after removing one stack value S[0] and recall the function again
  else:                                                   #goes into the else condition
    return s[0] + rmv_duplicates(s[1:])                   #if the two stacks value doesnt match it stores and pass it to the recursive function again to compare other stacks value

print(rmv_duplicates(input("Enter your strings here:")))  #takes inputs and pass it to the recursive function and prints the result