#identify array
number_ranges = {}
    #define range counters for each range
number_ranges = {
    "1-10" : 0,
    "11-20" : 0,
    "21-30" : 0,
    "31-40" : 0,
    "41-50" : 0
}
#ask user to input numbers 1-50
while True:
    try:
        input_number = int(input("Please input a number between 1 to 50: "))
    #input will be stored in array
    #for every input, add 1 to the respective range
    # #if input is greater than or equal 1 and less than or equal 50
        #compare input to range   
        if input_number >= 1 and input_number <= 50:
    #if input is greater than or equal 1 and less than or equal 10
            #add 1 to range 1-10        
            if input_number >= 1 and input_number <= 10:
                number_ranges["1-10"] += 1
    #elif input is greater than or equal 11 and less than or equal 20
            #add 1 to range 11-20
            elif input_number >= 11 and input_number <= 20:
                number_ranges["11-20"] += 1 
    #elif input is greater than or equal 21 and less than or equal 30
            #add 1 to range 21-30
            elif input_number >= 21 and input_number <= 30:
                number_ranges["21-30"] += 1 
    #elif input is greater than or equal 31 and less than or equal 40
            #add 1 to range 31-40
            elif input_number >= 31 and input_number <= 40:
                number_ranges["31-40"] += 1 
    #elif input is greater than or equal 41 and less than or equal 50
            #add 1 to range 41-50
            elif input_number >= 41 and input_number <= 50:
                number_ranges["41-50"] += 1 
        
        else:
            break
            
    #if input is not int
        #print "Please input a valid number"
    except:
        print("Please input a valid value")
#if input number less than 1 or input number greater than 50
    #break loop, then print how many inputted numbers are in the following range
print("The number of inputted numbers for each range are: ")
print(f"range 1-10 = {number_ranges["1-10"]}")
print(f"range 11-20 = {number_ranges["11-20"]}")
print(f"range 21-30 = {number_ranges["21-30"]}")
print(f"range 31-40 = {number_ranges["31-40"]}")
print(f"range 41-50 = {number_ranges["41-50"]}")
    
        
        
        
        
        










