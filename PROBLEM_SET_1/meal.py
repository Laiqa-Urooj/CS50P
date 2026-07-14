def main():
    time=input("What time is it ? ")
    meal_time = convert(time)
     #To match the time with meal time 
    if  7<= meal_time <=8 :
        print("breakfast time")
    elif 12<= meal_time <=13 :
        print("lunch time")
    elif 18<= meal_time <=19 :
        print("dinner time")
    else:
        None


#Function to convert time to float and match the meal time 
def convert(time):
    #To separate hours and minutes from user's input
    hours,minutes = time.split(":")
    #To convert time to float
    hours=float(hours)
    minutes=float(minutes)
    return hours + (minutes / 60) 
    
if __name__ == "__main__":
    main()