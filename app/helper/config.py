from configobj import ConfigObj
config = ConfigObj()

config.filename = 'config'
#
XPATH = {
    'login_username' : '/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/input',
    'login_password' : '/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input',
    'login_securitykey' : '/html/body/table[2]/tbody/tr/td[1]/form/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/input',
    'sorgu':'//*[@id="form1:menuHtmlCommandExButton201_MOUSE"]',
    'sorgu_input':'//*[@id="form1:text2"]',
    'sorgu_buton' : '//*[@id="form1:buttonSorgula"]',
    'isim':'//*[@id="form1:text13"]',
    'soyisim':'//*[@id="form1:text17"]',
    'kapsam':'//*[@id="form1:text22"]',
    'message':'//*[@id="form1"]/table[1]/tbody/tr/td[2]/center/div/table/tbody/tr/td[2]/span'
}

config['XPATH'] = XPATH
#
config['EXCEL_PATH'] = r'tc_no.xlsx'
#
config['OUT_EXCEL_PATH']= r'Mustehaklik.xlsx'

config['CHROMEDRIVER_PATH']=r'chromedriver.exe'
#
config['Kullanici_Adi']='18540463'
#
config['Sifre']='Sena1854'
#
config['Key']='P9NL-NKUF-7PV3-APAF-YLT3-JNHW-9PFF-MKTP'
# config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///:memory:'
#
config['login_page'] = 'https://medeczane.sgk.gov.tr/eczane/login.jsp'
#
config['main_page'] = 'https://medeczane.sgk.gov.tr/eczane/'
#
config['sorgu_page'] = 'https://medeczane.sgk.gov.tr/eczane/faces/pages/haksahibi/MustehaklikSorgu.jsp'

config.write()