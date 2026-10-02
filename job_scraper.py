import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://realpython.github.io/fake-jobs/"

# Get the webpage
response = requests.get(url, timeout=10)
response.raise_for_status()

print(response.status_code)

# Read the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all job cards
job_cards = soup.find_all("div", class_="card-content")

print("Number of job cards:", len(job_cards))

# Store all jobs
jobs = []

# Process each job
for job in job_cards:

    # Get job title
    title_tag = job.find("h2", class_="title")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    # Get company name
    company_tag = job.find("h3", class_="company")
    company = company_tag.get_text(strip=True) if company_tag else "N/A"

    # Get location
    location_tag = job.find("p", class_="location")
    location = location_tag.get_text(strip=True) if location_tag else "N/A"

    # Get job detail URL
    links = job.find_all("a", class_="card-footer-item")
    job_link = links[1]["href"] if len(links) > 1 else "N/A"

    # Store the job information
    job_data = {
        "Job Title": title,
        "Company": company,
        "Location": location,
        "Job URL": job_link
    }

    jobs.append(job_data)

# Save jobs to CSV
with open("jobs.csv", "w", newline="", encoding="utf-8") as file:

    fieldnames = ["Job Title", "Company", "Location", "Job URL"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(jobs)


print("Jobs saved to jobs.csv")
print("Total jobs saved:", len(jobs))