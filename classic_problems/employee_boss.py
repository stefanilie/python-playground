# Given a list of employees and their bosses as a text file, write a function
# that will print out a hierarchy tree of the employees.
# Sample input =
# Sam, Ian, technical lead, 2009 / Ian, NULL, CEO,2007/ Fred, Sam, developer, 2010
#
# The format is name, supervisor, designation, year of joining
#
# The output should be
# Ian CEO 2007
# -Sam Technical lead 2009
# - -Fred Developer 2010

f = open("hierarchy.txt", 'r')
data = f.read()
arr = str(data).split('/')
boss = []
employees = []

# Organising the data
for item in arr:
    toAppend = str(item).split(',')
    employees.append(toAppend)
    if " NULL" in toAppend:
        boss = toAppend

print boss

# Now that we found the boss, it's time to add him first to the list
arrStructure = []
arrStructure.append(boss)
employees.remove(boss)

i=1
while employees.count:
    # adding the first layer of employees that depend to the boss
    for employee in employees:
        if employee[1] == boss[0]:
            arrStructure.append(employee)

    # removing the items from the employee list
    for j in range(i,len(arrStructure)):
        employees.remove(employees[j])

    boss = arrStructure[i]
    i+=1

# selecting the boss' name
boss = arrStructure[0][1]
tree = ""
# them iterating through all the employees, but printing them by boss
for j in range(len(arrStructure)):
    while arrStructure[j][1] == boss and j <len(arrStructure):
        print tree, arrStructure[j]
        j+=1
    if j <len(arrStructure):
        boss = arrStructure[j][1]
        tree+="-"



# arrCurrentBoss =[]
# for item in employees:
#     if item[1] == boss:
#         # if it's the first item in the list
#         if arrCurrentBoss.count == 0:
#             arrCurrentBoss.append(item)
#         # if not, we add it to it's right place
#         else:
#             i=0
#             while i < len(arrCurrentBoss):
#                 # if his seniority in the firm is smaller than the one of others
#                 if arrCurrentBoss[i][3]<item[3]:
#
