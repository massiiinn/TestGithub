"""
Exercici 1: Cerca d’Elements:
m_ex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

“””
Nom de la funció: cercar_el
Paràmetres:
    - matriu: Llista de dues dimensions (list)
    - element: Element a cercar (int)
    - mostrar_posicio: Booleà que indica si volem la posició 
(bool, opcional, per defecte False)
Retorna:
    - tupla: (bool, (tupla)) -> (trobat, (fila, columna)) 
si mostrar_posicio és True
             (bool, None) -> (trobat, None) 
si mostrar_posicio és False, o bé no l’ha trobat
Funcionalitat: 
    Cerca un element en una matriu i retorna si s'ha trobat i opcionalment la seva posició, sino el troba 
“””

Fes la funció indicada amb una crida on passes com a paràmetres m_ex, 10 i una crida amb m_ex, 1 i True
"""

def cercar_el(matriu,element, mostrar_posicio=False):
    trobat =False
    for i in range(len(matriu)):
        for j in range(len(matriu[i])):
            if matriu[i][j] == element:
                trobat = True
                if mostrar_posicio:
                    
                    return (trobat, (i,j))
                else:
                    return (trobat, None)
                
    return (trobat,None)


"""Nom de la funció: sumar_fila
Paràmetres:
    - matriu: Llista de dues dimensions (list)
    - index: índex de la fila que volem sumar, per defecte 0
Retorna:
    - int: la suma dels elements de la fila indicada per index
Funcionalitat:
Comprova que index correspon a una fila correcta, en aquest cas retorna la suma de tots els elements en la fila indicada, sinó retorna 0,  

m_ex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Fes exemples de crida amb els paràmetres m_ex i 2, i m_ex i 10 i imprimeix el resultat. Posa en comentari que sortirà per consola.
"""

def sumar_fila(matriu, index=0):
    
    if 0<=index<len(matriu) or -1>=index>=-len(matriu):
        return sum(matriu[index])
    else:
        return None
    

"""
Nom de la funció: sumar_matriu
Paràmetres:
    - matriu: Llista de dues dimensions (list)
Retorna:
    - int: la suma tots els elements de la matriu
Funcionalitat:
Utilitza obligatòriament la funció anterior per sumar totes les files de la matriu i retornar el total.  

m_ex = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Fes l’exemple de crida amb el paràmetre m_ex. Imprimeix per consola el resultat.
"""


def sumar_matriu(matriu):
    total=0
    for i in range(len(matriu)):
        total += sumar_fila(matriu,i)
        
    return total

"""
Nom de la funció: transformar
Paràmetres:
    - matriu: Llista de dues dimensions (list)
    - k: constant (int)
    - op: operació que s’aplicarà a cada element, per defecte  “+”   
          (string)
Retorna:
    - None 
Funcionalitat:
Aplica l’operació indicada amb la constant a tots els elements de la matriu.

Les operacions permeses són +, -, *, i /

transformar(m_ex, 10, “+”) sumarà 10 a tots els elements de la matriu m_ex. 
transformar(m_ex, 10, “-”) restarà 10 a tots els elements de la matriu m_ex. 
transformar(m_ex, 10, “*”) multiplicarà per 10 tots els elements de la matriu m_ex. 
transformar(m_ex, 10, “/”) dividirà per 10 a tots els elements de la matriu m_ex. 
si l’operació no és vàlida no farà res.

"""

def transformar(matriu,k,op):
    
    for i in range(len(matriu)):
        for j in range(len(matriu[i])):
            if op == "+":
                matriu[i][j] += k
            elif op == "-":
                matriu[i][j] -= k
            elif op == "*":
                matriu[i][j] *= k
            elif op == "/":
                matriu[i][j] /= k