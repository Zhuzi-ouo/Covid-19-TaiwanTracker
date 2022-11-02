import requests
from bs4 import BeautifulSoup

class function_covid:
  def __init__(self):
    response=requests.get("https://www.worldometers.info/coronavirus/country/taiwan/")
    soup=BeautifulSoup(response.text,"html.parser")
    result=soup.find_all("div",attrs={"class":"maincounter-number"})
    self.cases=result[0].select_one("span").text
    self.death=result[1].select_one("span").text
    self.recovered=result[2].select_one("span").text