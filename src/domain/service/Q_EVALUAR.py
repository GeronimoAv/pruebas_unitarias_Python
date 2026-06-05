from domain.model.Q_PERSONA import Q_PERSONA
from domain.model.E_PRESTAMO import E_PRESTAMO

class Q_EVALUAR(Q_PERSONA):
    def __init__(V_EVALUAR, name, age, alive, occupation, V_PUNTAJE_C):
        super().__init__(name, age, alive, occupation, V_PUNTAJE_C)
    
    def F_EVALUAR(self):
        if self.V_PUNTAJE_C >= 70 and self.alive:
            return E_PRESTAMO.APROBADO
        else:
            return E_PRESTAMO.RECHAZADO
        
    def F_EVALUAR_TIPO_PRESTAMO(self):
        E_PRESTAMO_RESULTADO = self.F_EVALUAR()
        if E_PRESTAMO_RESULTADO == E_PRESTAMO.APROBADO and 18 > self.age < 40:
            return E_PRESTAMO.R_PRESTAMO_ESPECIAL
        

