def addcount():
    #Enter path to textfile
    deathfile = open("deathcount.txt", "r")
    #since readlines returns a list, additional characters have to be stripped
    readcount = str(deathfile.readlines(0)).strip("'\\[]n")
    intcount = int(readcount)
    intcount += 1
    deathfile.close()
    deathfile = open("deathcount.txt", "w")
    deathfile.write(str(intcount))
    deathfile.close()

def subcount():
    #Enter path to text file
    deathfile = open("deathcount.txt", "r")
    #since readlines returns a list, additional characters have to be stripped
    readcount = str(deathfile.readlines(0)).strip("'\\[]n")
    intcount = int(readcount)
    intcount -= 1
    deathfile.close()
    deathfile = open("deathcount.txt", "w")
    deathfile.write(str(intcount))
    deathfile.close()

def main():
    while True:
        trigger = input()
        if trigger == "1":
            addcount()
        elif trigger == "2":
            subcount()

main()
