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
    "importeSolo":[],
    "monedaOpera":[],
    "expensas":[]
    }

# accionar buscador con capital federal
element = driver.find_element_by_xpath("//*[@id='home-ubicacion']")
element1 = element.send_keys("Capital Federal")
time.sleep(4)
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ENTER)

# tiempo de espera
time.sleep(4)

# Borra todos los filtros de la busquedad
element = driver.find_element_by_xpath("/html/body/main/div[2]/sidebar/div[1]/div/button").click()

# Recolectar PAISES 
time.sleep(4)
allPaises = driver.find_elements_by_xpath('//*[@id="locationFilter"]/ul[1]/li')
todosPaises = []
for paisesNom in allPaises:
    todosPaises.append(paisesNom.text)

# INCIO BUSQUEDAD POR PAIS 
paises_nom = []
paises_avisos = []

for nombre in todosPaises:
    paises_nom.append(textoSolo(nombre))   
    paises_avisos.append(numeroSolo(nombre))

i=1
for i in range(len(paises_nom)):
    print(paises_nom[i] + ": " + paises_avisos[i])
    pais = paises_nom[i].strip().lower()
    
    # hacer CLICK en el PAIS para ver todos los avisos 
    element = driver.find_element_by_xpath('//*[@id=\'{}\']'.format(pais)).click()
        
    time.sleep(2)

    # Recolectar Localidades
    allLocalidades = driver.find_elements_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/div/div[2]/ul[1]/li')
    todosLocalidades = []
    
    # INICIO BUSQUEDAD POR LOCALIDAD 
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
             
            # Elegir BARRIO
            element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/form/div/div[2]/ul[1]/li[{}]/span'.format(j+1)).click()
            elem_barrio = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/form/div/div[2]/ul[1]/li[{}]/label/span/a'.format(j+1)).text
            barrio = textoSolo(elem_barrio).strip()
            barrio_cant = numeroSolo(elem_barrio)
            
            time.sleep(2)
                
            # Elegir SUB-BARRIO
            element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/form/div/div[2]/ul[1]/li[{}]/ul/li[1]/label/span/a'.format(j+1)).click()
            elem_subBarrio = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[1]/form/div/div[2]/ul[1]/li[{}]/ul/li[1]/label/span/a'.format(j+1)).text
            subBarrio = textoSolo(elem_subBarrio).strip()
            subBarrio_cant = numeroSolo(elem_subBarrio)

            # Elegir Operacion
            elem_tipo_operacion = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul/li[1]/a').text
            element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul/li[1]/a').click()
            tipo_operacion = textoSolo(elem_tipo_operacion).strip()
            tipo_operacion_cant = numeroSolo(elem_tipo_operacion)
            
            time.sleep(2)
                

            # SE EMPIEZA CON LOS TIPOS DE PROPIEDAD DE CADA SUB BARRIO
                
            for x in range(1, 20):
                    
                # BOTON MAS TIPO DE PROPIEDAD
