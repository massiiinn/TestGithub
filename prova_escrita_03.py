"""
Seguiment de Rendiment Esportiu
Imagina que ets un entrenador d'un equip d'atletisme i vols analitzar els 
rendiments dels teus atletes en diverses competicions. 
Per a cada atleta, reculls les marques (temps) d'una competició i vols determinar quina ha estat la millor i la pitjor marca registrada.
m1 = 10.50
m2 = 12.00
m3 = 15.00
# … 

Trobar el Mínim i el Màxim d'una Col·lecció de Nombres (amb nombre variable de paràmetres)
Nom de la funció: trobar_min_max_rendiment
Paràmetres: 
nombres: Un nombre variable de nombres (float).
Retorna: (tupla): Una tupla amb la millor i la pijtor de les marques
Funcionalitat: Rep un nombre variable de paràmetres que són nombres decimals  i 
retorna el mínim, i el màxim dels nombres passats. 
Sinó hi ha cap marca per analitzar, retorna 0,0

Defineix la funció, i fes un exemple de crida, passant les variables m1, m2 i m3
La sortida  per consola de la crida hauria de ser:
La millor marca de 10.50, 12.00 i 15.00 és  10.50 i la pitjor és 15.00

"""

def trobar_min_max_rendiment(*nombres):
    if len(nombres) == 0:
        return 0, 0
    else:
        millor_rendiment = min(nombres)
        pitjor_rendiment = max(nombres)
        return millor_rendiment, pitjor_rendiment
    
"""
m1 = 10.50
m2 = 12.00
m3 = 15.00
millor_rendiment, pitjor_rendiment = trobar_min_max_rendiment(m1, m2, m3)

print(f"La millor marca de {m1}, {m2} i {m3} es {millor_rendiment} i la pitjor es {pitjor_rendiment}")
"""

"""
Imagina que estàs gestionant les notes d'un grup d'estudiants en un diccionari on les claus són els noms dels estudiants i els valors són les seves notes. 
notes_estudiants = {
    "Anna": {"Matemàtiques": 8, "Història": 7},
    "Marc": {"Matemàtiques": 6},
    "Laura": {"Ciències": 9, "Matemàtiques": 10},
    "Jordi": {"Història": 5},
}


Exercici 2:  Comptar Elements d’un diccionari 
Nom de la funció: comptar_estudiants
Paràmetres: 
estudiants: diccionari de les notes dels estudiants
Retorna: (int): El nombre d’estudiants que hi ha al dicconari
Defineix la funció, i fes un exemple de crida amb la variable notes_estudiants
La sortida  per consola de la crida hauria de ser: 
Hi ha 4 estudiants matriculats a l’institut.
"""

def comptar_estudiants(estudiants):
    return len(estudiants)

notes_estudiants = {
    "Anna": {"Matemàtiques": 8, "Història": 7}, 
    "Marc": {"Matemàtiques": 6}, 
    "Laura": {"Ciències": 9, "Matemàtiques": 10}, 
    "Jordi": {"Història": 5}} 

"""
print(f"Hi ha {comptar_estudiants(notes_estudiants)} estudiants matriculats a l'institut.")
"""

"""
Exercici 3: Comptar Estudiants amb Notes en Matèries Específiques
Nom de la funció: comptar_estudiants_matèria
Paràmetres:
notes: Un diccionari on les claus són noms d'estudiants i els valors són les seves notes (un altre diccionari amb matèries com a claus i notes com a valors).
matèria: el nom d’una materia
Retorna:
(int): El nombre d'estudiants que estan matriculats en aquesta matèria

Defineix la funció, i fes un exemple de crida amb la variable notes_estudiants, i la matèria “Matemàtiques”
La sortida  per consola de la crida hauria de ser: 
Hi ha 3 estudiant(s) matriculat(s) a la matèria Matemàtiques.
"""

def comptar_estudiants_matèria(notes, matèria):
    return len([estudiant for estudiant in notes if matèria in notes[estudiant]])

def comptar_estudiants_matèria_v2(notes, matèria):  
    comptador = 0
    for estudiant in notes:
        if matèria in notes[estudiant]:
            comptador += 1
    return comptador    
"""
print(f"Hi ha {comptar_estudiants_matèria(notes_estudiants, 'Matemàtiques')} estudiant(s) matriculat(s) a la matèria Matemàtiques.")    

print(f"Hi ha {comptar_estudiants_matèria_v2(notes_estudiants, 'Matemàtiques')} estudiant(s) matriculat(s) a la matèria Matemàtiques.")
"""