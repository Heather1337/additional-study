log_file = open("um-server-01.txt")

#Objective --- change the day to Monday to log what the CEO is asking

#Declaring function that takes in a log file as an argument and prints out day if Tue
def sales_reports(log_file):
    #For each line in the file
    for line in log_file:
        #grabs each line and strips any trailing space or characters
        line = line.rstrip()
        #grabs the first 3 characters starting from the beginning
        day = line[0:3]
        #conditional checking if the day is equal to Tue 
        if day == "Mon":
            #printing each line if day is set to Tue
            print(line)


sales_reports(log_file)
