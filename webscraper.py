from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from splinter import Browser
app = Flask(__name__)

@app.route("/scrape", methods = ['POST', 'GET'])
def webscrapper():
    if request.method == 'POST':
        browser = Browser('chrome', headless=True)
        browser.visit("https://amazon.in")
        search_bar = browser.find_by_id("twotabsearchtextbox")
        search_btn = browser.find_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
        query = request.form["query"]
        search_bar.fill(query)
        search_btn.click()
        element_path = '//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]'
        elements = browser.find_by_xpath(element_path)
        title = []
        for element in elements:
            text = element.text
            title.append(text)
        browser.quit()
        return render_template("results.html", result = title)

if __name__ == '__main__':
   app.run(debug = True)
