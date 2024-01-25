
import subprocess
import numpy as np
import random
from random import randint
import os

#MAE e o airfoil que sera evoluido
#SON sao os airfoils evoluidos baseados na MAE

def main():

    mae = np.loadtxt("Naca0010.txt",skiprows=1)
    geraMae(mae,mae,-1,-1)
    son = []
    geracoes = 1000
    reynolds = "3e6"
    faixaangular = "0 15 1" #angulo inicial / final / incremento

    evo(mae,son,geracoes,reynolds,faixaangular)
    subprocess.call("xfoil.exe < ScriptFinal.txt", shell=True)


def evo(mae,son,geracoes,reynolds,faixaangular) -> None:
    #Simula Airfoil Mae
    script("Mae.txt",reynolds,faixaangular)
    subprocess.call("xfoil.exe < Script.txt", shell=True)
    coeficientemae = np.loadtxt("Polar.txt",skiprows=12,usecols=(1,2))
    
    for i in range(geracoes):
        for j in range(4):
            geraSon(mae,son,i,j)

            #Simula Airfoil Son
            script("Son.txt",reynolds,faixaangular)
            subprocess.call("xfoil.exe < Script.txt", shell=True)
            coeficienteson = np.loadtxt("Polar.txt",skiprows=12,usecols=(1,2))
            
            if (torneio(coeficientemae,coeficienteson)):
                geraMae(mae,son,i,j)   
                coeficientemae = coeficienteson
        
def script(airfoilfile,reynolds,faixaangular) -> None:
    if os.path.exists("Polar.txt"):
        os.remove("Polar.txt")

    arquivo = open("Script.txt",'w') 
    arquivo.write(f"load {airfoilfile}\n")
    arquivo.write("pane\n")
    arquivo.write("oper\n")
    arquivo.write(f"visc {reynolds}\n")
    arquivo.write("iter 100\n")
    arquivo.write("seqp\n")
    arquivo.write("pacc\n")
    arquivo.write("Polar.txt\n\n")
    arquivo.write(f"aseq {faixaangular}\n")
    arquivo.write("\n")
    arquivo.write("quit\n")
    arquivo.close()

def geraMae(mae,novomae,i,j) -> None:
    arquivo = open("Mae.txt",'w')
    arquivo.write(f"MAE ARFOIL {i}-{j}")
    for i in range(35):
        mae[i][0] = novomae[i][0]
        mae[i][1] = novomae[i][1]
        arquivo.write(f"\n{novomae[i][0]:.5f}     {novomae[i][1]}")
    arquivo.close() 

def geraSon(mae,son,i,j) -> None:
    son.clear()
    random.seed()
    arquivo = open("Son.txt","w")
    arquivo.write(f"SON 00 {i}{j}")

    for i in range(35):
        x=mae[i][0]
        
        if randint(0,10)/7 == 1 and i != 17:
            y=mae[i][1]*(randint(9000,10999)/10000)
        else:
            y=mae[i][1]

        son.append([x,y])
        arquivo.write(f"\n{son[i][0]:.5f}")
        arquivo.write(f"     {son[i][1]}")
    arquivo.close()

def torneio(coeficientemae,coeficienteson) -> bool:
    j=0
    try:
        for i in range(16):
            if (coeficienteson[i][0] - coeficienteson[i][1]) >= (coeficientemae[i][0] - coeficientemae[i][1]):
                j+=1
    except:   
        return False

    if(j>7):
        return True
    else:
        return False



if __name__ == "__main__":
   main()




