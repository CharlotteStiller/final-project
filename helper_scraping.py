from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import time
import requests

'''
this function gives us the number of pages we have to itterate for each category 
'''

def page_finder(url): 
    website =  requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')
    finder = soup.find_all(class_={"pagination-title__option-item"})
    pages = finder[0].get_text()
    number_of_pages = pages[12:15]
    return number_of_pages


'''
this function gives us the url of pages we have to itterate for each category 
'''

def category_urls(url):
    num_pages = int(page_finder(url))
    liste = []
    for i in range(1, num_pages, 1):
        liste.append(url + "?page=" + str(i))
    return liste


'''
this function gives us the rating and the id of every product
'''
def id_rating_scraper(url):
    http = httplib2.Http()
    website =  requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')
    list_new = []
    
    time.sleep(5)
    for link in soup.find_all('a',class_ = 'link link--no-decoration product-tile__main-link', href=True):
        list_new.append(link['href'])
    star_finder = soup.find_all('div', class_={'product-tile__details'})
    star_list = []
    
    time.sleep(random.randint(5,16))
    for i in star_finder:
        x = i.find('span', class_={'product-tile__ratings-info'})
        if x == None:
            star_list.append(None)
        else:
            star_list.append(x.get_text())

    return list_new, star_list


'''
this function return the rating cleaned
'''
def id_rating_cleaner(url):
    x,y = id_rating_scraper(url)
    time.sleep(10)
    
    
    url = []
    for i in x: 
        url.append("https://www.website.de"+ i)
    
    new_y = []
    for i in y:
        if i != None:
            new_y.append(i.replace('\xa0',' '))
        else:
            new_y.append(None)

    rating, num_rating = [],[]
    for i in new_y:
        if i != None:
            rating.append(i.split('(')[0].strip())
            num_rating.append(i.split('(')[1][:-1])
        else:
            rating.append(None)
            num_rating.append(None)
    df_url_ratin = pd.DataFrame(
    {"url": url,
     "rating": rating,
     "number_rating": num_rating,
     })
    
    return df_url_rating



"""
This functions gets the size of the product. 
The size is given in ml (50 ml) or in counting (1 Stk, 1 Stück)

"""

def size_getter(url): 
    website = requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')
    try: 
        ml_finder = soup.find_all(class_={'product-detail__variant-name'})
        ml_finder

        ml = []
        for i in ml_finder: 
            ml.append(i.get_text())
            size_one = ml[0]
            return size_one
    except:
        ml = []
        
        ml.append("None")
        return size_one
    
    
    
"""
This functions gets the original price of the product in Euro (24,99€). 
If there is a discounted price the original price is strikethrough and the function will take the strikethrough price. 

"""

def price_getter(url):
    website = requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')
    price_finder = soup.find_all(class_={'product-price'})
    price_finder
    prices_2 = []
    for i in price_finder: 
        prices_2.append(i.get_text())
        price_two = prices_2[0].replace('\xa0', '')
        return price_two
    
    
"""
This functions gets the brand of the product (Yves Saint Laurent).  

"""

def brand_getter(url): 
    website = requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')
    brand_finder = soup.find_all(class_={'brand-logo__text brand-logo__text--dynamic'})
    brand_finder

    for i in brand_finder: 
        brand_3 = i.get_text()
        brand = brand_3
        return brand
    
    
"""
This functions gets the typ of the product (Parfum, Set, Mascara).  

"""


def typ_getter(url): 
    website = requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')

    typ_finder = soup.find_all(class_={'third-line'})
    typ_finder

    for i in typ_finder: 
        typ = i.get_text()
        return typ
"""
This functions gets the name of the product (Good GirlEau de Parfum Spray).  

"""

def product_getter(url):
    website = requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')
    product_finder = soup.find_all(class_={'second-line'})
    product_finder

    for i in product_finder: 
        products_list = i.get_text()
    
        return products_list
    
    
    
