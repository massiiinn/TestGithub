from prova_escrita_03 import *
from prova_escrita_04 import *
import unittest
class TestProvaEscrita03(unittest.TestCase):
    def test_trobar_min_max_rendiment(self):
        """
        Comprovació de trobar el màxim i el mínim d'uns valors.
        """
        minim,maxim=trobar_min_max_rendiment(10.50, 12.00, 15.00)
        self.assertEqual(minim, 10.50)
        self.assertEqual(maxim, 15.00)
        
    def test_comptar_estudiants(self):
        """
        Comprovació per comptar els alumnes d'un
        diccionari utilitzant 'len'.
        """
        len(notes_estudiants)
        self.assertEqual(len(notes_estudiants), 4)
        
    def test_comptar_estudiants_matèria_v2(self):
        """
        Comprovació per comptar els estudiants en una matèria.
        """
        notes_estudiants = {
            "Anna": {"Matemàtiques": 8, "Història": 7}, 
            "Marc": {"Matemàtiques": 6}, 
            "Laura": {"Ciències": 9, "Matemàtiques": 10}, 
            "Jordi": {"Història": 5}
        } 
        resultat=comptar_estudiants_matèria_v2(notes_estudiants, "Matemàtiques")
        self.assertEqual(resultat, 3)

class TestProvaEscrita04(unittest.TestCase):
    def test_cercar_el(self):
        """
        Comprovació que un element és troba en una matriu.
        """
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        resultat = cercar_el(matriu, 5, mostrar_posicio=True)
        self.assertEqual(resultat, (True, (1, 1)))
        
    def test_sumar_fila(self):
        """
        Comprovació suma de files.
        """
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        resultat=sumar_fila(matriu, 0)
        self.assertEqual(resultat,6)
        resultat = sumar_fila(matriu, 1)
        self.assertEqual(resultat,15)
        resultat = sumar_fila(matriu, 2)
        self.assertEqual(resultat,24)
        resultat = sumar_fila(matriu, -1)
        self.assertEqual(resultat,24)
        resultat = sumar_fila(matriu, -2)
        self.assertEqual(resultat,15)
        resultat = sumar_fila(matriu, -3)
        self.assertEqual(resultat,6)
        resultat = sumar_fila(matriu, -4)
        self.assertEqual(resultat, None)
        resultat = sumar_fila(matriu, 4)
        self.assertEqual(resultat, None)
        
    def test_sumar_matriu(self):
        """
        Comprovació de la funció suma de matriu
        """
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        resultat= sumar_matriu(matriu)
        self.assertEqual(resultat, 45)
    
    def test_transformar(self):
        """
        Comprovació de la funció transformar
        pasant com a parametre l'operació a fer
        """
        # Suma
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        transformar(matriu, 2, "+")
        resultat = matriu
        self.assertEqual(resultat, [[3, 4, 5], [6, 7, 8], [9, 10, 11]])
        # Resta
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        transformar(matriu, 2, "-")
        resultat = matriu
        self.assertEqual(resultat, [[-1, 0, 1], [2, 3, 4], [5, 6, 7]])
        # Multiplicació
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        transformar(matriu, 2, "*")
        resultat = matriu
        self.assertEqual(resultat, [[2, 4, 6], [8, 10, 12], [14, 16, 18]])
        # Divisió 
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        transformar(matriu, 2, "/")
        resultat = matriu
        self.assertEqual(resultat, [[0.5, 1, 1.5], [2, 2.5, 3], [3.5, 4, 4.5]])
        

if __name__ =="__main__":
    unittest.main()