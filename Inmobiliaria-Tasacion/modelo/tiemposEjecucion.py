# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:29:33 2020

@author: Pablo Sergio Petito
"""

class TiemposEjecucion():
    
    def __init__(self):
        self.__horaInicial=0
        self.__horaFinal=0
    
    def setHoraInicial(self,hrs):
        self.horaInicial=hrs
          
    def getHoraInicial(self):
        return "{}".format(self.getHoraInicial)
    
    def setHoraFinal(self,hrs):
        self.horaFinal=hrs
    
    def getHoraFinal(self):
        return self.getHoraFinal
    
    def tiempoTrascurrido(self):
        return self.horaFinal - self.horaInicial