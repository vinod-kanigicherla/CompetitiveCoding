import sys
lines = [x.strip() for x in sys.stdin]
print(lines)

for i, line in enumerate(lines):
    #VAR
    if line.contains("VAR"):
        variable = line.split(" ")[1]
        #CHECK FOR REFERENCES
        for next_line in lines[1:]:
            if variable not in next_line:
                continue #no

