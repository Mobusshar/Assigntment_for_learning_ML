s=input("Enter your input here:")           #here the input got declared and stored in a string "s"
i=0                                         #initializing the index values of the follwoing string
s1=""                                       #s1 will contain the output string and it's initialized with an empty string

for x in s:                                 #using a for loop to check through each index and print it
    if s.index(x)==i:                       #checking if the following string getting a match with the index value then it will allow it to store the value in S1
        s1+=x                               #storing s1 whenever getting matched with the index value 
    i+=1                                    #increasing the value of i to approach to the next index number
print(s1)                                   #printing final value of s1 with the trimmed string
