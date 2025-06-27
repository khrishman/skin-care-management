# WeCare Beauty Products Management System

A simple terminal-based inventory and sales management system for a beauty product shop located in Manamaiju, Kathmandu. This application allows staff to view inventory, restock products, sell to customers, and generate invoices for purchases and sales. It includes a "Buy 3 Get 1 Free" promotional offer and maintains inventory in a plain text file.

## Features

- 📦 **Inventory Management**: Load products from `inventory.txt` or create a new file if not found.
- 🛒 **Restock Products**: Add more quantity to existing products and optionally update cost price.
- 💰 **Sell Products**: Process sales with customer details and "Buy 3 Get 1 Free" offer applied.
- 🧾 **Invoice Generation**: Creates timestamped text invoices for both restocks and sales.
- 📁 **Inventory Persistence**: Automatically updates `inventory.txt` after each operation.
- 📈 **Dynamic Pricing**: Selling price is calculated as 3x the cost price (200% markup).
- 🚚 **Shipping Option**: Optionally add ₹500 shipping cost to the sale invoice.

## Getting Started

### Requirements

- Python 3.x
- No external libraries required (uses built-in modules: `datetime`, `random`)

### Running the Program

Simply run the `main.py` file:

```bash
python main.py

<br>
Author - Khrishman Khadka
```
