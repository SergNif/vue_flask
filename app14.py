from selenium import webdriver
from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, request, render_template
from selenium.webdriver.chrome.options import Options
import os
# browser = webdriver.PhantomJS()
# This does not throw an exception if it got a 404
#browser.get("http://www.google.com")

#html = browser.page_source
#print html
app = Flask(__name__)
app.config.from_object(__name__)
# enable CORS
CORS(app)
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
GOOGLE_CHROME_BIN =  "/app/.apt/usr/bin/google-chrome-stable"


@app.route('/p', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/', methods=['GET'])
def ping_png():

    chrome_options = Options()
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    #    chrome_options.add_argument('--disable-gpu')
    #    chrome_options.add_argument('--no-sandbox')
    #    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    driver.get('https://ya.ru')
    html = driver.page_source
    driver.quit()
    #print(html)
    return render_template('index.html', name=html)


if __name__ == '__main__':
    app.run()