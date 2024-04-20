import csv
import requests
from bs4 import BeautifulSoup
import re
import urllib.request

# Function to extract logo URL
def extract_logo_url(soup):
    logo_tag = soup.find('div', {'class': 'ver lazyloaded'})
    if logo_tag and logo_tag.img:
        return logo_tag.img['src']
    return None

# Function to extract company page link
def extract_company_page_link(soup):
    company_page_link = soup.find('a', {'class': 'cmp_name'})
    if company_page_link:
        return company_page_link['href']
    return None

# Scrape the data from a single page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    #soup = BeautifulSoup(response.content, 'html5lib') 
    # If this line causes an error, run 'pip install html5lib' or install html5lib 
    #print(soup.prettify()) 
    data = []

   #for restaurant in soup.find_all('div', {'class': 'business-info'}):
   #   row title-row
    for restaurant in soup.find_all('div', {'class': 'row title-row'}):
        name = restaurant.find('h2', {'class': 'cmp_name'}).text.strip()
        print("NAME ::::" , name)
        '''
        location = restaurant.find('div', {'class': 'address-section'}).text.strip()
        city = restaurant.find('span', {'class': 'locationCity'}).text.strip()
        p_o_box = restaurant.find('span', {'class': 'pobox'})
        if p_o_box:
            p_o_box = p_o_box.text.strip()
        else:
            p_o_box = None

        phone = restaurant.find('span', {'class': 'phone'}).text.strip()
        mobile = restaurant.find('span', {'class': 'telephone'})
        if mobile:
            mobile = mobile.text.strip()
        else:
            mobile = None
        
        company_page_link = extract_company_page_link(restaurant)
        logo_url = extract_logo_url(restaurant)

        data.append({
            'name': name,
            'location': location,
            'city': city,
            'p_o_box': p_o_box,
            'phone': phone,
            'mobile': mobile,
            'company_page_link': company_page_link,
            'logo_url': logo_url
        })
        '''
        data.append({
            'name': name
        })
        print("In here :::: ", data)
    return data

# Scrape multiple pages and save the data to a CSV file
def scrape_multiple_pages(base_url, num_pages):
    print("insideScrapping function")
    data = []
    for i in range(1, num_pages + 1):
        url = f"{base_url}?page={i}"
        print(f"Scraping {url}")
        page_data = scrape_page(url)
        print("page_data", page_data)
        data.extend(page_data)

    with open('restaurants.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'location', 'city', 'p_o_box', 'phone', 'mobile', 'company_page_link', 'logo_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Set the base URL and number of pages to scrape
base_url = "https://www.yellowpages-uae.com/uae/restaurant"
num_pages = 1  # Change this value to scrape more pages

# Call the function to scrape multiple pages and save the data to a CSV file
scrape_multiple_pages(base_url,num_pages)
