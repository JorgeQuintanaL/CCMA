from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import math

drv = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

consultas = pd.read_csv('consultas_salud_local.csv', sep = ";")
consultas = list(consultas.values)
consultas = [consulta[0] for consulta in consultas]
eleconomista = []

for tema_busqueda in consultas:
    tema_busqueda = tema_busqueda.upper().replace(' ', '-')
    print('Buscando ' + str(tema_busqueda))
    driver = webdriver.Chrome(drv, chrome_options=chrome_options)
    driver.get('http://empresite.eleconomistaamerica.co/Actividad/{}/departamento/ANTIOQUIA/'.format(tema_busqueda))
    response = driver.find_element_by_tag_name('body')
    resultados = driver.execute_script('return arguments[0].innerHTML', response)
    resultados_html = BeautifulSoup(resultados, 'html.parser')
    if resultados_html.find_all('h2', {'class': 'title01'}) == []:
        total_resultados = 0
    else:
        total_resultados = resultados_html.find_all('h2', {'class': 'title01'})[0].get_text().split(' ')[0].replace('.', '')
    driver.close()
    print(str(total_resultados) + ' resultados encontrados!')

    if int(total_resultados) >= 100:
        paginas = 4
    else:
        paginas = math.ceil(int(total_resultados)/30)

    for i in range(1, paginas + 1):
        driver = webdriver.Chrome(drv, chrome_options=chrome_options)
        driver.get('http://empresite.eleconomistaamerica.co/Actividad/{}/departamento/ANTIOQUIA/PgNum-{}/'.format(tema_busqueda, i))
        response = driver.find_element_by_tag_name('body')
        resultados = driver.execute_script('return arguments[0].innerHTML', response)
        resultados_html = BeautifulSoup(resultados, 'html.parser')
        empresas = resultados_html.find_all('li', {'class': 'resultado_pagina'})
        driver.close()
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

            driver = webdriver.Chrome(drv, chrome_options=chrome_options)
            driver.get(link_empresa)
            try:
                response = driver.find_element_by_class_name('list06')
                resultados = driver.execute_script('return arguments[0].innerHTML', response) 
                resultados_html = BeautifulSoup(resultados, 'html.parser')
                actividad = resultados_html.find_all('span', {'class': 'category'})[0].get_text()
                telefono = resultados_html.find_all('span', {'class': 'tel'})[0].get_text()
            except:
                actividad = None
                telefono = None
            
            driver.close()
            eleconomista.append({'Tema_Busqueda': tema_busqueda,
                                 'Nombre_Empresa': nombre_empresa,
                                 'Link': link_empresa,
                                 'Direccion': direccion,
                                 'Departamento': departamento,
                                 'Ciudad': ciudad,
                                 'Actividad': actividad,
                                 'telefono': telefono})

eleconomista = pd.DataFrame(eleconomista)
print('Guardando los resultados')
eleconomista.to_csv('economista_salud_antioquia.csv', sep = ';', encoding = 'utf-8')
print('Todo Listo!')