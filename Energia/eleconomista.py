from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import math
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

consultas = pd.read_csv('consultas_energia.csv')
consultas = list(consultas.values)
consultas = [consulta[0] for consulta in consultas]
eleconomista = []

for tema_busqueda in consultas:
    tema_busqueda = tema_busqueda.upper().replace(' ', '-')
    driver = webdriver.Firefox(options=options)
    driver.get('http://empresite.eleconomistaamerica.co/Actividad/{}/departamento/ANTIOQUIA/'.format(tema_busqueda))
    response = driver.find_element_by_tag_name('body')
    resultados = driver.execute_script('return arguments[0].innerHTML', response)
    resultados_html = BeautifulSoup(resultados, 'html.parser')
    driver.close()
    if resultados_html.find_all('h2', {'class': 'title01'}) == []:
        total_resultados = 0
    else:
        total_resultados = resultados_html.find_all('h2', {'class': 'title01'})[0].get_text().split(' ')[0].replace('.', '')

    if int(total_resultados) >= 100:
        paginas = 3
    else:
        paginas = math.ceil(int(total_resultados)/30)

    for i in range(1, paginas + 1):
        driver = webdriver.Firefox(options=options)
        driver.get('http://empresite.eleconomistaamerica.co/Actividad/{}/departamento/ANTIOQUIA/PgNum-{}/'.format(tema_busqueda, i))
        response = driver.find_element_by_tag_name('body')
        resultados = driver.execute_script('return arguments[0].innerHTML', response)
        resultados_html = BeautifulSoup(resultados, 'html.parser')
        driver.close()
        empresas = resultados_html.find_all('li', {'class': 'resultado_pagina'})
        
        for empresa in empresas:
            try:
                nombre_empresa = empresa.find_all('a')[0].get_text()
            except:
                nombre_empresa = None
            try:
                link_empresa = empresa.find_all('a')[0].get('href')
            except:
                link_empresa = None
            try:
                direccion = empresa.find_all('div', {'class': 'street-address inline'})[0].get_text()
            except:
                direccion = None
            try:
                departamento = empresa.find_all('div', {'class': 'region inline'})[0].get_text()
            except:
                departamento = None
            try:
                ciudad = empresa.find_all('div', {'class': 'locality inline'})[0].get_text()
            except:
                ciudad = None

            driver = webdriver.Firefox(options=options)
            driver.get(link_empresa)
            try:
                response = driver.find_element_by_class_name('list06')
                resultados = driver.execute_script('return arguments[0].innerHTML', response) 
                resultados_html = BeautifulSoup(resultados, 'html.parser')
                driver.close()
                actividad = resultados_html.find_all('span', {'class': 'category'})[0].get_text()
                telefono = resultados_html.find_all('span', {'class': 'tel'})[0].get_text()
            except:
                actividad = None
                telefono = None
            eleconomista.append({'Tema_Busqueda': tema_busqueda,
                                 'Nombre_Empresa': nombre_empresa,
                                 'Link': link_empresa,
                                 'Direccion': direccion,
                                 'Departamento': departamento,
                                 'Ciudad': ciudad,
                                 'Actividad': actividad,
                                 'telefono': telefono})

eleconomista = pd.DataFrame(eleconomista)
eleconomista.to_csv('economista_energia_antioquia.csv', sep = ';', encoding = 'utf-8')
