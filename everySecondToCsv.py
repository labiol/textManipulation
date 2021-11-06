#convert txt file with layout: first_line <newline> empty_line <newline> second_line <newline> third_line etc.
#into csv file in format: first_line; second_line <newline> third_line; 4th_line <newline> etc.

print("--Input file input.txt--")
f = open("input.txt")
lines = f.readlines()
f.close

temp = ""
out = ""
i = 0

for line in lines:
    line = line.rstrip()
    linedl = len(line)
    if(linedl > 0 and i == 0):
        temp = line
        i = 1
    elif(linedl > 0 and i == 1):
        out = out + temp +"; " + line + "\n"
        i = 0    

print("--Output file: output.csv--")
f = open("output.csv","x")
f.write(out)
f.close
