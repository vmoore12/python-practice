"""Python script that will get a list of products that are out of stock in the dev site."""

from woocommerce import API 
import os
import csv



woo_api = API(
    url=os.environ.get('url'),
    consumer_key=os.environ.get('consumer_key'),
    consumer_secret=os.environ.get('consumer_secret'),
    wp_api=os.environ.get('wp_api'),
    version=os.environ.get('version')



)


per_page = 100
current_page = 1
count = 0
skipped_items =[]
out_of_stock = []
in_stock = []
while True:
        payload = {
            "per_page": per_page,
            "page": current_page, #Note: this show the specific page you want to see now
        }

        all_products = woo_api.get('products', params=payload).json()
        if not all_products:
                break 
        for product in all_products:
            # #note: This goes through all the products and and ignore all the "collections" products/not simple in product type.
            # if product['type'] != 'simple':
            #     s_name = product['name'] +',' + product['type']
            #     skipped_items.append(s_name)
            #     continue
            
            if product['stock_status'] == 'outofstock':
                  ofs_name = product['name']
                  ofs_id = product['id']
                  ofs_status = product['stock_status']
                  out_of_stock.append({'id': product['id'], 'product_name': product['name'], 'stock status': product['stock_status']})
            else:
                  ins_name = product['name'] +',' + product['stock_status']
                  in_stock.append(ins_name)

        current_page += 1 



with open('ofs.csv', 'w', newline='') as f:
      writer = csv.writer(f)
      for i in out_of_stock:
            row = f'{i['id']}: {i['product_name']}'
            writer.writerow([row])
         


      

print(count)
print(skipped_items)
print(f'List of out of stock products:{out_of_stock}')
print(f'List of in stock products: {in_stock}')

