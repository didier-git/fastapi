from abc import ABC, abstractmethod


class CalificacionStrategy(ABC):

    @abstractmethod
    def calcular_nota_estudiante(self,numero_de_asistencia : int,numero_de_participaciones : int , nota_evaluacion: int) -> float:
        pass


class PregadoEstrategy (CalificacionStrategy):

    def calcular_nota_estudiante(self,numero_de_asistencia: int, numero_de_participaciones: int, nota_evaluacion: int)-> float:
        return nota_evaluacion + (numero_de_asistencia * (10.0/100))

class PosgradoStrategy(CalificacionStrategy):
    def calcular_nota_estudiante(self,numero_de_asistencia: int, numero_de_participaciones: int, nota_evaluacion: int)-> float:
        return nota_evaluacion + (numero_de_asistencia * (20.0/100))
