# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful
def dose(needs):
    #YOUR SOLUTION STARTS HERE
    nutri = ()
    if (sum(needs) < int(501)) and (max(needs) < int(250)):
        for i in needs:
            nutri[i] = (round((250-needs[i])/10 - 0.4),(250-needs[i])%10)
        return nutri
    else:
        print("No medicine given")
print(dose(input("Please enter the patient's data:")))
    #YOUR SOLUTION ENDS HERE