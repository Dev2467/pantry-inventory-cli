# Pantry Inventory CLI (Python)

A simple command-line pantry inventory app written in Python.

I built this as a learning project to practise Python fundamentals, file handling, and thinking like an IT / infrastructure engineer who builds small internal tools to solve everyday problems. The app helps track pantry items, see what’s running low, and export the data for shopping or review.

---

## Features

- **View inventory**  
  See all items currently stored in the pantry file.

- **Add items**  
  Add new items with:
  - name  
  - quantity  
  - unit (e.g. can, pack, jar, bag, etc.)  
  - minimum quantity before restocking (used for low-stock alerts)

- **Update item quantity**  
  Select an existing item by name and update its quantity.

- **Remove items**  
  Remove an item from the inventory by name.

- **View low-stock items**  
  Shows only items where:
  - a minimum quantity is set, and  
  - the current quantity is less than or equal to that minimum.

- **Export to CSV**  
  Exports the current inventory to `inventory.csv` so it can be opened in Excel, Google Sheets, or other tools.

---

## How It Works

The app stores data in a JSON file (`inventory.json`):

- Each pantry item is a Python dictionary with keys like:
  - `name`
  - `quantity`
  - `unit`
  - `min_quantity`
- All items are stored in a list, which is saved and loaded from the JSON file.
- On startup, the app:
  1. Loads `inventory.json` (or starts with an empty list if it doesn’t exist).
  2. Enters a menu loop where you choose actions by number.

The core logic is written as functions (for example: loading/saving inventory, printing items, finding an item by name), and the `main()` function acts as the entry point and menu controller.

---

## Running the App

Requirements:

- Python 3 installed

To run:

```bash
python3 pantry.py
