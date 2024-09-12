# Daily Web Scraper

This repository contains a Python script that scrapes content from a specified website daily at 16:00 UTC using GitHub Actions.

## How it works

1. The `scraper.py` script fetches content from the specified URL.
2. The content is saved in a text file within the `scraped_content` directory, with the current date as the filename.
3. GitHub Actions runs this script daily at 16:00 UTC.
4. If there are changes, the new content is committed and pushed to the repository.

## Configuration

To change the target website, edit the `url` variable in `scraper.py`.

To modify the scraping schedule, edit the `cron` expression in `.github/workflows/daily_scrape.yml`.

## Directory Structure

- `scraped_content/`: Contains all the scraped content files.
- `scraper.py`: The main Python script for web scraping.
- `.github/workflows/daily_scrape.yml`: GitHub Actions workflow file.
