# Ecommerce Scraper

This project was built as part of Quiz 1 for the Tools and Technologies for Data Science course. The task was to scrape product data from a static e-commerce website using Python and BeautifulSoup, while following proper Git branching practices.

## About the Project

I built a scraper that visits this website:
https://webscraper.io/test-sites/e-commerce/static

The scraper automatically finds the categories on the website, then goes deeper into subcategories, moves through multiple pages, and finally opens every single product page to collect detailed information. All the collected data is saved into CSV files at the end.

## What I Used

- Python as the programming language
- uv to set up and manage the whole project
- requests library to fetch web pages
- beautifulsoup4 to read and extract data from HTML
- pandas to organize and export data into CSV format
- Git and GitHub for version control and branch management

## Setting Up

I initialized and managed everything through uv:
```bash
uv init ecommerce-scraper
cd ecommerce-scraper
uv add requests beautifulsoup4 pandas
```

## Running the Project

First sync the dependencies:
```bash
uv sync
```

Then run the scraper:
```bash
uv run python src/main.py
```

To run tests:
```bash
uv run python tests/test_utils.py
```

## Git Branches I Used

I made sure not to work directly on main at any point. Here is the exact workflow I followed:

- Started with main branch
- Created dev from main for all development work
- Made feature/catalog-navigation branch to write the crawler that finds categories, subcategories and handles pagination
- Made feature/product-details branch to write the parser that visits each product page
- Merged both feature branches into dev
- Made fix/url-resolution branch to fix how relative links are converted to full URLs
- Made fix/deduplication branch to make sure no duplicate products end up in the final dataset
- Merged both fix branches into dev
- After everything was tested and working, merged dev into main

## What the Scraper Collected

- 147 total products
- 2 categories: Computers and Phones
- 3 subcategories: Laptops, Tablets and Touch
- 20 pages crawled for Laptops alone
- Zero duplicate records in the final output

## Output

- data/products.csv contains every product with its title, price, description, rating, review count, image link, specs and page number
- data/category_summary.csv contains a summary for each subcategory showing total products, average price, minimum and maximum prices, and missing description counts

## Assumptions

- Since the website does not use JavaScript to load content, requests and BeautifulSoup were sufficient without needing any browser automation tools
- I used the product page URL to identify and remove duplicate entries

## Limitations

- The scraper depends on the current HTML structure of the website so if the layout changes the code would need to be updated
- There is no request delay added since this is a practice site designed for scraping