********************                
ACA JODE VER ERROR EN BOTON MAS PROPIEADES
********************
                element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/button').click()
                   
                # Recolectar todos los tipos de propiedad                             
                html_list = driver.find_element_by_id("tipopropiedad")
                items = html_list.find_elements_by_tag_name("li")
                   
                # COMIENZA BUCLE TIPO DE PROPIEADES 
                posI=1
                for item in items:
                    elem_tipo_propiedad = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul[1]/li[{}]/a'.format(posI)).text
                    element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[4]/div/div[4]/div/ul[1]/li[{}]/a'.format(posI)).click()
                    tipo_propiedad = textoSolo(elem_tipo_propiedad).strip()
                    tipo_propiedad_cant = numeroSolo(elem_tipo_propiedad)
                    
                    # BOTON CANCELAR - ALERTA BUSQUEDAD
                    try:
                        element = driver.find_element_by_xpath('/html/body/main/div[4]/button[2]').click()
                    except:
                        element="sin dato"            
              
                    # Obtener datos del aviso
                    for y in range(1, 3):    
                                
                        try: 
                            element = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]'.format(y))
                        except:
                            print("fin sub barrio")
                            element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[1]/div/ul/li[1]/h2/span').click()
                            break
                        
                        # archivar fecha y hora extraccion del aviso
                        fecha_extraccion=datetime.datetime.now()
                        fecha_str = fecha_extraccion.strftime('%Y/%m/%d')
                        avisos["fecha"].append(fecha_str)
                        
                        # archivar portal del aviso
                        avisos["portal"].append("Argenprop")
                        
                        # archivar pais del aviso 
                        avisos["pais"].append(pais)
                        
                        # archivar localidad del aviso 
                        avisos["localidad"].append(localidad)
                        
                        # archivar barrio del aviso 
                        avisos["barrio"].append(barrio)

                        # archivar sub-Barrio del aviso 
                        avisos["subBarrio"].append(subBarrio)

                        # archivar Operacion del aviso 
                        avisos["operacion"].append(tipo_operacion)
                        
                        # archivar pais del aviso 
                        avisos["tipoProp"].append(tipo_propiedad)
                                                                        
                        calle = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/div[1]/h2'.format(y)).text
                        # archivar calle del aviso 
                        avisos["calle"].append(calle)
                        
                        detalle_Principal = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/h3'.format(y)).text
                        # archivar Detalle Principal del aviso 
                        avisos["detallePrincipal"].append(detalle_Principal)
                        
                        sub_Detalle = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/p[1]'.format(y)).text
                        # archivar Sub Detalle del aviso 
                        avisos["subDetalle"].append(sub_Detalle)
                        
                        detalle_detallado = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/p[2]'.format(y)).text
                        # archivar Detalle Detallado del aviso 
                        avisos["detalleDetallado"].append(detalle_detallado)
                        
                        importe_moneda_Operacion = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[1]/div[2]/p[1]'.format(y)).text
                        # archivar Importe y Moneda de la Operacion  
                        avisos["importeMonedaOpera"].append(importe_moneda_Operacion)
                        
                        patron_moneda = r"([$,USD,usd]+)"
                        importe_aviso = numeroSolo(importe_moneda_Operacion)
                        moneda_aviso = re.findall(patron_moneda, importe_moneda_Operacion)
                        
                        avisos["importeSolo"]=importe_aviso
                        avisos["monedaOpera"]=moneda_aviso
                    
                        try:
                            expensas = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[1]/div[2]/p[2]'.format(y)).text
                        except:
                            expensas = "0"
                        # archivar expensas del aviso 
                        avisos["expensas"].append(expensas)
                 
                    for z in range(6,24):
                        try: 
                            element = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]'.format(z))
                        except:
                            print("fin sub barrio")
                            element = driver.find_element_by_xpath('/html/body/main/div[2]/sidebar/div[1]/div/ul/li[1]/h2/span').click()
                            break
                        
                        # archivar fecha y hora extraccion del aviso
                        fecha_extraccion=datetime.datetime.now()
                        fecha_str = fecha_extraccion.strftime('%Y/%m/%d')
                        avisos["fecha"].append(fecha_str)
                        
                        # archivar portal del aviso
                        avisos["portal"].append("Argenprop")
                        
                        # archivar pais del aviso 
                        avisos["pais"].append(pais)
                        
                        # archivar localidad del aviso 
                        avisos["localidad"].append(localidad)
                        
                        # archivar barrio del aviso 
                        avisos["barrio"].append(barrio)

                        # archivar sub-Barrio del aviso 
                        avisos["subBarrio"].append(subBarrio)

                        # archivar Operacion del aviso 
                        avisos["operacion"].append(tipo_operacion)
                        
                        # archivar pais del aviso 
                        avisos["tipoProp"].append(tipo_propiedad)
                                                               
                        try:    
                            calle = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/div[1]/h2'.format(z)).text        
                        except:
                            calle = "sin dato"
                        # archivar calle del aviso 
                        avisos["calle"].append(calle)
                
                        try:
                            detalle_Principal = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/h3'.format(z)).text
                        except:
                            detalle_Principal = "sin dato"
                        # archivar Detalle Principal del aviso 
                        avisos["detallePrincipal"].append(detalle_Principal)
                
                
                        try:
                            sub_Detalle = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/p[1]'.format(z)).text
                        except:
                            sub_Detalle = "sin dato"
                        # archivar Sub Detalle del aviso 
                        avisos["subDetalle"].append(sub_Detalle)
                
                        try:
                            detalle_detallado = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[2]/p[2]'.format(z)).text
                        except:
                            detalle_detallado = "sin dato"
                        # archivar Detalle Detallado del aviso 
                        avisos["detalleDetallado"].append(detalle_detallado)
                
                        try:
                            importe_moneda_Operacion = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[1]/div[2]/p[1]/span'.format(z)).text
                        except:
                            importe_moneda_Operacion ="Sin dato"
                        # archivar Importe y Moneda de la Operacion  
                        avisos["importeMonedaOpera"].append(importe_moneda_Operacion)
                
                        patron_moneda = r"([$,USD,usd]+)"
                        importe_aviso = numeroSolo(importe_moneda_Operacion)
                        moneda_aviso = re.findall(patron_moneda, importe_moneda_Operacion)
                        
                        avisos["importeSolo"]=importe_aviso
                        avisos["monedaOpera"]=moneda_aviso
                
                        try:
                            expensas = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div[1]/div[{}]/a/div[1]/div[2]/p[2]'.format(z)).text                
                        except:
                            expensas = "0"
                        # archivar expensas del aviso 
                        avisos["expensas"].append(expensas)  
                    
                    try:
                        element = driver.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/ul/li[3]').click()
                    except:
                        break
                    
            print("--------------")
            print(avisos)
                       
            # --- Cierra navegador 
            driver.close()
            # --- hora Final
            hrsFin=datetime.datetime.now()
            print("Hora Final de la Extraccion: ", hrsFin)
            print("Tiempo trasncurrido de la Extraccion: ", hrsFin - hrsInicial)
                        
            sys.exit()             
        
        # VER ARMADO DE ARRAYS Y TERMINAR CON LA CANTIDAD DE CADA TIPO DE PROPIEDAD 
         
                    
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

