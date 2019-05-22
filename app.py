import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

# from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def init_driver():
    #    options = webdriver.FirefoxOptions()
    #    options.add_argument('headless')
    opts = Options()
    opts.set_headless()
    assert opts.headless  # без графического интерфейса.
    driver = webdriver.Firefox(options=opts)
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, query):
    driver.get("http://www.ya.ru")
    try:
        box = driver.wait.until(
            EC.presence_of_element_located((By.NAME, "text")))
        #        button = driver.wait.until(EC.element_to_be_clickable(
        #            (By.NAME, "btnK")))
        box.send_keys(query)
        # button.click()
        box.send_keys(u'\ue007')
        box = driver.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "serp-item")))
        results = driver.find_elements_by_class_name("serp-item")
        print(type(results), "  ", len(results))
        for res in results:
            print(res)

    except TimeoutException:  #except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "Selenium")
    time.sleep(4)
    driver.quit()

# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options
#
# opts = Options()
# opts.set_headless()
# assert opts.headless  # без графического интерфейса.
#
# browser = Firefox(options=opts)
# browser.get('https://ya.ru')
# search_form = browser.find_elements_by_class_name('input__control input__input')
# print(len(search_form))
# search_form.send_keys('real python')
# search_form.submit()
# results = browser.find_elements_by_class_name('serp-list serp-list_left_yes')
# print(results)
# browser.close()
# quit()

# from flask import Flask, jsonify
# from flask_cors import CORS
# from flask import Flask, request
#
# configuration
# DEBUG = False
#
# instantiate the app
# app = Flask(__name__)
# app.config.from_object(__name__)
#
# enable CORS
# CORS(app)
#
#
# @app.route('/png', methods=['GET', 'POST'])
# def ping_png():
#
#    r = requests.get("http://ya.ru", params={"did": 123, "ng": 456})
#    return r.text()
# return jsonify('pong!')
#
#
# sanity check route
# @app.route('/ping', methods=['GET'])
# def ping_pong():
#    return jsonify('pong!')
#
#
# if __name__ == '__main__':
#    app.run()
