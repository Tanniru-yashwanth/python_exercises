from bs4 import BeautifulSoup

with open("S:/material/sample.xml", mode='r') as file:
    data = file.read()
Bs_data = BeautifulSoup(data, "html.parser")
b_unique = Bs_data.find_all('unique')
print(b_unique)
b_name = Bs_data.find('year')
print(b_name)
