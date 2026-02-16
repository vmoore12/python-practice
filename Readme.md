# WooCommerce API Python Practice

This repository is compiled of several automation scripts to refresh and improve basic skills learned in backend automation testing.

## Requirements

1. Python 3.6+
2. WooCommerce 3.0+
3. WooCommerce API Keys (Consumer Key and Consumer Secret) with appropriate permissions.

## Environment Variables

All scripts require the following environment variables to be set to interact with your WooCommerce store:

* `url`: Your store URL (e.g., `http://example.com/`)
* `consumer_key`: Your WooCommerce API Consumer Key
* `consumer_secret`: Your WooCommerce API Consumer Secret
* `wp_api`: Set to `True` if using the WordPress REST API (usually `True`)
* `version`: WooCommerce API version (e.g., `wc/v3`)

## Install dependencies

* try `pip3` if below doesn't work 

```bash
pip install -r requirements.txt
```

## Available Scripts

### 1. Missing Prices Finder
* **Path:** `dev_missing_price/dev_missing_price.py`
* **Purpose:** Scans all products to find those missing a regular price.
* **Output:** Generates `missing_price.csv`.

### 2. Out of Stock Reporter
* **Path:** `dev_out_of_stock/dev_out_of_stock.py`
* **Purpose:** Identifies all products that are currently out of stock.
* **Output:** Generates `ofs.csv`.

### 3. Random Out of Stock Product Creator
* **Path:** `dev_random_created_ofs/dev_created_ofs_products.py`
* **Purpose:** Generates a specified number of dummy out-of-stock products for testing purposes.
* **Usage:** `python3 dev_created_ofs_products.py <quantity>`

### 4. 10% Price Update Calculator
* **Path:** `dev_update_prices/update_prices_10p.py`
* **Purpose:** Calculates a 10% price increase for all products.
* **Output:** Generates `up10.csv` with old and new price comparisons.

## Usage
To run any of the automation scripts, navigate to the appropriate directory and execute the script:
```bash
cd dev_random_created_ofs
python3 dev_created_ofs_products.py 5
```







  
