
numDays = int(input("How many days temperature? "))
each= []
total =0
for i in range(1,numDays+1):
    eachTemp= int(input("Day " + str(i) + "'s high temperature:  "))
    each.append(eachTemp)

avg= round(sum(each)/len(each),2)

print(f"Average Temperature: {avg}")

above= 0
for i in each:
    if i > avg:
        above += 1

print(f"{above} days above average")