from app.website.medula import Medula
from app.helper.online_license import is_valid
import sys

if __name__ == '__main__':
    
    is_valid()

    med = Medula()

    liste = med.sorgu()
    med.to_excel(liste)

    med.selenium.driver.quit()