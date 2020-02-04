# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 17:45:52 2020

@author: Pablo Sergio Petito
"""


class InicializaWeb():
    
    estado = False
    nombreDriver=""
    nombreweb=""    
        
    def __init__(self, estado, nombreDriver, nombreWeb):
        self.__estado=estado
        self.__nombreDriver=nombreDriver
        self.__nombreWeb=nombreWeb
        
    def inicializa(self):

        return driver;