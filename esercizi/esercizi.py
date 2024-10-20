import random
import time 


matrice = [[3,6,4,3,5,],[3,6,4,3,5,],[3,6,4,3,5,],[3,6,4,3,5,]]


def cornice():
    cornice = []
    ultimaRiga = []
    fineCornice = []
    for i in range(len(matrice)):
        if i == 0:
            for j in range(len(matrice[i])):
                cornice.append(matrice[i][j])
        elif i == len(matrice)-1:
            for j in range(len(matrice[i])):
                ultimaRiga.append(matrice[i][j])
            ultimaRiga.reverse()
            for j in ultimaRiga:
                cornice.append(j)
        else:
            fineCornice.append(matrice[i][0])
            cornice.append(matrice[i][len(matrice[i])-1])
    fineCornice.reverse()
    for num in fineCornice:
        cornice.append(num)
    print(cornice)       

#cornice()

def MinMax():
    for i in range(len(matrice)):
        max = matrice[i][0]
        min = matrice[i][0]
        for j in range(len(matrice[i])):
            
            if matrice[i][j] > max:
                max = matrice[i][j]
            elif matrice[i][j] < min:
                min = matrice[i][j]
        print(f"il numero minore della linea {i} è {min}")
        print(f"il numero maggiore della linea {i} è {max}")

#MinMax()


def matriceSoloCornice():
    A = []
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if i == 0:
                A.append(matrice[i][j])
            elif i == len(matrice)-1:
                A.append(matrice[i][j])
            elif j == 0 or j == len(matrice[i])-1:
                A.append(matrice[i][j])
            else:
                A.append(0)
    print(A)

#matriceSoloCornice()

def generaPasswordDiff():
    passwdDiff = ""
    charPass = ""
    randomNum = 0
    for i in range(20):  
        randomNum = random.randint(0, 255) 
        charPass = chr(randomNum)
        passwdDiff = passwdDiff + charPass
    print(passwdDiff)

#generaPasswordDiff()


def generaPasswordFac():
    passwdFac = ""
    charPass = ""
    charNum = ""
    charMaui = ""
    rNum = ""
    rMaiu = ""
    rChar = ""
    temp = ""
    for i in range(8):
        rMaiu = random.randint(65, 90)
        rChar = random.randint(97, 122)
        rNum = random.randint(48, 57)
        charPass = chr(rChar)
        charNum = chr(rNum)
        charMaui = chr(rMaiu)
        temp = charPass + charNum + charMaui
        passwdFac = passwdFac + random.choice(temp)
    print(passwdFac)
    
#generaPasswordFac()


def genera_pass_cedro():
    passwced = ""
    charPass = ""
    rChar = ""
    while passwced != "cedro":
        passwced = ""
        for i in range(5):
            rChar = random.randint(97, 122)
            charPass = chr(rChar)
            passwced = passwced + charPass
        print(passwced + " ")
        
#genera_pass_cedro()


def genera_cedro():      
    target = "cedro"  
    passwced = ["*"] * len(target)  
    for i in range(len(target)):
        while passwced[i] != target[i]: 
            rChar = chr(random.randint(97, 122))  
            if rChar == target[i]:  
                passwced[i] = rChar
            print("".join(passwced)) 
            time.sleep(0.07)  

#generacedro()


