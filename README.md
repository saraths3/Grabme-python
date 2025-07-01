# Grab Me

**Grab Me** is a Python Django-based web application that performs real-time **price comparison** of products across multiple online shopping websites using web scraping. It helps users identify the best available deals by fetching, comparing, and filtering prices of similar or identical products.

---

## Features

| Feature                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Product Search             | Search products by name or keyword.                                         |
| Real-Time Scraping         | Fetches live data from supported e-commerce sites.                          |
| Price Comparison           | Compares prices of the same or similar products.                            |
| Smart Filtering            | Filter results by price, brand, relevance, or availability.                 |
| Product Detail View        | Shows full product details, specs, and redirect links to original websites. |
| Responsive UI              | Clean design, mobile-friendly layout.                                       |

---

## Tech Stack

| Component       | Technology             |
|----------------|------------------------|
| Language        | Python                 |
| Framework       | Django                 |
| Scraping        | BeautifulSoup, Requests or Scrapy |
| Frontend        | HTML, CSS, Bootstrap   |
| Database        | SQLite (or PostgreSQL) |
| Hosting         | Localhost / WSGI-ready |

---

## Project Structure

| Folder / File         | Purpose                                     |
|-----------------------|---------------------------------------------|
| `/grabme/`            | Django project files                        |
| `/products/`          | Django app for product models & views       |
| `/templates/`         | HTML templates                              |
| `/static/`            | CSS, JavaScript, and static assets          |
| `scraper/`            | Web scraping logic and data parsing         |
| `manage.py`           | Django CLI management script                |
| `requirements.txt`    | Python dependencies                         |

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone git@github.com:saraths3/Grabme-python.git
   cd Grabme-python
