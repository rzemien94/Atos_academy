def createfile(string):
    try:
        file=open('zad1.txt','a')
        file.write(string)
        file.close()
    except Exception as e:
        print("error: ",e)

createfile('cos')