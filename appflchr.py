#import time
#from selenium import webdriver
#
# driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/xhtml')
# time.sleep(5)  # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)  # Let the user actually see something!
# driver.quit()
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By

# from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options

from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, request, render_template

# configuration
DEBUG = False
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# enable CORS
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def ping_png():
    driver = init_driver()
    rzt = lookup(driver, "Selenium")
    return render_template('index.html', name=rzt)
    # return jsonify(len())


#    return ('pong!')


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


def init_driver():

    CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
    GOOGLE_CHROME_BIN = "/app/.apt/usr/bin/google-chrome-stable"
    #CHROMEDRIVER_PATH = "/usr/local/bin/chromedriver"
    #GOOGLE_CHROME_BIN = "/usr/bin/google-chrome-stable"
    chrome_options = Options()
    # jsonify(chrome_bin)
    #    chrome_options = Options()
    #    chrome_options.add_argument("--headless")
    #    chrome_options.add_argument("--no-sandbox")
    #    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--window-size=1200x600')
    driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    #    options = webdriver.FirefoxOptions()
    #    options.add_argument('headless')
    #opts = Options()
    # opts.set_headless()
    # assert opts.headless  # без графического интерфейса.
    #    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    #driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=opts)
    #    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.wait = WebDriverWait(driver, 2)
    return driver


def lookup(driver, query):
    # driver.get("http://www.ya.ru")
    driver.get('http://www.google.com/xhtml')
    time.sleep(1)  # Let the user actually see something!
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(query)
    search_box.submit()
    lst = []
    with open('templates/includes/ht.html', 'w') as outfile:
        outfile.write('<ul>')
    try:
        # box = driver.wait.until(
        #    EC.presence_of_element_located((By.NAME, "text")))
        # button = driver.wait.until(EC.element_to_be_clickable(
        # (By.NAME, "btnK")))
        # box.send_keys(query)
        # button.click()
        # box.send_keys(u'\ue007')
        box = driver.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "g")))
        page_html = driver.page_source
        with open('templates/includes/ht_source.html', 'w') as soutfile:

            i = page_html.find('</body></html>')
            page_html = page_html[:i] + '<script type="text/javascript">window.onclick = function() {alert("test");}</script><script  type="text/javascript">     window.onclick = function (e) {      var el = e ? e.target : window.event.srcElement;          alert(e.target.parentNode);            el = el.parentNode;          };  </script>' + page_html[i:]
            soutfile.write(page_html)

        results = driver.find_elements_by_css_selector("span.st")

        #       results = driver.find_elements_by_class_name("st")
        # results = driver.find_elements(by=By.CSS_SELECTOR, value='#rso span.st')
        with open('templates/includes/ht.html', 'a') as outfile:

            for result in results:
                result = result.get_attribute('innerHTML').strip()
                result = '<li>' + result + '</li>'
                print(result)
                outfile.write(result)
                lst.append(result)
        driver.quit()
        with open('templates/includes/ht.html', 'a') as outfile:
            outfile.write("</ul>")
        return lst
    except TimeoutException:  # except TimeoutException:
        print("Box or Button not found in google.com")


if __name__ == '__main__':
    app.run()
