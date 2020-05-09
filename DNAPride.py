import re


data = [[input() for i in range(2)] for k in range(int(input()))]

for group in data:
    RNA = re.findall("[^ATCG]", group[1])
    if (len(RNA) > 0):
        print("Error RNA nucleobases found!")
    else:
        output = ""
        for base in group[1]:
            if (base == 'A'):
                output += "T"
            elif (base == "T"):
                output += "A"
            elif (base == "C"):
                output += "G"
            elif (base == "G"):
                output += "C"
        print(output)
