"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

#Open sale report 
f = open('sales-report.txt')
#Iterate over each line (order) in the sales report
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    #Saving the salesperson for each sale into a variable
    salesperson = entries[0]
    #Saving the amount of melons purchased in each sale into a variable
    melons = int(entries[2])

    #Checking to see if salesperson already exists in salespeople list
    if salesperson in salespeople:
        #If they do exist, saving the index of their location in the list
        position = salespeople.index(salesperson)
        #Then incrementing the count of melons they have sold by amount in current sale
        melons_sold[position] += melons
    else:
        #If they do NOT exist, add them to the salespeople list
        salespeople.append(salesperson)
        #Add the amount of melons sold to melons list with coordinating index 
        melons_sold.append(melons)

#Print out the amounts of melons sold by each salesperson by looping over list
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
