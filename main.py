'''
DEVELOPER(S): Jake Feldman
COLLABORATORS: n/a
DATE: 4/17/2026
'''

"""
Gas mileage tracker that logs each fill-up and shows average MPG.

User enters the miles driven and gallons filled for a single fill-up and
the program calculates the MPG for the entry. Each fill is appended to a log
which shows the  overall average MPG.


I chose to use a list for fillups becuase each fillup just adds to the last one
and there is no need to identify each specfic fillup with a key for key based lookups.
The list keeps it simple and works by looking through all fillups not just indivudal ones.
"""



##########################################
# FUNCTIONS:
##########################################
def calculate_mpg(miles,gallons):
    "Calculates miles per gallon"
    return miles/gallons

def log_fillup(miles, gallons, cost, mpg):
    "Appends a fill-up to the log file"
    with open("mileage_log.txt", "a") as file:
        file.write(f"{miles},{gallons},{cost},{mpg}\n")

def load_fillups():
    "Returns past fillups from file into a list of mpg and cost entries"
    fillups=[]
    with open("mileage_log.txt","r") as file:
        for line in file:
            miles, gallons, cost, mpg=line.strip().split(",")
            fillups.append([float(mpg),float(cost)])
    return fillups

def average_mpg(fillups):
    "Returns average mpg from log"
    total=0
    for entry in fillups:
        total+= entry[0]
    return total/len(fillups)

def total_spent(fillups):
    "Returns total spent from log"
    total=0
    for entry in fillups:
        total+= entry[1]
    return total

##########################################
# MAIN PROGRAM:
##########################################
miles=float(input("Enter miles driven since last fill: "))
gallons=float(input("Enter gallons filled: "))
cost=float(input("Enter total cost of fill-up: "))
mpg=calculate_mpg(miles, gallons)
log_fillup(miles, gallons, cost, mpg)
fillups=load_fillups()

print(f"This fill-up: {mpg:.2f} MPG, ${cost:.2f}")
print(f"Average MPG across {len(fillups)} fillups: {average_mpg(fillups):.2f}")
print(f"Total Spent: ${total_spent(fillups):.2f}")