import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#dane testowe
haslo = 'kk33.o9'

class RejestracjaNowegoUzytkownika(unittest.TestCase):#unitest.TestCase - biblioteki
    def setUp(self):
        # WARUNKI WSTĘPNE
        # 1. Otwarta strona główna
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.eobuwie.com.pl/")
        # (2. Użytkownik niezalogowany)
        # Zamknij alert o ciasteczkach
        self.driver.find_element(By.CLASS_NAME, "e-button--type-primary.e-button--color-brand.e-consents-alert__button.e-button").click()

    def testBrakPodaniaImienia(self):#zawsze musi byc slowo test zeby progrma wiedzial ze to test
        sleep(5)
        # 1. Kliknij „Zarejestruj”
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Zarejestruj").click()
        # 2.Wpisz nazwisko
        nazwisko = self.driver.find_element(By.ID, "lastname")
        nazwisko.send_keys("Nowak")
        sleep(5)
        # 3. wpisz adres email
        adres = self.driver.find_element(By.ID, "email_address")
        adres.send_keys("adrian@adrian.pl")
        # 4. wpisz haslo(co namniej 6 znakow)
        haslo = self.driver.find_element(By.ID, "password")
        haslo.send_keys("kk33.o9")
        # 5. powtorz haslo
        haslo2 = self.driver.find_element(By.ID, "confirmation")
        haslo2.send_keys("kk33.o9")

        # 6. Zaznacz „Oświadczam, że zapoznałem się z treścią Regulaminu serwisu i akceptuję
        # jego postanowienia.”
        self.driver.find_element(By.XPATH, '//label[@class="checkbox-wrapper__label"]').click()
        # OSTROŻNIE!!!!
        # 7. Kliknij „Załóż nowe konto” (tylko dla przypadków niegatywnych!)
        self.driver.find_element(By.XPATH, '//button[@data-testid="register-create-account-button"]').click()

    
    def tearDown(self):
        # Zakończenie testu
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()