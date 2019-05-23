import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

# from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, request, render_template

#configuration
DEBUG = False
#instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
#enable CORS
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def ping_png():
    driver = init_driver()
    rzt = lookup(driver, "Selenium")
    return render_template('index.html', name=rzt)
    #return jsonify(len())


#    return ('pong!')


#sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


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
        return results


#        print(type(results), "  ", len(results))
#        for res in results:
#            print(res)

    except TimeoutException:  #except TimeoutException:
        print("Box or Button not found in google.com")

if __name__ == '__main__':
    app.run()