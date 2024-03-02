import time
from time import perf_counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
import csv
import pygetwindow as gw


index=1

#funkcja do klikania przyciku "Show more" na stronie
def click_show_more_button():
    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button-compare"))
    )
    button.click()

#zbieranie danych ze strony
def collect_runner_data():
    runners = driver.find_elements(By.CSS_SELECTOR, "div.row.rms-grid-item")
    for runner in runners:
        try:
            name = runner.find_element(By.CSS_SELECTOR, "div.name.rms-grid-line.ng-binding").text.strip()
            name = name.split()
            first, second = name[0], ' '.join(name[1:])

            details = runner.find_element(By.CSS_SELECTOR, "div.details.rms-grid-line")
            gender_age_elements = details.find_elements(By.CSS_SELECTOR, "span.ng-binding.ng-scope")
            gender_age = [elem.text.strip() for elem in gender_age_elements]

            result_section = runner.find_element(By.CSS_SELECTOR, "div.col-xs-8.col-sm-8.col-md-6")
            time = result_section.find_element(By.CSS_SELECTOR, "span.long-text > span.num.ng-binding").text.strip()
            place = result_section.find_element(By.CSS_SELECTOR, "span.mid-text > span.num.ng-binding").text.strip()

            gender = gender_age[0][0]
            age = gender_age[0][1:]
            country = gender_age[-1]

            bib = details.find_element(By.CSS_SELECTOR, "span.left-bordered.ng-scope").text.strip().split()[1]

            #zapis pojedynczego rekordu do pliku
            with open('runners_datas.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([first, second, gender, age, country, bib, time, place])
        except (IndexError, NoSuchElementException):
            #w przypadku niepasujących danych, dodawany jest rekord Anonymous
            with open('runners_datas.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Anonymous", "-", "-", "-", "-", "-", time, place])


if __name__ == "__main__":

    #stworzenie pliku
    with open('runners_datas.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Name","LastName","Sex","Age","Country","BibNumber","Result","Place"])

    while index<48000:
        time1 = time.perf_counter()
        driver = webdriver.Chrome()
        browser_window = gw.getWindowsWithTitle('Chrome')[0]
        browser_window.hide()
        driver.get(f'https://results.nyrr.org/event/M2022/finishers#opf={index}')
        while True:
            try:
                click_show_more_button()
            except TimeoutException:
                break
        collect_runner_data()
        index+=500 #strona pozwala załadować maksymalnie 500 rekordów, dlatego co 500 zapisanych rekordów działanie jest powtarzane


