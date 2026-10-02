# Fake Python Jobs Scraper

A beginner-friendly web scraping project built with Python. This project collects fake Python job listings from the Real Python Fake Jobs website and saves the extracted information into a CSV file.

## Project Overview

The scraper collects the following information from each job listing:

- Job Title
- Company Name
- Location
- Job Detail URL

The extracted data is stored in:

`jobs.csv`

## Features

- Fetches job listings from a website
- Finds all available job cards
- Extracts job title
- Extracts company name
- Extracts job location
- Extracts the job detail URL
- Handles missing fields using `N/A`
- Saves the results to a CSV file
- Includes basic error handling
- Uses a request timeout for safer execution

## Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV

## Python Libraries

```text
requests
beautifulsoup4