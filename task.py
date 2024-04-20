import requests
from bs4 import BeautifulSoup

url = "https://www.yellowpages-uae.com/uae/restaurant"

response = requests.get(url)


if response.status_code == 200:
  soup = BeautifulSoup(response.text, "html.parser")
  restaurants = soup.find_all("div", class_="listing-details")
  restaurant_data = []

  for restaurant in restaurants:
 
    name_tag = restaurant.find("h2", class_="cmp_name")
    if name_tag:
      name = name_tag.text.strip()
    else:
      name = "NA"

    location_tag = restaurant.find("span", class_="location")  
    if location_tag:
      location = location_tag.text.strip()
    else:
      location = "NA"

    city_tag = restaurant.find("span", class_="locationCity")  
    if city_tag:
      city = city_tag.text.strip()
    else:
      city = "NA"

    po_box_tag = restaurant.find("span", class_="postalCode")  
    if po_box_tag:
      po_box = po_box_tag.text.strip()
    else:
      po_box = "NA"

    phone_tag = restaurant.find("span", class_="phone") 
    if phone_tag:
      phone = phone_tag.text.strip()
    else:
      phone = "NA"

    mobile_tag = restaurant.find("span", class_="phone") 
    if mobile_tag:
      mobile = mobile_tag.text.strip()
    else:
      mobile = "NA"

    company_link_tag = restaurant.find("a", class_="website")
    if company_link_tag:
      company_link = company_link_tag["href"]
    else:
      company_link = "NA"

    logo_tag = restaurant.find("img", class_="ver lazyloaded") 
    if logo_tag:
      logo_url = logo_tag["src"]
    else:
      logo_url = "NA"

    restaurant_data.append({
      "Name": name,
      "Location": location,
      "City": city,
      "PO Box": po_box,
      "Phone": phone,
      "Mobile": mobile,
      "Company Page Link": company_link,
      "Logo URL": logo_url
    })

  with open("restaurant_data.csv", "w", newline="") as csvfile:
    import csv
    writer = csv.DictWriter(csvfile, fieldnames=[
      "Name", "Location", "City", "PO Box", "Phone", "Mobile", "Company Page Link", "Logo URL"
    ])
    writer.writeheader()
    writer.writerows(restaurant_data)

  print("Restaurant data scraped successfully!")
else:
  print(f"Error: Failed to retrieve data. Status code: {response.status_code}")
