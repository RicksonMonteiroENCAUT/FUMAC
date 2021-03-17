"""
@author: Rickson Gomes Monteiro
BackWard Euler

"""
#importação de bibliotecas
import numpy as np
import matplotlib.pyplot as plt
#Delta t
dt=0.2
#respostas
resps_X=[]
saidas_Y=[]

#Gera sequência de numeros de 0 até 5 em um intervalo de dt (5.2 não é incluso)
tempo=np.arange(0,5+dt,dt)

#Calculo da matriz Ad (A discreta)
A=np.array([[0, 1],
           [-29, -4]])
Ad= np.linalg.inv(np.eye(2) - dt*A)
#print(Ad)

#Calculo da Matriz Bd (B discreta)
B=np.array([[0],
            [1]])
Bd=np.matmul(Ad, dt*B)
#print(Bd)

#Solução analítica:
def y_analitica(t):
    return (8/29 -(8/29)*np.exp(-2*t)*(np.cos(5*t) - (13/40)*np.sin(5*t)))

#função para a apresentação dos resultados em
def graficos(y, x=tempo):
    k=0
    print("SAÍDAS- BackWard Euler")
    for i in y:
        print("t={:.2f}s: {}".format(k, i))
        k += 0.2

    plt.plot(x,y,'b', label='Sol. Numeric.')
    plt.plot(x, y_analitica(x), 'r', label='Sol. Analt.')
    plt.legend(loc="lower right")
    plt.title('Gráfico para delta-t = 0.2s')
    plt.xticks(np.arange(0,5.5,0.5))
    plt.xlabel('Tempo')
    plt.ylabel('Saída')
    plt.show()



#função degrau
def u(t):
    if t<=0:
        return 0
    else:
        return 1

#backward-euler
def x(t):
    if t<=0:
        return np.zeros((2,1))
    else:
        return np.matmul(Ad,x(t-dt)) +Bd*u(t)

def y(x):
    return np.matmul([8,1],x)


for t in tempo:
    resps_X.append(x(t))
    saidas_Y.append(np.round(y(x(t))[0],4))

graficos(saidas_Y)


