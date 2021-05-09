import re

def sintaxAnalyzer(tokens):
    valido = True
    n=len(tokens)
    print(n)
    i=0
    while (i < n and valido):
        if (tokens[i] == 'while'):
            if(i + 5< n): 
                cad = str(tokens[i+1]) + str(tokens[i+2])+str(tokens[i+3])+str(tokens[i+4])+str(tokens[i+5])
                print(cad)
                valido = revisaExpresion(cad)
                i=i+5
                if ( i + 1 <n and ~valido):
                    cad = cad + str(tokens[i])
                    valido = revisaExpresion(cad)
            else:
                valido = False
        else:                
            i=i+1    
    return valido


def revisaExpresion(cad):
    res = re.search("\(([a-zA-Z]|[0-9])(<|>|<=|>=|==|!=)([a-zA-Z]|[0-9])\)",cad)
    return res != None

def test():
    p1 = ['while', '(' , 'a', '==', 'b',')','{','while','(','7','<','8',')','}']
    p2 = ['while', '(' , 'a', '==', 'b',')','{','while','(','while','<','8',')','}']
    p3 = ['while', '(' , 'a', '==', 'b',')','{','while','(','7','while','8',')','}']
    p4 = ['while', '(' , 'a', '==', 'b',')','{','while','(','7','<','8','9','}']
    p5 = ['while', '(' , 'a', '==', 'b',')','{','while','7','7','<','8',')','}','a']
    print(sintaxAnalyzer(p1))
    print(sintaxAnalyzer(p2))
    print(sintaxAnalyzer(p3))
    print(sintaxAnalyzer(p4))
    print(sintaxAnalyzer(p5))

