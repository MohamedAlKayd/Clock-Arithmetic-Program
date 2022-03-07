# Mohamed Yasser Anwar Mahmoud AlKayd
# Clock Arithmetic Program

# - Start of Program -

current_time = input("Enter the current time: ")
duration = input("Enter the duration: ")
 
#24 hour format
HH=int(current_time[:2])
MM=int(current_time[3:5])
SS=int(current_time[6:8])
AP=(current_time[9:11])
YY=int(duration[-3:-1])

if len(duration)==6:
    XX=int(duration[-6:-4])
else:
    XX=0

if len(duration)==3:
    total_seconds=(((HH)*3600)+((MM+YY)*60)+SS)
else:
    total_seconds=(((HH+XX)*3600)+((MM+YY)*60)+SS)

hour=(total_seconds//3600)
minutes=((total_seconds-hour*3600)//60)
seconds=(total_seconds-(hour*3600)-(minutes*60))

if AP=="AM":
    print(hour,"hours,",minutes,"mins,",seconds,"secs")
elif AP=="PM":
    print(hour+12,"hours,",minutes,"mins,",seconds,"secs")
else:
    print(hour,"hours,",minutes,"mins,",seconds,"secs")

# - End of the Program -