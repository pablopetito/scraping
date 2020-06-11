# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:34:05 2019

@author: Pablo Sergio Petito
"""

#paquetes externos
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import datetime 
import time
import sys
import re

#paquetes propios

#funciones
def textoSolo(texto):
    patron = re.compile('\s')
    palabra = patron.split(texto)
    patron2 = '[A-Z][a-z]+'
    matcher = re.findall(patron2, texto)
    palabrafinal=""
    for tx in matcher:
        palabrafinal = palabrafinal + " " + tx 
    return palabrafinal  

def numeroSolo(numero):
    patron = '[0-9]+'
    numero2=re.findall(patron, numero)
    final=""
    for nro in numero2:
        final = final + nro
    return final 

#hora Inicial
hrsInicial=datetime.datetime.now()
print("Inicio de la Extraccion: ", hrsInicial)

#setEntornoWeb
useDriver="chromedriver.exe"
useWeb="https://www.argenprop.com.ar"

#iniciaWebDriver
driver=webdriver.Chrome(useDriver)
driver.get(useWeb)

# --- Esperar un tiempo que se cargue la pagina ---
time.sleep(2)

# --- Maximiza Navegador
driver.maximize_window()

# --- Inicializa variables a utilizar
i=1
j=1

element = driver.find_element_by_xpath("//*[@id='home-ubicacion']")
element1 = element.send_keys("Capital Federal")
time.sleep(2)
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ENTER)

# --- tiempo de espera
time.sleep(2)

# --- Presiona boton Cancelar de una ventana emergente
#element = driver.find_element_by_xpath("//*[@id='suggestAlertPopup']/div/form/button[2]").click()

# --- tiempo de espera 
time.sleep(3)

# --- Borra todos los filtros de la busquedad
element = driver.find_element_by_xpath("/html/body/main/div[2]/sidebar/div[1]/div/button").click()

# --- Recolectar link PAISES 
#//*[@id="argentina"]
#//*[@id="locationFilter"]/ul[1]/li[1]
#/html/body/main/div[1]/sidebar/div[4]/div/div[1]/div/div[2]/ul[1]/li[1]/a

time.sleep(2)
paisArgentina = driver.find_element_by_xpath('//*[@id="argentina"]').text
paisUruguay = driver.find_element_by_xpath('//*[@id="uruguay"]').text

paises2 = driver.find_element_by_xpath('//*[@id="locationFilter"]/ul[1]').text
allPaises = driver.find_elements_by_xpath('//*[@id="locationFilter"]/ul[1]/li')
todosPaises = []
for paisesNom in allPaises:
    todosPaises.append(paisesNom.text)

time.sleep(2)

#   **** Paises ****
paises_nom = []
paises_avisos = []

for nombre in todosPaises:
    paises_nom.append(textoSolo(nombre))   
    paises_avisos.append(numeroSolo(nombre))

for i in range(len(paises_nom)):
    print(paises_nom[i] + ": " + paises_avisos[i])
    pais = paises_nom[i].strip().lower()
    
    # INGRESA A LOS  AVISOS DEL PAIS
    element = driver.find_element_by_xpath('//*[@id=\'{}\']'.format(pais)).click()
    
    time.sleep(2)

#   **** Localidades ****
    allLocalidades = driver.find_elements_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/div/div[2]/ul[1]/li')
    todosLocalidades = []
    for localidadNom in allLocalidades:
        todosLocalidades.append(localidadNom.text)

        localidades_nom = []
        localidades_avisos = []
        
        for nombre in todosLocalidades:
            localidades_nom.append(textoSolo(nombre))   
            localidades_avisos.append(numeroSolo(nombre))
            j=1
            for j in range(len(localidades_nom)):
                print(localidades_nom[j] + ": " + localidades_avisos[j])
                localidad = localidades_nom[j].strip().lower()
                
                # INGRESA A LOS  AVISOS DE LA LOCALIDAD
                element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/div/div[2]/ul[1]/li[{}]'.format(j+1)).click()
                
                time.sleep(2)              
             
                #BARRIO
                element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/form/div/div[2]/ul[1]/li[{}]/span'.format(j+1)).click()
                elem_barrio = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/form/div/div[2]/ul[1]/li[{}]/label/span/a'.format(j+1)).text
                barrio = textoSolo(elem_barrio).strip()
                barrio_cant = numeroSolo(elem_barrio)
                
                time.sleep(2)
                
                #SUB-BARRIO
                element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/form/div/div[2]/ul[1]/li[{}]/ul/li[1]/label/span/a'.format(j+1)).click()
                elem_subBarrio = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/form/div/div[2]/ul[1]/li[{}]/ul/li[1]/label/span/a'.format(j+1)).text
                subBarrio = textoSolo(elem_subBarrio).strip()
                subBarrio_cant = numeroSolo(elem_subBarrio)
                
                print(barrio + ": " + barrio_cant)
                print(subBarrio + ": " + subBarrio_cant)

                #Tipo de Operacion
                elem_tipo_operacion = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul/li[1]/a').text
                element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul/li[1]/a').click()
                tipo_operacion = textoSolo(elem_tipo_operacion).strip()
                tipo_operacion_cant = numeroSolo(elem_tipo_operacion)
                
                print(tipo_operacion + ": " + tipo_operacion_cant)
                
                time.sleep(4)
                
                
                for x in range(20):
                    
                    #BOTON MAS TIPO DE PROPIEDAD
                    element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/button').click()
                
                    time.sleep(2)
                
                    #TIPO DE PROPIEDAD 
                    tipo_propiedad = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul[1]/li[2]/a').text
                    element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul[1]/li[{}]/a'.format(x+1)).click()
                
                    print(tipo_propiedad)
                                  
                    time.sleep(3)
                    
                    
                    #BOTON CANCELAR - ALERTA BUSQUEDAD
                    try:
                        element = driver.find_element_by_xpath('/html/body/main/div[4]/button[2]').click()
                    except:
                        element=""
                        
                    for y in range(4):    
                        calle = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/div[1]/h2'.format(y+1)).text
                        print(calle)
                
                        detalle_Principal = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/h3'.format(y+1)).text
                        print(detalle_Principal)
                
                        sub_Detalle = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/p[1]'.format(y+1)).text
                        print(sub_Detalle)
                
                        detalle_detallado = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/p[2]'.format(y+1)).text
                        print(detalle_detallado)
                
                        importe_moneda_Operacion = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[1]/div[2]/p[1]'.format(y+1)).text
                        print(importe_moneda_Operacion)
                
                
                        try:
                            expensas = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[1]/div[2]/p[2]'.format(y+1)).text
                        except:
                            expensas = ""
                    
                        print(expensas)
                
                    #Elimina Tipo de la Propiedad    
                    element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[1]/div/ul/li[1]/h2/span').click()
  
    #-------------------------------------
                sys.exit()
                #BOTON MAS TIPO DE PROPIEDAD
                element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/button').click()
                
                time.sleep(2)
                
                #TIPO DE PROPIEDAD 
                tipo_propiedad = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul[1]/li[2]/a').text
                element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul[1]/li[2]/a').click()
                
                print(tipo_propiedad)
                
                sys.exit()
                
                time.sleep(3)
                
                
                
                #Elimina Sub-Barrio
                element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[1]/div/ul/li[3]/h2/span').click()
                
                
                
                
                               
                
                
                #TIPO DE PROPIEDAD 
                element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul[1]/li[2]/a').click()
                tipo_propiedad = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul[1]/li[2]/a').text
                
                print(tipo_propiedad)
                
                sys.exit()
                
                #otro.SUB-BARRIO
                element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/form/div/div[2]/ul[1]/li[{}]/ul/li[2]/label/span/a'.format(j+1)).click()
                elem_subBarrio = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/form/div/div[2]/ul[1]/li[{}]/ul/li[2]/label/span/a'.format(j+1)).text
                subBarrio = textoSolo(elem_subBarrio).strip()
                subBarrio_cant = numeroSolo(elem_subBarrio)
                
                print(barrio + ": " + barrio_cant)
                print(subBarrio + ": " + subBarrio_cant)
                sys.exit()

# --- Cierra navegador 
driver.close()

#hora Final
hrsFin=datetime.datetime.now()
print("Hora Final de la Extraccion: ", hrsFin)
print("Tiempo trasncurrido de la Extraccion: ", hrsFin - hrsInicial)