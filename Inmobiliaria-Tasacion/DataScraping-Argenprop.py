# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:07:13 2021

@author: User
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

def busquedadInicial():
    element = driver.find_element_by_xpath("//*[@id='home-ubicacion']")
    element1 = element.send_keys("Capital Federal")
    time.sleep(4)
    element.send_keys(Keys.ARROW_DOWN)
    element.send_keys(Keys.ENTER)
    element = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div[2]/form[1]/button").click()    
    return element

def borraFiltros():
    element = driver.find_element_by_xpath("/html/body/main/div[2]/sidebar/div[1]/div/button").click()
    return element

def recolctaPaises(indice):
    allPaises = driver.find_elements_by_xpath('//*[@id="locationFilter"]/ul[{}]/li'.format(indice)) 
    todosPaises = []                                        
    for paisesNom in allPaises:                             
        todosPaises.append(paisesNom.text)
    return todosPaises

def recolctaBarrios(indice):
    allPaises_2 = driver.find_elements_by_xpath('//*[@id="locationContainer"]/ul[{}]/li'.format(indice))
    todosPaises_2 = []
    for paisesNom in allPaises_2:
        todosPaises_2.append(paisesNom.text)
    return todosPaises_2    

def ingresarPais(indice, tipoUl):
    element = driver.find_element_by_xpath('//*[@id="locationFilter"]/ul[{}]/li[{}]/label/span'.format(tipoUl,indice)).click()
    return element

def ingresarBarrio(indice, tipoUl):
    element = driver.find_element_by_xpath('//*[@id="locationContainer"]/ul[{}]/li[{}]/label/span'.format(tipoUl,indice)).click()
    element2 = driver.find_element_by_xpath('//*[@id="locationApply"]').click()
    return element

#Operacion Venta / Alquiler
def ingresarOperacion(indice):
    element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/form/div/div[3]/div/div/ul[1]/li[{}]/label/span'.format(indice)).click()
    time.sleep(2)
    element2= driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/form/div/div[3]/div/button[2]').click()
    return element

#Tipo de Operaciones 
def recolectaTipoProp(indice):
    allTipoProp = driver.find_elements_by_xpath('//*[@id="tipopropiedadFilter"]/ul[{}]/li'.format(indice))
    todosTipoProp = []
    for tipoPropNom in allTipoProp:
        todosTipoProp.append(tipoPropNom.text)
    return todosTipoProp

def ingresarTipoProp(indice, tipoUl):                                          
    element = driver.find_element_by_xpath('//*[@id="tipopropiedadFilter"]/ul[{}]/li[{}]/label/span'.format(tipoUl,indice)).click()                                      
    time.sleep(2)
    element2= driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/form/div/div[4]/div/button').click()
    return element

### INICIO ###

# hora Inicial
hrsInicial=datetime.datetime.now()
print("Inicio de la Extraccion: ", hrsInicial)

# setEntornoWeb
useDriver="chromedriver.exe"
useWeb="https://www.argenprop.com.ar"

# inicia WebDriver
driver=webdriver.Chrome(useDriver)
driver.get(useWeb)

# --- Esperar un tiempo que se cargue la pagina ---
time.sleep(2)

# --- Maximiza Navegador
driver.maximize_window()

# --- Inicializa variables a utilizar

avisos={
    "fecha":[],
    "portal":[],
    "pais": [],
    "localidad": [],
    "barrio":[],
    "subBarrio":[],
    "operacion":[],
    "tipoProp":[],
    "calle":[],
    "detallePrincipal":[],
    "subDetalle":[],
    "detalleDetallado":[],
    "importeMonedaOpera":[],
    "expensas":[]
    }

# accionar buscador con capital federal
busquedadInicial()

# tiempo de espera
time.sleep(4)

# Borra todos los filtros de la busquedad
borraFiltros()

# tiempo de espera
time.sleep(4)

# Recolectar PAISES 
paises = recolctaPaises(1)
paises_2 = recolctaPaises(2)
print(paises)
print(paises_2)

# INCIO BUSQUEDAD POR PAIS 
paises_nom = []
paises_avisos = []
### INICIO pais primero cinco 
for nombre in paises:
    paises_nom.append(textoSolo(nombre))   
    paises_avisos.append(numeroSolo(nombre))
