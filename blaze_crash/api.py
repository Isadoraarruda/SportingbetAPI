import requests
import json
import blaze_crash as g
import telebot


class bot:
    def __init__(self):
        while True:
            try:
                self.name = 'Blaze Crash'
                self.token_bot = '6076057018:AAEs2O2x5oswARe0sMpRyVGEl4ZaqYVp3eA'
                self.user_id = '-1001828355004'
                self.link = 'http://api.mxvinvest.com:63000/blaze-crash'
                self.result = None
                self.now = None
                self.check_now = None
                self.now_time = 0
                self.message_ids = 0
                self.entrada_atual = 0
                self.message_delete = False
                self.win_results = 0
                self.loss_results = 0
                self.empate_results = 0
                self.max_hate = 0
                self.win_hate = 0
                self.win_semgale = 0
                self.win_gale1 = 0
                self.win_gale2 = 0
                self.empate_semgale = 0
                self.empate_gale1 = 0
                self.empate_gale2 = 0
                self.analisar = 0
                self.martingales = int(input('Quantos martingales: '))
                self.alvo = float(input('Qual a meta do sinal: '))
                self.bot = telebot.TeleBot(token=self.token_bot, parse_mode='MARKDOWN')
                g.utils.get_data(self)
                break
            except:
                print('Erro de configuração.')
                continue


    def requets_game(self):
        url = requests.get(self.link)
        data = json.loads(url.content)
        results = data["results"]
        return results

    def rum(self):
        check_results = []
        while True:
            main_results = self.requets_game()
            if main_results != check_results:
                print(main_results)
                check_results = main_results
                g.utils.delet(self)
                g.utils.estrategy(self, main_results)
                
try:
    objeto = bot()
    objeto.rum()
except:
    pass