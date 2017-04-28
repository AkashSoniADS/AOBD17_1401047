fout=open("MergedDataset.csv","a")

# For the first file:
for line in open("sh1.csv"):
    fout.write(line)

# For the rest of the files:    
for num in range(2,39):
    f = open("sh"+str(num)+".csv")
    f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()