for i in range(len(paises_nom)):
    print(paises_nom[i] + ": " + paises_avisos[i])
    pais = paises_nom[i].strip().lower()
    # hacer CLICK en el PAIS para ver todos los avisos 
    ingresarPais(i+1, 1)
    time.sleep(4)
    pais_aviso=paises_nom[i]

    ### INICIO Localidades
    localidades=recolctaPaises(1)
    localidades_2=recolctaPaises(2)
    print(localidades)
    print(localidades_2)
    localidad_nom = []
    for nombre in localidades:
        localidad_nom.append(textoSolo(nombre))   
    for i in range(len(localidad_nom)):
        print(localidad_nom[i])
        # hacer CLICK en el LOCALIDAD para ver todos los avisos 
        ingresarPais(i+1, 1)
        time.sleep(4)
        localidad_aviso=localidad_nom[i]
        
        ### INICIO Barrio    
        barrios=recolctaBarrios(1)
        barrios_2=recolctaBarrios(2)
        print(barrios)
        print(barrios_2)
        barrios_nom = []
        for nombre in barrios:
            barrios_nom.append(textoSolo(nombre))   
        for i in range(len(barrios_nom)):
            print(barrios_nom[i])
            # hacer CLICK en el LOCALIDAD para ver todos los avisos 
            ingresarBarrio(i+1, 1)
            time.sleep(4)
            barrio_aviso=barrios_nom[i]
            
            time.sleep(2)
            
            #Operacion Venta
            ingresarOperacion(1)
            operacion_aviso="Venta"
          
            #Tipo de Propiedad - Primer Tramo
            tiposProp=recolectaTipoProp(1)
            
            for i in range(len(tiposProp)):
                # hacer CLICK en el TIPO PROP para ver todos los avisos 
                ingresarTipoProp(i+1, 1)
                time.sleep(4)
                tipoProp_aviso=tiposProp[i]
 
                #Recolecta cantidad de card con avisos           
                id_elements_head=driver.find_elements_by_class_name('listing__item--featured')
                
                id_elements=driver.find_elements_by_class_name('listing__item')
                    
                print(len(id_elements_head))
                
                print(len(id_elements))
                
                for h in range(len(id_elements)):
                    
                   
                    ##### INICIO RECOLECCION AVISOS CARD
                
                    #Fecha de recoleccion
                    avisos['fecha'].append(datetime.datetime.now())
                    #Portal a buscar
                    avisos['portal'].append("Argenprop")
                    #Pais
                    avisos['pais'].append(pais_aviso)
                    #Localidad
                    avisos['localidad'].append(localidad_aviso)
                    #Barrio
                    avisos['barrio'].append(barrio_aviso)
                    #subBarrio
                    avisos['subBarrio'].append(barrio_aviso)
                    #Operacion
                    avisos['operacion'].append(operacion_aviso)
                    #Tipo de Propiedad
                    avisos['tipoProp'].append(tipoProp_aviso)                
                    #Calle               
                    element = driver.find_element_by_xpath('//*[@id="id-card-{}"]/div[2]/div[1]/h2'.format(h+1)).text            
                    avisos['calle'].append(element)
                    #Detalle Principal
                    element = driver.find_element_by_xpath('//*[@id="id-card-{}"]/div[2]/h3'.format(h+1)).text
                    avisos['detallePrincipal'].append(element)
                    #sub Detalle 
                    element = driver.find_element_by_xpath('//*[@id="id-card-{}"]/div[2]/p[1]'.format(h+1)).text
                    avisos['subDetalle'].append(element)
                    #Importe y Moneda              
                    element = driver.find_element_by_xpath('//*[@id="id-card-{}"]/div[1]/div[2]/p[1]'.format(h+1)).text
                    avisos['importeMonedaOpera'].append(element)
                    #Expensas
                    try:
                        element = driver.find_element_by_xpath('//*[@id="id-card-{}"]/div[1]/div[2]/p[2]'.format(h+1)).text
                        avisos['expensas'].append(element)
                    except:
                        avisos['expensas'].append("sin dato")
                    #Detalle Largo
                    try:
                        element = driver.find_element_by_xpath('//*[@id="id-card-{}"]/div[2]/p[2]'.format(h+1)).text
                        avisos['detalleDetallado'].append(element)
                    except:
                        avisos['detalleDetallado'].append("sin dato")
              
                print(avisos)
                    
                sys.exit()            
            
            
            #Tipo de Propiedad - Segundo Tramo
            tiposProp=recolectaTipoProp(2)
            print(tiposProp)
# =============================================================================
# avisos={
#     "calle":[],
#     "detallePrincipal":[],
#     "subDetalle":[],
#     "detalleDetallado":[],
#     "importeMonedaOpera":[],
#     "importeSolo":[],
#     "monedaOpera":[],
#     "expensas":[]
#     }       
# =============================================================================

    
    sys.exit()
    
    # Cambiar Pais
    borraFiltros()

# inicio pais segundo tramo      
paises_nom_2 = []
paises_avisos_2 = []
for nombre in paises_2:
    paises_nom_2.append(textoSolo(nombre))   
    paises_avisos_2.append(numeroSolo(nombre))

for j in range(len(paises_nom_2)):
    print(paises_nom_2[j] + ": " + paises_avisos_2[j])
    pais = paises_nom_2[j].strip().lower()
    
    # hacer CLICK en el PAIS para ver todos los avisos 
    ingresarPais(j+1, 2)
    
    time.sleep(4)

    # Cambiar Pais
    borraFiltros()    
    
sys.exit()
