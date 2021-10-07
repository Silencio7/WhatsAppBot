from selenium import webdriver
import pyautogui
import time
from tkinter import *


mensagem = "Teste do bot 123"
contatos = ['Mãe']


class WhatsappBot:
    def __init__(self):
        self.mensagem = mensagem
        self.contatos = contatos
        options = webdriver.FirefoxOptions()
        options.add_argument('lang=pt-br')
        self.navegador = webdriver.Firefox()

    def enviar_mensagens(self):
        self.navegador.get('https://web.whatsapp.com')
        time.sleep(10)
        for contatos in self.contatos:
            self.navegador.find_element_by_class_name('_13NKt').send_keys(f'{contatos}')
            time.sleep(2)
            pyautogui.press("Enter")
            time.sleep(1)
            chat_box = self.navegador.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]\
                                                                /footer/div[1]/div/div/div[2]/div[1]/div/div[2]")
            time.sleep(1)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.navegador.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]\
                                                                        /footer/div[1]/div/div/div[2]/div[2]/button")
            time.sleep(1.5)
            botao_enviar.click()
            time.sleep(2)


def janela_bot():
    janela = Tk()
    janela.geometry('330x80+500+280')
    janela.title('V.1 - WhatsAppBot')
    texto_inicial = Label(janela, text="Clique no 'Iniciar' para começar o funcionamento do Bot")
    texto_inicial.grid(column=0, row=2)
    botao = Button(janela, text="Iniciar", command=janela.destroy)
    botao.grid(column=0, row=4)
    texto_res = Label(janela, text="Após pressionar, apenas espere sem executar nenhuma tarefa.")
    texto_res.grid(column=0, row=6)
    janela.mainloop()


def janela_bot2():
    janela = Tk()
    janela.geometry('165x70+580+290')
    janela.title('V.1 - WhatsAppBot')
    texto_inicial = Label(janela, text="O Bot terminou o seu serviço.")
    texto_inicial.grid(column=0, row=1)
    botao = Button(janela, text="Encerrar", command=janela.quit)
    botao.grid(column=0, row=2)
    texto_inicial = Label(janela, text="Obrigado por utilizar.")
    texto_inicial.grid(column=0, row=3)
    janela.mainloop()


janela_bot()
bot = WhatsappBot()
bot.enviar_mensagens()
janela_bot2()