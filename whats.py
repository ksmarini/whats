from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service
from time import sleep


fake = Faker('pt_BR')

options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
# service = Service(GeckoDriverManager().install())
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(service=service, options=options)


def abrir_janela_whatsapp():
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, timeout=60)
    driver.maximize_window()
    barra_lateral = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]')))
    driver.implicitly_wait(2)


def abrir_janela_conversa(numero_contato):
    barra_pesquisa = driver.find_element(By.XPATH, '//div[@title="Caixa de texto de pesquisa"]')
    barra_pesquisa.send_keys(Keys.CONTROL + 'a')
    barra_pesquisa.send_keys(Keys.DELETE)

    nova_conversa = driver.find_element(By.XPATH, '//div[@title="Nova conversa"]')
    nova_conversa.click()

    barra_pesquisa = driver.find_element(By.XPATH, '//div[@title="Caixa de texto de pesquisa"]')
    driver.implicitly_wait(2)
    # barra_pesquisa.send_keys(numero_contato)

    for num in numero_contato:
        barra_pesquisa.send_keys(num)
        sleep(1)

    barra_pesquisa.send_keys(Keys.RETURN)



def sai_das_conversas():
    barra_pesquisa = driver.find_element(By.XPATH, '//div[@title="Caixa de texto de pesquisa"]')
    barra_pesquisa.send_keys(Keys.CONTROL + 'a')
    barra_pesquisa.send_keys(Keys.DELETE)
    barra_pesquisa.send_keys(Keys.ESCAPE)



def envia_mensagens(mensagem):
    barra_mensagem = driver.find_element(By.XPATH, '//div[@title="Digite uma mensagem"]')
    barra_mensagem.send_keys(mensagem)
    barra_mensagem.send_keys(Keys.RETURN)


if __name__ == '__main__':
    contatos = ['556992809962', '556992768408', '551132511229']
    mensagem = f"""
    Por favor, ignore essa mensagem.
    """
    abrir_janela_whatsapp()

    for contato in contatos:
        abrir_janela_conversa(contato)
        sleep(1)
        envia_mensagens(f'Olá {fake.name()}!\n{mensagem}')
        sleep(1)
        sai_das_conversas()
        sleep(1)


    sleep(200)


