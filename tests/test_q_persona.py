import os
import sys

# Añade la carpeta `src` al path para poder importar Q_PERSONA
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from domain.model.Q_PERSONA import Q_PERSONA
from domain.service.Q_EVALUAR import Q_EVALUAR
from domain.model.E_TIPO_PRESTAMO import E_PRESTAMO
from domain.model.E_PRESTAMO import E_PRESTAMO as E_PRESTAMO_RESULTADO
import pytest

#------------PRUEBA GREEN----------------
def test_credit_approv():
    # Arrange
    applicant = Q_EVALUAR("Ana", 30, True, "Estudiante", 80)

    # Act
    resultado = applicant.F_EVALUAR()

    # Assert
    assert resultado == E_PRESTAMO_RESULTADO.APROBADO


#------------PRUEBA RED----------------
def test_loan_tipe():
    # Arrange
    applicant = Q_EVALUAR("Ana", 30, True, "Estudiante", 80)

    # Act
    tipo = applicant.F_EVALUAR_TIPO_PRESTAMO()

    # Assert
    assert tipo == E_PRESTAMO.R_PRESTAMO_DENEGADO


@pytest.mark.parametrize("age, alive, score, expected", [
    (17, True, 80, E_PRESTAMO.R_PRESTAMO_ESPECIAL),
    (18, True, 80, E_PRESTAMO.R_PRESTAMO_DENEGADO),
    (30, True, 80, E_PRESTAMO.R_PRESTAMO_DENEGADO),
    (40, True, 80, E_PRESTAMO.R_PRESTAMO_REGULAR),
    (59, True, 80, E_PRESTAMO.R_PRESTAMO_REGULAR),
    (60, True, 80, E_PRESTAMO.R_PRESTAMO_DENEGADO),
    (30, True, 60, E_PRESTAMO.R_PRESTAMO_DENEGADO),
    (30, False, 80, E_PRESTAMO.R_PRESTAMO_DENEGADO),
])
def test_tipo_prestamo_param(age, alive, score, expected):
    # Arrange
    applicant = Q_EVALUAR("Ana", age, alive, "Estudiante", score)

    # Act
    result = applicant.F_EVALUAR_TIPO_PRESTAMO()

    # Assert
    assert result == expected