import requests
from bs4 import BeautifulSoup

class Product:
  def __init__(self, amazon_url,flipkart_url,mobiles_url,headers):
    self.amazon_url = amazon_url
    self.flipkart_url = flipkart_url
    self.mobiles = mobiles_url
    self.headers  = headers
  def myfunc(self):
    page=requests.get(flipkart_url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    soup.prettify

    print("<--Flipkart-->")
    name1  = soup.find( class_= "B_NuCI")
    t = name1.get_text()
    print(t.strip())
    print( )
    price  = soup.find( class_= "_30jeq3 _16Jk6d")
    a = price.get_text()
    print(a.strip())

    flipkart_price=a.strip()
    print( )
    print("Rating:")
    rating1 = soup.find(class_="_3LWZlK")
    q = rating1.get_text()
    print(q.strip())
    flipkart_rating = q.strip()

    print("<-- 91 Mobiles -->")
    print( )


    page1=requests.get(mobiles_url,headers=headers)
    soup = BeautifulSoup(page1.content,'html.parser')
    soup.prettify

    name = soup.find(class_="h1_pro_head")
    l = name.get_text()
    print(l.strip())
    print( )
    price1 = soup.find(class_="store_prc") 
    b = price1.get_text()
    print(b.strip())
    mobiles_price= b.strip()
    print( )
    print("Rating:")
    rating = soup.find(class_="ratpt")
    u = rating.get_text()
    print(u.strip())
    mobiles_rating = u.strip()


    print("<--Amazon-->")
    print( )

    page3=requests.get(amazon_url,headers=headers)
    soup = BeautifulSoup(page3.content,'html.parser')
    soup.prettify
    name3 = soup.find(id="productTitle")
    u = name3.get_text()
    print(u.strip())
    print( )
    price3 = soup.find(class_="a-offscreen")
    m = price3.get_text()
    print(m.strip())
    amazon_price = m.strip()
    
    print( )
    print("Rating:")
    rating2 = soup.find(class_="a-icon-alt")
    g = rating2.get_text()
    print(g.strip())
    amazon_rating = g.strip()

    amazon_price = (amazon_price[1:])
    flipkart_price = (flipkart_price[1:])
    mobiles_price = (mobiles_price[4:])


    amazon_rating = (amazon_rating[0:2])
    flipkart_rating = (flipkart_rating[0:])
    mobiles_rating = (mobiles_rating[0:2])
    min_price = min (amazon_price,flipkart_price,mobiles_price)

    #max_rating = max (amazon_rating,flipkart_rating,mobiles_rating)

    if(min_price==amazon_price ):
     URL = amazon_url
     company="Amazon"
    elif(min_price==flipkart_price ):
     URL = flipkart_url
     company="Flipkart"
    else:
     company = "91 Mobiles"
     URL = mobiles_url
    print( )
    print("Best Product is:")
    print(company)
    if(company=="Flipkart"):
     print("Reviews :")
     page=requests.get(flipkart_url,headers=headers)
     soup = BeautifulSoup(page.content,'html.parser')
     soup.prettify
     for paragraph in soup.find_all(class_="t-ZTKy"):
      print(paragraph.string)
      print(str(paragraph.text))
      print()
    elif(company == "Amazon"):
     page3=requests.get(amazon_url,headers=headers)
     soup = BeautifulSoup(page3.content,'html.parser')
     soup.prettify
     for paragraph1 in soup.find_all(class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content"):
      print(paragraph1.string)
      print(str(paragraph1.text))

    else:
     page1=requests.get(mobiles_url,headers=headers)
     soup = BeautifulSoup(page1.content,'html.parser')
     soup.prettify
   
    for paragraph1 in soup.find_all(class_="details_p preLine"):
     print(paragraph1.string)
     print(str(paragraph1.text))

    print()

    print("Link to go:")
    print(URL)

print("                                        <------ Product Analysis-------> \n")
print("Websites Used Amazon,Flipkart,91_Mobiles \n")
print("You have the Follwing Products \n")
print("1. OPPO K10 \n")
print("2. SAMSUNG A23 \n")
print("3. REALME 9 \n")
print("4. REALME NARZO  \n")
print("5. SAMSUNG M53 \n")
print("6. REDMI NOTE 11 \n")  
print("7. POCO X3 PRO \n")
print("Enter 0 For Exit \n")

print("Enter Product Name \n")
product= (input())

while(product!=0):
  if(product == "OPPO K10"):
    print("Variant Available \n")
    print("1. 6 GB/128 GB \n")
    print("2. 8 GB/ 128 GB \n")

    print("Enter 0 to Return Back \n")
    specification = int(input())
    while(specification!=0):
        if(specification==1):
         amazon_url ='https://www.amazon.in/OPPO-Ocean-Blue-128GB-Storage/dp/B09ZHRNP28/ref=sr_1_1?adgrpid=144946086907&ext_vrnc=hi&gclid=CjwKCAiA7IGcBhA8EiwAFfUDscuUKg5t5b2bK1pK26_uNDpxkaZqvz6NW6KkRPfLXbG57djCdxodFxoCrXUQAvD_BwE&hvadid=625454263140&hvdev=c&hvlocphy=9298142&hvnetw=g&hvqmt=b&hvrand=1385209887476762939&hvtargid=kwd-1823351877969&hydadcr=24538_2265412&keywords=oppo%2Bk10%2Bmobile%2B5g%2B8%2B128&qid=1669366564&qu=eyJxc2MiOiIxLjgzIiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sr=8-1&th=1'
         flipkart_url = 'https://www.flipkart.com/oppo-k10-black-carbon-128-gb/p/itm6205e7e72fe0c'
         mobiles_url = 'https://www.91mobiles.com/oppo-k10-price-in-india'
         headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
         oppo_k10_1 = Product(amazon_url,flipkart_url,mobiles_url,headers)
         oppo_k10_1.myfunc()
         
        elif(specification==2):
            amazon_url ='https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B09VK5D8KW?th=1'
            flipkart_url = 'https://www.flipkart.com/oppo-k10-5g-midnight-black-128-gb/p/itm28cf887931942?pid=MOBGETEKHMT7HMR7&lid=LSTMOBGETEKHMT7HMR7WHUWBT&marketplace=FLIPKART&q=oppo+k10+5g+8+128&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_12_na_na_na&fm=organic&iid=d8739837-767e-4e14-b063-d687c047c542.MOBGETEKHMT7HMR7.SEARCH&ppt=pp&ppn=pp&ssid=d9d3dtwhxc0000001668260435445&qH=edeb7b303bedb77b'
            mobiles_url = 'https://www.91mobiles.com/samsung-galaxy-a23-price-in-india'
            headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
            oppo_k10_2 = Product(amazon_url,flipkart_url,mobiles_url,headers)
            oppo_k10_2.myfunc()

        print("Variant Available \n")
        print("1. 6 GB/128 GB \n")
        print("2. 8 GB/ 128 GB \n")

        print("Enter 0 to Return Back \n")
        specification = int(input())
  elif(product == "SAMSUNG A23"):
     print("Variant Available \n")
     print("1. 6 GB/128 GB \n")
     print("2. 8 GB/ 128 GB \n")

     print("Enter 0 to Return Back \n")
     specification = int(input())
     while(specification!=0):
        if(specification==1):
          amazon_url ='https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B09VK34ZZR?th=1'
          flipkart_url = 'https://www.flipkart.com/samsung-galaxy-a23-black-128-gb/p/itm742a1886f56eb?pid=MOBGCFVYBAHXBGYM&lid=LSTMOBGCFVYBAHXBGYMSD4FVZ&marketplace=FLIPKART&sattr[]=color&sattr[]=ram&st=ram'
          mobiles_url = 'https://www.91mobiles.com/samsung-galaxy-a23-price-in-india'
          headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
          Samsung_A23__1 = Product(amazon_url,flipkart_url,mobiles_url,headers)
          Samsung_A23__1.myfunc()
         
        elif(specification==2):
            amazon_url ='https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B09VK5Y947?th=1'
            flipkart_url = 'https://www.flipkart.com/samsung-galaxy-a23-black-128-gb/p/itm7217aca85e502?pid=MOBGCFVYYDZT7HDH&lid=LSTMOBGCFVYYDZT7HDHINVQGI&marketplace=FLIPKART&sattr[]=color&sattr[]=ram&st=ram'
            mobiles_url = 'https://www.91mobiles.com/samsung-galaxy-a23-8gb-ram-price-in-india'
            headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
            Samsung_A23_2 = Product(amazon_url,flipkart_url,mobiles_url,headers)
            Samsung_A23_2.myfunc()
        
        print("Variant Available \n")
        print("1. 6 GB/128 GB \n")
        print("2. 8 GB/ 128 GB \n")
        print("Enter 0 to Return Back \n")
        specification = int(input())
  elif(product == "REDMI NOTE 11"):
     print("Variant Available \n")
     print("1. 6 GB/128 GB \n")
     print("2. 8 GB/128 GB \n")

     print("Enter 0 to Return Back \n")
     specification = int(input())
     while(specification!=0):
        if(specification==1):
         amazon_url = 'https://www.amazon.in/Redmi-Storage-Additional-Exchange-Included/dp/B09T2WPLS1?th=1'
         flipkart_url ='https://www.flipkart.com/redmi-note-11-pro-star-blue-128-gb/p/itme7022ee103b26'
         mobiles_url ='https://www.91mobiles.com/xiaomi-redmi-note-11-pro-price-in-india'
         headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
         redmi_11_1= Product(amazon_url,flipkart_url,mobiles_url,headers)
         redmi_11_1.myfunc()
        elif(specification==2):
          amazon_url = 'https://www.amazon.in/Redmi-Storage-Additional-Exchange-Included/dp/B09T2WRLJJ?th=1'
          flipkart_url ='https://www.flipkart.com/redmi-note-11-pro-phantom-white-128-gb/p/itme7022ee103b26?pid=MOBGCVHXV2UHHCDG&lid=LSTMOBGCVHXV2UHHCDGYULHRN&marketplace=FLIPKART&sattr[]=color&sattr[]=ram&st=ram'
          mobiles_url ='https://www.91mobiles.com/xiaomi-redmi-note-11-pro-8gb-ram-price-in-india'
          headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
          redmi_11_2 = Product(amazon_url,flipkart_url,mobiles_url,headers)
          redmi_11_2.myfunc()
        print("Variant Available \n")
        print("1. 6 GB/128 GB \n")
        print("2. 8 GB/ 128 GB \n")

        print("Enter 0 to Return Back \n")
        specification = int(input())

  elif(product == "REALME 9"):
     print("Variant Available \n")
     print("1. 6 GB/128 GB \n")
     print("2. 8 GB/128 GB \n")

     print("Enter 0 to Return Back \n")
     specification = int(input())
     while(specification!=0):
        if(specification==1):
         amazon_url = 'https://www.amazon.in/Realme-Sunrise-Blue-128GB-Storage/dp/B09SVGQJ23?th=1'
         flipkart_url ='https://www.flipkart.com/realme-9-pro-5g-aurora-green-128-gb/p/itm15e7a06fe9352?pid=MOBGB5Y3XVNYWNTH&lid=LSTMOBGB5Y3XVNYWNTHXKJXOD&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&sattr[]=ram&st=color'
         mobiles_url ='https://www.91mobiles.com/realme-9-pro-price-in-india'
         headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
         realme_1= Product(amazon_url,flipkart_url,mobiles_url,headers)
         realme_1.myfunc()
        elif(specification==2):
          amazon_url = 'https://www.amazon.in/Realme-Sunrise-Blue-128GB-Storage/dp/B09SVDDWL4?th=1'
          flipkart_url ='https://www.flipkart.com/realme-9-pro-5g-aurora-green-128-gb/p/itm15e7a06fe9352?pid=MOBGB5Y3RSYHBFJP&lid=LSTMOBGB5Y3RSYHBFJP9RYIE2&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&sattr[]=ram&st=ram'
          mobiles_url ='https://www.91mobiles.com/realme-9-pro-8gb-ram-price-in-india'
          headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
          realme_2 = Product(amazon_url,flipkart_url,mobiles_url,headers)
          realme_2.myfunc()
        print("Variant Available \n")
        print("1. 6 GB/128 GB \n")
        print("2. 8 GB/ 128 GB \n")
        print("Enter 0 to Return Back \n")
        specification = int(input())
  elif(product == "REALME NARZO"):
     print("Variant Available \n")
     print("1. 6 GB/128 GB \n")
     print("2. 8 GB/128 GB \n")

     print("Enter 0 to Return Back \n")
     specification = int(input())
     while(specification!=0):
        if(specification==1):
         amazon_url = 'https://www.amazon.in/realme-Racing-Storage-Additional-Exchange/dp/B0993YD3KJ?th=1'
         flipkart_url ='https://www.flipkart.com/realme-narzo-30-5g-racing-silver-128-gb/p/itm56837fcb0d6f3'
         mobiles_url ='https://www.91mobiles.com/realme-narzo-30-128gb-price-in-india'
         headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
         realme_narzo_1= Product(amazon_url,flipkart_url,mobiles_url,headers)
         realme_narzo_1.myfunc()
        elif(specification==2):
         amazon_url= 'https://www.amazon.in/realme-Racing-Storage-Additional-Exchange/dp/B0993YD3KJ?th=1'
         flipkart_url = 'https://www.flipkart.com/realme-narzo-30-racing-blue-128-gb/p/itm957dacbc8270c?pid=MOBG3W3GSPZ2S3DY&lid=LSTMOBG3W3GSPZ2S3DYGKRMAL&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&sattr[]=ram&st=storage'
         mobiles_url = 'https://www.91mobiles.com/realme-narzo-30-128gb-price-in-india'
         headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
         realme_narzo_2 = Product(amazon_url,flipkart_url,mobiles_url,headers)
         realme_narzo_2.myfunc()
        print("Variant Available \n")
        print("1. 6 GB/128 GB \n")
        print("2. 8 GB/ 128 GB \n")

        print("Enter 0 to Return Back \n")
        specification = int(input())
  elif(product=="SAMSUNG M53"):
     print("Variant Available \n")
     print("1. 6 GB/128 GB \n")
     print("2. 8 GB/128 GB \n")

     print("Enter 0 to Return Back \n")
     specification = int(input())
     while(specification!=0):
        if(specification==1):
         amazon_url = 'https://www.amazon.in/Samsung-Mystique-Storage-Purchased-Separately/dp/B09XJ5LD6L?th=1'
         flipkart_url ='https://www.flipkart.com/samsung-m53-5g-deep-ocean-blue-128-gb/p/itm8fb1195f06dd3'
         mobiles_url ='https://www.91mobiles.com/samsung-galaxy-m53-5g-price-in-india'
         headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
         Samsung_M53_1= Product(amazon_url,flipkart_url,mobiles_url,headers)
         Samsung_M53_1.myfunc()
        elif(specification==2):
         amazon_url= 'https://www.amazon.in/Samsung-Mystique-Storage-Purchased-Separately/dp/B0B146VNMY?th=1'
         flipkart_url = 'https://www.flipkart.com/samsung-m53-5g-emerald-brown-128-gb/p/itm3697f79186ecc?pid=MOBGFZKBXGAWZZY7&lid=LSTMOBGFZKBXGAWZZY7ISICLB&marketplace=FLIPKART&sattr[]=color&sattr[]=ram&st=color'
         mobiles_url = 'https://www.91mobiles.com/samsung-galaxy-m53-5g-8gb-ram-price-in-india'
         headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
         Samsung_M53_2 = Product(amazon_url,flipkart_url,mobiles_url,headers)
         Samsung_M53_2.myfunc()
        print("Variant Available \n")
        print("1. 6 GB/128 GB \n")
        print("2. 8 GB/ 128 GB \n")
        
        print("Enter 0 to Return Back \n")
        specification = int(input())

  elif(product=="POCO X3 PRO"):
     print("Variant Available \n")
     print("1. 6 GB/128 GB \n")
     print("2. 8 GB/128 GB \n")

     print("Enter 0 to Return Back \n")
     specification = int(input())
     while(specification!=0):
        if(specification==1):
         amazon_url = 'https://www.amazon.in/Poco-Steel-Blue-128GB-Storage/dp/B09DFQSSRG'
         flipkart_url ='https://www.flipkart.com/poco-x3-pro-steel-blue-128-gb/p/itm92bc566db15d8?pid=MOBGFKNFXBYGHFHJ&lid=LSTMOBGFKNFXBYGHFHJVIXT3U&marketplace=FLIPKART&sattr[]=color&sattr[]=ram&st=ram'
         mobiles_url ='https://www.91mobiles.com/poco-x3-pro-price-in-india'
         headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
         Poco_x3_1= Product(amazon_url,flipkart_url,mobiles_url,headers)
         Poco_x3_1.myfunc()
        elif(specification==2):
         amazon_url= 'https://www.amazon.in/Poco-Steel-Blue-128GB-Storage/dp/B09DFQ6GSK'
         flipkart_url = 'https://www.flipkart.com/poco-x3-pro-steel-blue-128-gb/p/itm527548fcdf883?pid=MOBGFKNF6HFYZWPY&lid=LSTMOBGFKNF6HFYZWPYH0RJAD&marketplace=FLIPKART&sattr[]=color&sattr[]=ram&st=ram'
         mobiles_url = 'https://www.91mobiles.com/poco-x3-pro-8gb-ram-price-in-india'
         headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
         Poco_x3__2 = Product(amazon_url,flipkart_url,mobiles_url,headers)
         Poco_x3__2.myfunc()
        print("Variant Available \n")
        print("1. 6 GB/128 GB \n")
        print("2. 8 GB/ 128 GB \n")
        
        print("Enter 0 to Return Back \n")
        specification = int(input())  
  
  

   
   

  print( )
  print("You have the Follwing Products \n")
  print("1. OPPO K10 \n")
  print("2. SAMSUNG A23 \n")
  print("3. REALME 9 \n")
  print("4. REALME NARZO  \n")
  print("5. SAMSUNG M53 \n")
  print("6. REDMI NOTE 11 \n")  
  print("7. POCO X3 PRO\n")
  print("Enter 0 For Exit \n")
  print( )
  print("Enter Product Name \n")
  product= (input())

  