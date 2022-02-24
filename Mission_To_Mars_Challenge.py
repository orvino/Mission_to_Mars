{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "a1d79e77",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Splinter and BeautifulSoup\n",
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup as soup\n",
    "from webdriver_manager.chrome import ChromeDriverManager\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5eed5b41",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 98.0.4758\n",
      "Get LATEST chromedriver version for 98.0.4758 google-chrome\n",
      "Driver [/Users/mimir/.wdm/drivers/chromedriver/mac64/98.0.4758.102/chromedriver] found in cache\n"
     ]
    }
   ],
   "source": [
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "f16b3dab",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://redplanetscience.com'\n",
    "browser.visit(url)\n",
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css('div.list_text', wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "0f232b43",
   "metadata": {},
   "outputs": [],
   "source": [
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n",
    "slide_elem = news_soup.select_one('div.list_text')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "9c0e8bc4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"content_title\">NASA's Perseverance Rover Mission Getting in Shape for Launch</div>"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We'll want to assign the title and summary text to variables we'll reference later. In the next empty cell, let's begin our scraping. Type the following:\n",
    "slide_elem.find('div', class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "3708c17a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"NASA's Perseverance Rover Mission Getting in Shape for Launch\""
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the first `a` tag and save it as `news_title`\n",
    "news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ef3e244b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Stacking spacecraft components on top of each other is one of the final assembly steps before a mission launches to the Red Planet. '"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "123aa1a8",
   "metadata": {},
   "source": [
    "### Featured Images"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "dbdc15c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit URL\n",
    "url = 'https://spaceimages-mars.com'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "7c7691c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find and click the full image button\n",
    "full_image_elem = browser.find_by_tag('button')[1]\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "455abbff",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Parse the resulting html with soup\n",
    "html = browser.html\n",
    "img_soup = soup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "650bed82",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Find the relative image url\n",
    "img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "img_url_rel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "04553d98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://spaceimages-mars.com/image/featured/mars2.jpg'"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use the base URL to create an absolute URL\n",
    "img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "81bdb944",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>description</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <td>Mars</td>\n",
       "      <td>Earth</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "description                                              \n",
       "Mars - Earth Comparison             Mars            Earth\n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "df.columns=['description', 'Mars', 'Earth']\n",
    "df.set_index('description', inplace=True)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "e43a3ca4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mars_news():\n",
    "\n",
    "   # Visit the mars nasa news site\n",
    "   url = 'https://redplanetscience.com/'\n",
    "   browser.visit(url)\n",
    "\n",
    "   # Optional delay for loading the page\n",
    "   browser.is_element_present_by_css('div.list_text', wait_time=1)\n",
    "\n",
    "   # Convert the browser html to a soup object and then quit the browser\n",
    "   html = browser.html\n",
    "   news_soup = soup(html, 'html.parser')\n",
    "\n",
    "   slide_elem = news_soup.select_one('div.list_text')\n",
    "\n",
    "   # Use the parent element to find the first <a> tag and save it as `news_title`\n",
    "   news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "\n",
    "   # Use the parent element to find the paragraph text\n",
    "   news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "\n",
    "   return news_title, news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2b03c32a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mars_news(browser):\n",
    "\n",
    "    # Scrape Mars News\n",
    "    # Visit the mars nasa news site\n",
    "    url = 'https://redplanetscience.com/'\n",
    "    browser.visit(url)\n",
    "\n",
    "    # Optional delay for loading the page\n",
    "    browser.is_element_present_by_css('div.list_text', wait_time=1)\n",
    "\n",
    "    # Convert the browser html to a soup object and then quit the browser\n",
    "    html = browser.html\n",
    "    news_soup = soup(html, 'html.parser')\n",
    "\n",
    "    # Add try/except for error handling\n",
    "    try:\n",
    "        slide_elem = news_soup.select_one('div.list_text')\n",
    "        # Use the parent element to find the first 'a' tag and save it as 'news_title'\n",
    "        news_title = slide_elem.find('div', class_='content_title').get_text()\n",
    "        # Use the parent element to find the paragraph text\n",
    "        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()\n",
    "\n",
    "    except AttributeError:\n",
    "        return None, None\n",
    "\n",
    "    return news_title, news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "80a6e8c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def featured_image(browser):\n",
    "    # Visit URL\n",
    "    url = 'https://spaceimages-mars.com'\n",
    "    browser.visit(url)\n",
    "\n",
    "    # Find and click the full image button\n",
    "    full_image_elem = browser.find_by_tag('button')[1]\n",
    "    full_image_elem.click()\n",
    "\n",
    "    # Parse the resulting html with soup\n",
    "    html = browser.html\n",
    "    img_soup = soup(html, 'html.parser')\n",
    "\n",
    "    # Add try/except for error handling\n",
    "    try:\n",
    "        # Find the relative image url\n",
    "        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')\n",
    "\n",
    "    except AttributeError:\n",
    "        return None\n",
    "\n",
    "    # Use the base url to create an absolute url\n",
    "    img_url = f'https://spaceimages-mars.com/{img_url_rel}'\n",
    "\n",
    "    return img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "87b0a345",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mars_facts():\n",
    "    # Add try/except for error handling\n",
    "    try:\n",
    "        # Use 'read_html' to scrape the facts table into a dataframe\n",
    "        df = pd.read_html('https://galaxyfacts-mars.com')[0]\n",
    "\n",
    "    except BaseException:\n",
    "        return None\n",
    "\n",
    "    # Assign columns and set index of dataframe\n",
    "    df.columns=['Description', 'Mars', 'Earth']\n",
    "    df.set_index('Description', inplace=True)\n",
    "\n",
    "    # Convert dataframe into HTML format, add bootstrap\n",
    "    return df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "440ed5a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# browser.quit()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "218f5617",
   "metadata": {},
   "source": [
    "# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fae0606c",
   "metadata": {},
   "source": [
    "### Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "871f6bfc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 1. Use browser to visit the URL \n",
    "url = 'https://marshemispheres.com/'\n",
    "\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "abb42565",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<h3>Cerberus Hemisphere Enhanced</h3>,\n",
       " <h3>Schiaparelli Hemisphere Enhanced</h3>,\n",
       " <h3>Syrtis Major Hemisphere Enhanced</h3>,\n",
       " <h3>Valles Marineris Hemisphere Enhanced</h3>,\n",
       " <h3>Back</h3>]"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 2. Create a list to hold the images and titles.\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "# 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    "html = browser.html\n",
    "hemi_soup = soup(html, 'html.parser')\n",
    "\n",
    "# links for each of the 4 hemispheres\n",
    "hemi_links = hemi_soup.find_all('h3')\n",
    "\n",
    "hemi_links\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "a72307f4",
   "metadata": {},
   "outputs": [
    {
     "ename": "ElementNotInteractableException",
     "evalue": "Message: element not interactable\n  (Session info: chrome=98.0.4758.102)\nStacktrace:\n0   chromedriver                        0x0000000100e4aee9 chromedriver + 5013225\n1   chromedriver                        0x0000000100dd61d3 chromedriver + 4534739\n2   chromedriver                        0x00000001009ac91f chromedriver + 170271\n3   chromedriver                        0x00000001009e2227 chromedriver + 389671\n4   chromedriver                        0x00000001009d6359 chromedriver + 340825\n5   chromedriver                        0x00000001009fe7e2 chromedriver + 505826\n6   chromedriver                        0x00000001009d5bf5 chromedriver + 338933\n7   chromedriver                        0x00000001009fe8ee chromedriver + 506094\n8   chromedriver                        0x0000000100a11074 chromedriver + 581748\n9   chromedriver                        0x00000001009fe6d3 chromedriver + 505555\n10  chromedriver                        0x00000001009d476e chromedriver + 333678\n11  chromedriver                        0x00000001009d5745 chromedriver + 337733\n12  chromedriver                        0x0000000100e06efe chromedriver + 4734718\n13  chromedriver                        0x0000000100e20a19 chromedriver + 4839961\n14  chromedriver                        0x0000000100e261c8 chromedriver + 4862408\n15  chromedriver                        0x0000000100e213aa chromedriver + 4842410\n16  chromedriver                        0x0000000100dfba01 chromedriver + 4688385\n17  chromedriver                        0x0000000100e3c538 chromedriver + 4953400\n18  chromedriver                        0x0000000100e3c6c1 chromedriver + 4953793\n19  chromedriver                        0x0000000100e52225 chromedriver + 5042725\n20  libsystem_pthread.dylib             0x00007ff81f9d64f4 _pthread_start + 125\n21  libsystem_pthread.dylib             0x00007ff81f9d200f thread_start + 15\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mElementNotInteractableException\u001b[0m           Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-43-d3ea7fb1cfd8>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mhemi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mhemi_links\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0mimg_page\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_by_text\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhemi\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m     \u001b[0mimg_page\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m     \u001b[0mhtml\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhtml\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[0mimg_soup\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msoup\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhtml\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'html.parser'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/site-packages/splinter/driver/webdriver/__init__.py\u001b[0m in \u001b[0;36mclick\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    822\u001b[0m                 \u001b[0merror\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    823\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 824\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0merror\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    825\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    826\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mcheck\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/site-packages/splinter/driver/webdriver/__init__.py\u001b[0m in \u001b[0;36mclick\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    815\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mend_time\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    816\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 817\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_element\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    818\u001b[0m             except(\n\u001b[1;32m    819\u001b[0m                 \u001b[0mElementClickInterceptedException\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/site-packages/selenium/webdriver/remote/webelement.py\u001b[0m in \u001b[0;36mclick\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     79\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     80\u001b[0m         \u001b[0;34m\"\"\"Clicks the element.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 81\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_execute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mCLICK_ELEMENT\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     82\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     83\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0msubmit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/site-packages/selenium/webdriver/remote/webelement.py\u001b[0m in \u001b[0;36m_execute\u001b[0;34m(self, command, params)\u001b[0m\n\u001b[1;32m    708\u001b[0m             \u001b[0mparams\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    709\u001b[0m         \u001b[0mparams\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'id'\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_id\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 710\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommand\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    711\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    712\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mfind_element\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mby\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mID\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    422\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    423\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 424\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    425\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[1;32m    426\u001b[0m                 response.get('value', None))\n",
      "\u001b[0;32m~/opt/anaconda3/envs/PythonData/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    245\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'alert'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'text'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    246\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# type: ignore[call-arg]  # mypy is not smart enough here\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 247\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    248\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    249\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mMapping\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0m_KT\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0m_VT\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0m_KT\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0m_VT\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0m_VT\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mElementNotInteractableException\u001b[0m: Message: element not interactable\n  (Session info: chrome=98.0.4758.102)\nStacktrace:\n0   chromedriver                        0x0000000100e4aee9 chromedriver + 5013225\n1   chromedriver                        0x0000000100dd61d3 chromedriver + 4534739\n2   chromedriver                        0x00000001009ac91f chromedriver + 170271\n3   chromedriver                        0x00000001009e2227 chromedriver + 389671\n4   chromedriver                        0x00000001009d6359 chromedriver + 340825\n5   chromedriver                        0x00000001009fe7e2 chromedriver + 505826\n6   chromedriver                        0x00000001009d5bf5 chromedriver + 338933\n7   chromedriver                        0x00000001009fe8ee chromedriver + 506094\n8   chromedriver                        0x0000000100a11074 chromedriver + 581748\n9   chromedriver                        0x00000001009fe6d3 chromedriver + 505555\n10  chromedriver                        0x00000001009d476e chromedriver + 333678\n11  chromedriver                        0x00000001009d5745 chromedriver + 337733\n12  chromedriver                        0x0000000100e06efe chromedriver + 4734718\n13  chromedriver                        0x0000000100e20a19 chromedriver + 4839961\n14  chromedriver                        0x0000000100e261c8 chromedriver + 4862408\n15  chromedriver                        0x0000000100e213aa chromedriver + 4842410\n16  chromedriver                        0x0000000100dfba01 chromedriver + 4688385\n17  chromedriver                        0x0000000100e3c538 chromedriver + 4953400\n18  chromedriver                        0x0000000100e3c6c1 chromedriver + 4953793\n19  chromedriver                        0x0000000100e52225 chromedriver + 5042725\n20  libsystem_pthread.dylib             0x00007ff81f9d64f4 _pthread_start + 125\n21  libsystem_pthread.dylib             0x00007ff81f9d200f thread_start + 15\n"
     ]
    }
   ],
   "source": [
    "# loop through each hemisphere link\n",
    "for hemi in hemi_links:\n",
    "    img_page = browser.find_by_text(hemi.text)\n",
    "    img_page.click()\n",
    "    html= browser.html\n",
    "    img_soup = soup(html, 'html.parser')\n",
    "    # Scrape the image link\n",
    "    img_url = 'https://marshemispheres.com/' + str(img_soup.find('img', class_='wide-image')['src'])\n",
    "    # Scrape the title\n",
    "    title = img_soup.find('h2', class_='title').text\n",
    "    # Define and append to the dictionary\n",
    "    hemi_dict = {'img_url': img_url,'title': title}\n",
    "    hemisphere_image_urls.append(hemi_dict)\n",
    "    browser.back()\n",
    "    # Error appears to be due to Chrome browser being updated.  Has no effect on outcome."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e543f12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'img_url': 'https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg',\n",
       "  'title': 'Cerberus Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg',\n",
       "  'title': 'Schiaparelli Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg',\n",
       "  'title': 'Syrtis Major Hemisphere Enhanced'},\n",
       " {'img_url': 'https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg',\n",
       "  'title': 'Valles Marineris Hemisphere Enhanced'}]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4. Print the list that holds the dictionary of each image url and title.\n",
    "hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1fcfbcc6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 5. Quit the browser\n",
    "browser.quit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46437dca",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35c5e531",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "740000aa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3084e691",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4220a8a9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9e7d02a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a983a775",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "b31670b8fd7bc6a3eb168e40dcc0a94c16f5d4ef6cc9dea5cc7e28b5803d42ff"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
