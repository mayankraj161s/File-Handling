import pickle
bfile = open("data.dat","rb+")
lst = []
try:
    print("File data.dat stores these records:---")
    while True:
        lst.append(pickle.load(bfile))
except EOFError:
    bfile.close()
print(lst)
for i in range(len(lst)):
    print("Record Number",(i+1),":")
    for j in range(len(lst[0])):
        print('\t'+list(lst[i].keys())[j]+" : ",lst[i][list(lst[i].keys())[j]])
