from app.model.website import Website
from app.helper.excel import readContacts,format_number
from app import config

from xlsxwriter import Workbook

import time

class Medula(Website):

    def __init__(self, *args, **kwargs) -> None:
        super(Medula, self).__init__(*args, **kwargs)

        self.url = ''
        self.excel_path = ''
    
    @staticmethod
    def get_tc():
        send_list = readContacts(config['EXCEL_PATH'])
        tc_list = format_number(send_list)

        return tc_list

    def main_page(self):
        self.selenium.set_ignore_certificate_error()

        self.go_to(config['login_page'])
        try:
            login = self.get_element_wait(element_path=config['XPATH']['login_username'])

            if self.current_url() == config['login_page']:
                self.url = self.current_url()
            
            return True
        except Exception as e:
            print('Websitesi açılmadı')

            return False

    def login(self):
        if self.main_page():
            try:
                user_el = self.get_element(element_path=config['XPATH']['login_username'])
                self.write(user_el,config['Kullanici_Adi'])

                pass_el = self.get_element(element_path=config['XPATH']['login_password'])
                self.write(pass_el,config['Sifre'])

                sorgu_el = self.get_element_wait(element_path=config['XPATH']['sorgu'])

                if self.current_url() == config['main_page']:
                    self.url = self.current_url()
                
                return True

            except Exception as e:
                print('Sayfa açılmadı')

                return False

    def sorgu(self):
        if self.login() and (self.url == config['main_page']):
            people = []

            tc_list = self.get_tc()

            try:
                for tc in tc_list:
                    person = {'TC':'', 'Status':''}
                    person['TC'] = tc

                    sorgu_el = self.get_element(element_path=config['XPATH']['sorgu'])
                    self.click(sorgu_el)

                    sorgu_input_el = self.get_element_wait(element_path=config['XPATH']['sorgu_input'])
                    self.write(sorgu_input_el,tc)

                    time.sleep(1)

                    sorgu_buton_el = self.get_element(element_path=config['XPATH']['sorgu_buton'])
                    self.click(sorgu_buton_el)

                    try:
                        sorgu_isim_el = self.get_element_wait(wait=2,element_path=config['XPATH']['isim'])
                        print(sorgu_isim_el.text)

                        person['Status'] = '{} Yaşıyor'.format(sorgu_isim_el.text)
                        
                    except Exception as e:
                        person['Status'] = 'Ölü'
                        
                    people.append(person)
                    
                if self.current_url() == config['main_page']:
                    self.url = self.current_url()

                print(people)

                return people

            except Exception as e:
                print('Sayfa açılmadı')

                return False

    @staticmethod
    def to_excel(dict_data):
        ordered_list=['TC','Status']

        wb=Workbook(config['OUT_EXCEL_PATH'])
        ws=wb.add_worksheet()

        first_row=0
        for header in ordered_list:
            col=ordered_list.index(header)
            ws.write(first_row,col,header)

        row=1
        for data in dict_data:
            for _key,_value in data.items():
                col=ordered_list.index(_key)
                ws.write(row,col,_value)
            row+=1 #enter the next row
        wb.close()
