inFile = 'data.csv' #input
outFile = 'lista.data'

with open(inFile, 'r', encoding="utf-8") as f1, open(outFile, 'w', encoding='utf-8') as f2:
    #här finns filen
    lines = f1.readlines()
    for line in lines: #iterera över listan
        print(line)
        # splitLine = line.split(',')
        # username = splitLine[1] + splitLine[2]
        # f2.write(username + '\n')
        # print(line.replace(',', ';')) #sida.94 i boken
        #skriv ny fil s.204
        # replacted = line.replace(',', ',')
        # print(replaced)
        # f2.write(replaced)
        
        