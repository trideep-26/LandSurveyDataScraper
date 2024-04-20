import requests
from bs4 import BeautifulSoup

def get_survey_numbers(district, mandal, village):
    # URL of the website
    url = "https://dharani.telangana.gov.in/knowLandStatus"

    # Data to select the district, mandal, and village
    data = {
        'district': district,
        'mandal': mandal,
        'village': village
    }

    # Send a POST request with the data
    response = requests.post(url, data=data)

    # Parsing the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the survey numbers on the page
    survey_numbers = soup.find_all('...')

    # Print the survey numbers
    for number in survey_numbers:
        print(number.text)

get_survey_numbers('Hyderabad', 'Ameerpet', 'SR Nagar')
