from prova_escrita_06 import *
import pytest

biblioteca = [
    {
        "llibre": "El Quixot",
        "autor": "Cervantes",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Joan", "dies": 15, "retornat": True},
            {"usuari": "Maria", "dies": 20, "retornat": False},
            {"usuari": "Pere", "dies": 12, "retornat": True}
        ]
    },
    {
        "llibre": "1984",
        "autor": "Orwell",
        "categoria": "ciència-ficció",
        "prestecs": [
            {"usuari": "Pere", "dies": 10, "retornat": True},
            {"usuari": "Anna", "dies": 25, "retornat": True},
            {"usuari": "Marta", "dies": 18, "retornat": False}
        ]
    },
    {
        "llibre": "El Senyor dels Anells",
        "autor": "Tolkien",
        "categoria": "fantasia",
        "prestecs": [
            {"usuari": "Maria", "dies": 30, "retornat": True},
            {"usuari": "Joan", "dies": 22, "retornat": True},
            {"usuari": "Pere", "dies": 15, "retornat": False}
        ]
    },
    {
        "llibre": "Crim i Càstig",
        "autor": "Dostoievski",
        "categoria": "novel·la",
        "prestecs": [
            {"usuari": "Anna", "dies": 28, "retornat": True},
            {"usuari": "Marta", "dies": 14, "retornat": True},
            {"usuari": "Joan", "dies": 21, "retornat": True}
        ]
    }
]

@pytest.mark.parametrize("categoria, esperat", [("novel·la", ["El Quixot", "Crim i Càstig"]),("ciència-ficció", ["1984"]),("fantasia", ["El Senyor dels Anells"]),("història", [])])
#Damos a pytest la categoria y lo esperado de ella
def test_llibres_per_categoria(categoria, esperat):
    """
    Test para la función llibres_per_categoria. Comprovación de retorno de libros
    """
    assert llibres_per_categoria(biblioteca, categoria) == esperat

@pytest.mark.parametrize("llibre, esperat", [("El Quixot", False),("1984", False),("El Senyor dels Anells", False),("Crim i Càstig", True)])
#Damos a pytest el titulo del libro y lo esperado (true or false)
def test_esta_disponible(llibre, esperat):
    """
    Test para la función esta_disponible. Comprovación con True or False.
    """
    assert esta_disponible(biblioteca, llibre) == esperat

@pytest.mark.parametrize("usuari, esperat", [("Joan", False),("Maria", True),("Pere", True),("Anna", False)])
#Damos a pytest el usario para comprovar el prestamo y lo esperado (true or false)
def test_usuari_te_prestecs(usuari, esperat):
    """
    Test para la función usuari_te_prestecs. Comprovación de si un usuario tiene un prestamo (True) o no (False)
    """
    assert usuari_te_prestecs(biblioteca, usuari) == esperat

@pytest.mark.parametrize("llibre, esperat", [("El Quixot", 47),("1984", 53),("El Senyor dels Anells", 67),("Crim i Càstig", 63)])
#Damos a pytest el usario para comprovar el prestamo y lo esperado (true or false)
def test_dies_prestec_total(llibre, esperat):
    """
    Test para la función dies_prestec_total. Comprovación del total de dias
    """
    assert dies_prestec_total(biblioteca, llibre) == esperat