"""
This functions gets more details of the product
ITEM_NB = The item number (031546)
EFFECT = The effect of the product (refining / verfeinernd)
AGE = The age for which the product is recommended
CHARESTERISTICS = characteristics of the product (smoothing, protective / glättend, schützend) 
PRODUCT AWARD = What distinguishes the product in particular (microplastic-free, paraffin-free)
SCOPE = Is the area of application for which the product is suitable (face / Gesicht)

"""


def details_getter(url):
    website = requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')
    details = []
    details_finder = soup.find_all(class_={'classification__item'})
    
    for i in details_finder:
        details.append(i.get_text())
    
    details_iter = iter(details)
    details_dict_object = itertools.zip_longest(details_iter, details_iter, fillvalue=None)
    details_dict = dict(details_dict_object)

    for i in details_dict:
        try:
            item_nb = details_dict['Art-Nr.']
        except:
            item_nb = "0"
        try:
            effect = details_dict['Effekt']
        except:
            effect = "None"

        try:
            age = details_dict['Alter']
        except:
            age = "None"

        try:
            charesteristics = details_dict['Eigenschaft']
        except:
            charesteristics = "None"

        try:
            product_award = details_dict['Produktauszeichnung']
        except:
            product_award = "None"

        try:
            scope = details_dict['Anwendungsbereich']
        except:
            scope = "None"
 
        detail_list = [item_nb, effect, age, charesteristics, product_award, scope]
    
        return detail_list 
    
"""
This functions gets the name of the product (FACE / GESICHT, BODY / KÖRPER ).  

"""

def category_getter(url): 
    website = requests.get(url)
    soup = BeautifulSoup(website.content, 'html.parser')
    
    try: 
        category_finder = soup.find_all(class_={'link link--text'})
        time.sleep(1)
        category = category_finder[0].get_text()
        return category
    except:
        category = "None"
        return category
    
    
"""
This functions calls all the functions to get the product details and returns the data in a dataframe

"""

def get_data(url_list):
    
    sizes_list = []
    prices_list = []
    brand_list = []
    product_list = []
    typ_list = []
    item_nb_list = []
    effect_list = []
    age_list = []
    charesteristics_list = []
    product_award_list = []
    scope_list = []
    category_list = []
    
    for i in url_list: 
        
        size = size_getter(i)
        sizes_list.append(size)
        time.sleep(random.randint(1,4))
        
        
        price = price_getter(i)
        prices_list.append(price)

        brand_1 = brand_getter(i)
        brand_list.append(brand_1)
        time.sleep(random.randint(1,4))

        typ = typ_getter(i)
        typ_list.append(typ)

        
        product = product_getter(i)
        product_list.append(product)
        
        time.sleep(random.randint(1,4))
        
        details = details_getter(i)
        
        try: 
            item_nb_list.append(details[0])
        except:
            item_nb_list.append('Null')
        
        try: 
            effect_list.append(details[1])
        except:
            effect_list.append('Null')
            
        try:
            age_list.append(details[2])
        except:
            age_list.append("Null")
            
        try:
            charesteristics_list.append(details[3])
        except:
            charesteristics_list.append("Null")
            
        try:
            product_award_list.append(details[4])
        except:
            product_award_list.append("Null")
        
        try:
            scope_list.append(details[5])
        except:
            scope_list.append("Null")
        
        category = category_getter(i)
        category_list.append(category) 
        
        
    df_02 = pd.DataFrame(
    {
     "item_nb": item_nb_list, 
     "brand": brand_list,
     "product": product_list,
     "size": sizes_list,
     "price": prices_list,
     "category": category_list,
     "type": typ_list, 
     "effect": effect_list, 
     "scope": scope_list, 
     "age": age_list,
     "charesteristics": charesteristics_list, 
     "product_award": product_award_list,
     "url": url_list
     }
    )
    df_02
        
    return df_02    