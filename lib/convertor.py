def convertor ():
    #input field to enter the time
    hour = int(input ("Enter hours:"))
    minute = int(input("Enter Minute:"))
    period = input("am/pm:") 

    if 1 <= hour <= 12 and 0 <= minute <= 59 and period in ("am", "pm"):
        if period == "pm" and hour != 12:
            hour += 12
        elif period == "am" and hour == 12:
            hour = 0

        output = str(f"Time is: {hour}:{minute} hrs")
        return output
    else:
        return "enter valid time"
   
#prints the output
print(convertor())