Python print two variables
To print the two variables in Python, use the print() function.

# app.py
name = "Stranger Things"
season = 4
print("Total season for %s is %s" % (name, season))

Output
Total season for Stranger Things is 4

# How to remove everything after a character in a string in Python

a_string = "ab-cd"

split_string = a_string.split("-", 1) //Split into "ab" and "cd"

substring = split_string[0]

print(substring)

# Convert number to VNĐ
def add_commas(instr):
    out = [instr[0]]
    for i in range(1, len(instr)):
        if (len(instr) - i) % 3 == 0:
            out.append(',')
        out.append(instr[i])
    return ''.join(out)
