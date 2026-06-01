import os
import sys

# Añade la carpeta `src` al path para poder importar Q_PERSONA
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from domain.model.Q_PERSONA import Q_PERSONA


def test_get_name():
    p = Q_PERSONA("Ana", 30, True, "Estudiante")
    assert p.F_GET_NAME() == "Ana"


def test_get_age():
    p = Q_PERSONA("Ana", 30, True, "Estudiante")
    assert p.F_GET_AGE() == 30


def test_is_alive():
    p = Q_PERSONA("Ana", 30, True, "Estudiante")
    assert p.F_IS_ALIVE() is True
