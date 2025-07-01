import requests
from bs4 import BeautifulSoup
from django.shortcuts import redirect, HttpResponse
import requests
from django.shortcuts import render
from django.http import JsonResponse
from urllib.parse import urljoin  
import time
import re

def home(request):
    return render(request,"home.html")

def get_page_description(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        description_tag = soup.find('meta', attrs={'name': 'description'})
        if description_tag:
            description = description_tag.get('content')
            return description
        text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        description = ""
        for element in text_elements:
            description += element.get_text(strip=True) + " "
            if len(description) >= 200:  
                break
        print("des",description)
        return description.strip() if description else None
    return None

def get_page_title(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string if soup.title else 'Title not found'
            return title
        else:
            return 'HTTP Error: ' + str(response.status_code)
    except Exception as e:
        return 'Error fetching title: ' + str(e)
    
    
def get_images_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            base_url = response.url  
            image_urls = []
            img_tags = soup.find_all('img', src=True)

            for img in img_tags:
                img_url = img['src']
                if not img_url.startswith(('data:', 'http:', 'https:')):
                    img_url = urljoin(base_url, img_url)
                    if img_url.lower().endswith(('.jpg', '.jpeg',)):
                        image_urls.append(img_url)
            print(image_urls)

            return image_urls

        return []
    except Exception as e:
        return []


def extract_price_from_text(text):
    price_pattern = r'₹([\d,]+)'
    matches = re.findall(price_pattern, text)
    if matches:
        return matches[0]
    else:
        return None


def get_page_price(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            description_tag = soup.find('meta', attrs={'name': 'description'})
            description = description_tag.get('content') if description_tag else None
            price_elements = soup.find_all(text=re.compile(r'₹'))
            prices = [extract_price_from_text(price_element.strip()) for price_element in price_elements]
            prices = [price for price in prices if price is not None]
            first_price = prices[0] if prices else None

            return first_price
        else:
            return 'HTTP Error: ' + str(response.status_code)
    except Exception as e:
        return 'Error fetching price: ' + str(e)

website_urls = [
    'https://www.flipkart.com',
    'https://www.meesho.com',
    'https://www.amazon.com', 
    'https://www.ajio.com', 
    'https://www.jiomart.com',
    'https://www.gsmarena.com',
    'https://www.gadgets360.com',
    'https://www.mi.com',
    'https://www.gsmarena.com',
]


prices_dict = {}

for url in website_urls:
    price = get_page_price(url)
    prices_dict[url] = price

for url, price in prices_dict.items():
    print(f'Website: {url}\nPrice: {price}\n')


def get_serpstack_search_results(query):
    api_key = 'ae36a47341d79dc0ac4f174ce6ca556e'  
    base_url = 'http://api.serpstack.com/search'
    num_results = 20

    params = {
        'access_key': api_key,
        'query': query,
        'num': num_results,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        max_results = 10  
        search_results = data.get('organic_results', [])[:max_results]
        return search_results
    else:
        return None

def chatbot_response(request):
    if request.method == 'POST':
        user_query = request.POST.get('query')
        search_results = get_serpstack_search_results(user_query)

        if search_results:
            specific_sites = ['flipkart.com', 'meesho.com', 'amazon.com', 'gsmarena.com', 'gadgets360','ajio.com','jiomart.com','mi.com']
            results_data = []
            for result in search_results:
                link = result.get('url', '')
                title = result.get('title', '')

                for site in specific_sites:
                    if site in link:
                        description = get_page_description(link)
                        price=get_page_price(link)
                      
                        image_urls = get_images_from_url(link)

                        results_data.append({
                            'link': link,
                            'title': title,
                            'description': description,
                            'images': image_urls,
                            'price':price,
                            'query': user_query,
                        })
                        break 
            print("Number of Results:", len(results_data))

            return render(request, 'chatbot_response.html', {'results_data': results_data})
        else:
            return render(request, 'chatbot_response.html', {'error_message': "No results found."})

    return render(request, 'chatbot_form.html')

def chatbot_form(request):
        return render(request, 'chatbot_form.html')
    
    
    