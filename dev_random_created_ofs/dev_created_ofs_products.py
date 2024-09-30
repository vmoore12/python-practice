""""
Project ID: 605

** Challenge **
Create a script that will generate a given number of products that are out of stock.

** Use Case **
There is a previous project (project id = 601) that is to list all products that are out of stock. 
But the site might not have any products that are out of stock. So in that case we need to prepare data for the
project. This script can be run to create out of stock products (data) to be used in project 601.


** Details **

You are tasked with creating a script that generates a specified number of out-of-stock products in a WooCommerce store. 
The script should use the woocommerce library to interact with the WooCommerce API and create products with random names. 
The number of products to be created should be provided as a command line argument.

Requirements:

1. WooCommerce API Setup:
   - Ensure you have the woocommerce library installed. You can install it using [`pip install woocommerce`].
   - Replace url, consumer_key, and consumer_secret with your WooCommerce store's details.

2. Script Functionality:
   - The script should generate random product names.
   - Each product should be created with the following attributes:
     - `name`: Randomly generated name.
     - `type`: "simple".
     - `regular_price`: <generate random price>.
     - `description`: Empty string.
     - `short_description`: Empty string.
     - `stock_quantity`: 0.
     - `manage_stock`: True.
   - The script should accept the number of products to be created as a command line argument.
   - The script should print the name and ID of each created product.

Prerequisits:
    * API Key/Secret with "Write" access. (You must use site you created on your local since 'write' api can not be provided to the public site)
   
   
** Example Usage **

Save the script as `create_out_of_stock_products.py` and run it from the terminal:

$ python create_out_of_stock_products.py 10

This command will create 10 out-of-stock products in your WooCommerce store.

"""

from woocommerce import API
import random
import string
import argparse
import os

## Command Line Argument using ARGPARSE:
parser = argparse.ArgumentParser(description='Create out of stock products')
parser.add_argument('quantity', metavar='quantity', type=int, help='Number of out-of-stock products to create')
args = parser.parse_args()
#-----------------------------------------------------------------------

num_of_products = args.quantity

woo_api = API(
    url=os.environ.get('url'),
    consumer_key=os.environ.get('consumer_key'),
    consumer_secret=os.environ.get('consumer_secret'),
    wp_api=os.environ.get('wp_api'),
    version=os.environ.get('version')

)

def random_name():
    letters = string.ascii_letters ## contains uppercase and lowercase letters
    random_string = ''.join(random.choice(letters)for i in range(8))
    return random_string


def create_products(num_of_products):
    product_slug= random_name()
    price = round((random.uniform(10.00,60.00)), 2)

    payload = {
        'name': product_slug,
        'type': 'simple',
        'regular_price': str(price),
        'description': '',
        'short_description': '',
        'stock_quantity': '0',
        'manage_stock': 'True'

    }
    for i in range(num_of_products):
        new_products = woo_api.post('products',data=payload).json()

    return new_products

create_products(num_of_products)

# #*  Delete created products.

# def deleted_unwanted_products():
#     per_page = 100
#     current_page = 1
#     count = 0
#     no_images = 0
#     with_images = 0

#     try:
#         # Get the total number of products to calculate the total pages
#         # total_products = woo_api.get('products', params={"per_page": 1}).json()

#         while True:
#             payload = {
#                 "per_page": per_page,
#                 "page": current_page,
#             }

#             all_products = woo_api.get('products', params=payload).json()

#             if not all_products:
#                 break

#             for product in all_products:
#                 count += 1
#                 # Delete products with no images
#                 if not product['images']:
#                     product_id = product['id']
#                     no_images += 1
#                     woo_api.delete(f'products/{product_id}', params={"force": True}).json()

#                 # Get remaining products
#                 elif product['images']:
#                     with_images += 1

#             current_page += 1

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     print(f"Total products = {count}.\n"
#           f'Total products deleted = {no_images}.\n'
#           f'Total products remaining = {with_images}.')

# deleted_unwanted_products()