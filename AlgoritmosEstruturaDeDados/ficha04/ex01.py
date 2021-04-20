# 1.	Implementar um método recursivo para listar os números inteiros positivos de 1 a 50
def countup(n):
    if n >= 1:
        countup(n - 1)
        print(n)
        
countup(50)

# 2.	Implemente um método recursivo que receba um inteiro positivo N
#  e calcule a soma dos números pares inteiros de 0 a N 
print("\nexercício 02")
def conta_pares(n):
    if n == 0:
        return n # 0 é par
    elif n%2 == 0:
        return n + conta_pares(n-1)
    else:
        return conta_pares(n-1)

print(conta_pares(5))


print("\nexercício 03")
#3.	Escreva uma função recursiva, somaSerie(i,j,k: inteiro): inteiro, que devolva a
#  soma da série de valores do intervalo [i,j], com incremento k.
def somaSerie(i,j,k):
    if j < i:
        return 0
    elif j == i:
        return j
    else:
        return j + somaSerie(i,(j-k),k)
print(somaSerie(0,10,4))


print("\nexercício 04")
# 4.	Exponenciação: escreva uma função recursiva expRec(x,y: inteiro),
# que devolva o exponencial de x por y (xy).

def expRec(x, y):
    if y == 0:
        return 1
    if y >= 1:
        return x * expRec(x, y - 1)

print(expRec(3,2))

print("\nexercício 05")
# 5.	Implemente o algoritmo de Euclides de forma recursiva: recebe dois inteiros positivos e devolve o maior
#  divisor comum -  pesquise na internet o cálculo de Euclides em que mdc(a,b) = mdc(b,a%b) para b != 0 e mdc(a,0)=a.
def mdc(n,m):

    # Algoritmo de Euclides
    anterior = n
    atual    = m
    resto    = anterior % atual

    while resto != 0:
        anterior = atual
        atual    = resto
        resto    = anterior % atual

    print("MDC(%d,%d)=%d" %(n,m,atual))

mdc(8,5)