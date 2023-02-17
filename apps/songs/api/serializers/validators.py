import requests

def is_valid_url(url:str)->bool:
  try:
    response = requests.get(url)
    if response.status_code == 200:
      
      return True

    return False

  except requests.exceptions.RequestException as e:

    return False