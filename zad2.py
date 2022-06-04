print(50*"-")
try:
    file=open('zad1.txt','r')
    for i in file:
        print(i,end="")
    file.close()
except Exception as e:
    print("error:",e)
print("\n",50*"-")
samogloski=('a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y','A', 'Ą', 'E', 'Ę', 'I', 'O', 'U', 'Y')
try:
    file=open('zad1.txt','r')
    lines=file.readlines()
    for line in lines:
        tekst = line
        do_zmiany = []
        for i in range(len(line)):
            for j in range(len(samogloski)):
                if (tekst[i] == samogloski[j]):
                    do_zmiany.append(tekst[i])
        for i in range(len(do_zmiany)):
            tekst = tekst.replace(do_zmiany[i], "")
        print(tekst, end="")
    file.close()
except Exception as e:
    print("error:",e)
print("\n",50*"-")
try:
    file=open('zad1.txt','r')
    lines=file.readlines()
    file.close()
    file = open('zad1.txt', 'w')
    for line in lines:
        file.write(line.upper())
    file.close()
except Exception as e:
    print("error:",e)