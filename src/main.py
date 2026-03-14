import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from scraper.crawler import run_crawler
from scraper.parsers import parse_all_products
from scraper.exporters import export_all
from scraper.utils import deduplicate


def main():
    print("\n" + "="*60)
    print("  ECOMMERCE SCRAPER PROJECT")
    print("  Target: webscraper.io/test-sites/e-commerce/static")
    print("="*60)

    product_links = run_crawler()

    if not product_links:
        print("\n[MAIN] No product links found. Exiting.")
        return

    products = parse_all_products(product_links)

    if not products:
        print("\n[MAIN] No products parsed. Exiting.")
        return

    print("\n" + "="*60)
    print("STEP 3: Deduplicating products")
    print("="*60)

    raw_count = len(products)
    subcategories = set(p["subcategory"] for p in products)
    duplicates_removed_map = {}

    for sub in subcategories:
        sub_products = [p for p in products if p["subcategory"] == sub]
        _, removed = deduplicate(sub_products)
        duplicates_removed_map[sub] = removed

    products, total_removed = deduplicate(products)
    print(f"[MAIN] Removed {total_removed} duplicates. {len(products)} unique products remain.")

    export_all(products, duplicates_removed_map)

    print("\n" + "="*60)
    print("  SCRAPING COMPLETE!")
    print(f"  Total products scraped : {raw_count}")
    print(f"  Duplicates removed     : {total_removed}")
    print(f"  Unique products saved  : {len(products)}")
    print("  Output files in        : data/")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()