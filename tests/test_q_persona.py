import os
import sys

# Añade la carpeta `src` al path para poder importar Q_PERSONA
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from domain.model.Q_PERSONA import Q_PERSONA
from domain.service.Q_EVALUAR import Q_EVALUAR
from domain.model.E_TIPO_PRESTAMO import E_PRESTAMO
from domain.model.E_PRESTAMO import E_PRESTAMO as E_PRESTAMO_RESULTADO

#------------PRUEBA GREEN----------------
def test_credit_approv():
    p = Q_EVALUAR("Ana", 30, True, "Estudiante", 80) 
    assert p.F_EVALUAR() == E_PRESTAMO_RESULTADO.APROBADO
