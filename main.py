
def columnCalc(n, i, tabela, j=0, coluna=None):

    if coluna is None:
        coluna = []

    if j == n-i-1:
        return coluna

    v = tabela[i][j] - tabela[i][j+1]
    coluna.append(round(v, 2))

    return columnCalc(n, i, tabela, j+1, coluna)


def babbage(eixo_y, n=None, tabela=None, i=0):

    if n is None:
        n = len(eixo_y)
    
    if tabela is None:
        tabela = [eixo_y]  
    
    if i == (n-1):
        return tabela
        
    tabela.append(columnCalc(n, i, tabela))

    return babbage(eixo_y, n, tabela, i+1)



def polinomio(x, coeficientes, soma=0, i=0):

    grau = len(coeficientes)-1
    if(i == grau):
        return soma

    soma += coeficientes[i] * (x**(grau-i))
    i += 1

    return polinomio(x, coeficientes, soma, i)


def findDiff(eixo_x, diffs = [], i=0):

    rang = len(eixo_x) - 1
    if(i == rang):
        if diffs[-1] != diffs[0]:
            return  
        return diffs[0]

    diffs.append(round(eixo_x[i + 1] - eixo_x[i], 2))

    i += 1

    return findDiff(eixo_x, diffs, i)


def completeTillGetValue(eixo_x, v, diff):
    
    new_value = eixo_x[-1] + diff
 
    eixo_x.append(new_value)

    if(round(new_value, 2) == v):
        return eixo_x

    return completeTillGetValue(eixo_x, v, diff)


coeficientes = list(map(float, input("Digite os coeficientes do polinômio separado por espaço: ").split()))

eixo_x = list(map(float, input("Digite os valores de eixo_x separado por espaço: ").split()))

entrada = float(input("Digite o valor de entrada para o x: "))

diff = findDiff(eixo_x)

eixo_x = completeTillGetValue(eixo_x, entrada, diff)

print(eixo_x)

eixo_y = []
for x in eixo_x:
    eixo_y.append(polinomio(x, coeficientes))

diffs = babbage(eixo_y)

print("tabela de diferenças:")
for c, linha in enumerate(diffs):
    print(f"nível {c}: {linha}")
