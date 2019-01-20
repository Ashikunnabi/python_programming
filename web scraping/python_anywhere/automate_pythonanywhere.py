import requests
from bs4 import BeautifulSoup as bs

url = "https://www.pythonanywhere.com/login/"

# Collect information from Network tab
request_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '170',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.pythonanywhere.com',
    'Origin': 'https://www.pythonanywhere.com',
    'Referer': 'https://www.pythonanywhere.com/login/',
    'Upgrade-Insecure-Requests': '1',
    'User-ArithmeticError': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

login_data = {
    'csrfmiddlewaretoken': '',
    'auth-username': 'YOUR USERNAME',   #  Fill up properly
    'auth-password': 'YOUR PASSWORD',   #  Fill up properly
    'login_view-current_step': 'auth'
    }

with requests.Session() as session:
    # Login to Pythonanywhere 
    # Get reqest 
    response = session.get(url)
    soup = bs(response.content, 'html.parser')
    # Collecting CSRF value
    login_data['csrfmiddlewaretoken'] = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']     
    # Post request for login
    response = session.post(url, data=login_data, headers=request_headers)


    # Active Pythonanywhere for next 3 months
    web_tab_url = 'https://www.pythonanywhere.com/user/'+login_data['auth-username']+'/webapps/'
    submit_url = 'https://www.pythonanywhere.com/user/'+login_data['auth-username']+'/webapps/'+login_data['auth-username']+'.pythonanywhere.com/extend'
    request_headers['Referer']='https://www.pythonanywhere.com/user/'+login_data['auth-username']+'/webapps/'
    context = {
        'csrfmiddlewaretoken': '',        
        }
    # Get reqest 
    response = session.get(web_tab_url)
    soup = bs(response.content, 'html.parser')
    # Collecting CSRF value
    context['csrfmiddlewaretoken'] = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value'] 
    # Post request for next 3 month activation
    response = session.post(submit_url, data=context, headers=request_headers) 
    print("Successfull")
    
