#convert txt file in schema 1stline newline empty newline 2ndline newline etc
#into csv file with 1stline and 2ndline
#need to convert file to anki

f = open("input.txt")
lines = f.readlines()
f.close

temp = ""
out = ""
i = 0

for line in lines:
#    print(str(len(line.rstrip())))
    line = line.rstrip()
    linedl = len(line)
    if(linedl > 0 and i == 0):
        temp = line
        print("temp=" + temp)
        i = 1
    elif(linedl > 0 and i == 1):
        out = out + temp +"; " + line + "\n"
        print("out=" + out)
        i = 0    

print("----")
f = open("output.csv","x")
f.write(out)
f.close
#print(out)
