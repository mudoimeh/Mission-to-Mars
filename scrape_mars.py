
# coding: utf-8

#import dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time


def init_browser():
executable_path = {"executable_path":"C:\chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless = False)

def scrape():
    browser = init_browser()
    mars_facts_scrape = {}

# # NASA Mars News

#Go to the NASA news page
mars_news= "https://mars.nasa.gov/news/"
browser.visit(mars_news)
time.sleep(2)


#Use beautiful soup to write the data into html
html = browser.html
soup = bs(html,"html.parser")

# NASA Mars News

news_title = soup.find("div",class_="content_title").text
news_paragraph = soup.find("div", class_="article_teaser_body").text
mars_facts_scrape['news_title'] = news_title
mars_facts_scrape['news_paragraph'] = news_paragraph


# # JPL Mars Featured Space Images


nasa_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(nasa_image_url)
time.sleep(2)

#Ensure Full size jpg image view 

browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(2)
browser.click_link_by_partial_text('more info')
time.sleep(2)
browser.click_link_by_partial_text('.jpg')


#get image url using Beautiful soup
html = browser.html
soup = bs(html, 'html.parser')

featured_img_url = soup.find('img').get('src')
mars_fact_scrape["featured_img"] = featured_img_url


# # Mars Weather


#Get mars weather's latest tweet from the website
url_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_weather)

html_weather = browser.html
soup = bs(html_weather, "html.parser")
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
mars_fact_scrape["mars_weather"] = mars_weather


# # Mars Facts



mars_url_facts = "https://space-facts.com/mars/"
time.sleep(2)



table = pd.read_html(mars_url_facts)
table[0]
df_mars_facts = table[0]
df_mars_facts.columns = ["Parameter", "Values","Earth"]
df_mars_facts.set_index(["Parameter"])
mars_facts = df_mars_facts.drop(['Earth'], axis=1)
mars_html_table = df_mars_facts.to_html()
mars_html_table = mars_html_table.replace("\n","")
mars_fact_scrape["mars_facts_table"] = mars_html_table



mars_html_table = mars_facts.to_html()
mars_html_table = mars_html_table.replace("\n", "")
mars_html_table


# # Mars Hemispheres



mars_url_hemisphere = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_url_hemisphere)

html = browser.html
soup = bs(html, 'html.parser')




hemisphere_image_urls = []
hem_dict = {'title': [], 'img_url': [],}

x = soup.find_all('h3')


for i in x:
    t = i.get_text()
    title = t.strip('Enhanced')
    browser.click_link_by_partial_text(t)
    hemisphere_url = browser.find_link_by_partial_href('download')['href']
    hem_dict = {'title': title, 'img_url': url}
    hemisphere_image_urls.append(hem_dict)
    browser.back()

mars_fact_scrape["hemisphere"] = hemisphere_image_urls


return mars_data_scrape


