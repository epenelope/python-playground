fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    s = line.find(' ')
    e = len(line) -1
    d = (line[s+1:e])
    data = float(d)
    total = total+data
    count = count+1

avg = total/count
    
print('Average spam confidence:', avg)
