# Dynamic Web Scraping using Selenium 🚀

This project demonstrates how to perform **dynamic web scraping** using **Selenium** on a website that loads its data dynamically through **AJAX requests**.

## 🌐 Website

Data Source: [adamchoi.co.uk - Football Match Statistics](https://www.adamchoi.co.uk/teamgoals/detailed)

## ⚙️ Technologies Used

- Python 🐍
- Selenium WebDriver
- Pandas
- Jupyter Notebook

## 📋 Features

- Automates browser interactions using Selenium.
- Selects dropdowns dynamically (e.g., filtering matches by country).
- Handles AJAX-loaded content.
- Extracts data from HTML tables into structured formats.
- Exports data as:
  - CSV (`Football_Data.csv`)
  - JSON (`Football_Data.json`, `Football_Spain.json`)

## 📁 Files

| File | Description |
|------|--------------|
| `Selenium_scraping.ipynb` | Main scraping notebook |
| `Football_Data.json` | All matches data |
| `Football_Spain.json` | Spain-filtered data |
| `Football_Data.csv` | Matches in CSV format |

## 🧠 Learning Highlights

- Difference between static and dynamic websites.
- Using Selenium’s `Select()` for dropdowns.
- Waiting for AJAX content to load (`time.sleep()`).
- Data parsing and cleaning using Pandas.

## 📦 How to Run
```bash
pip install selenium pandas
```

## 🏁 Output Example (JSON)
```
[
  {
    "Date": "26-10-2025",
    "HomeTeam": "Arsenal",
    "Score": "1 - 0",
    "AwayTeam": "Crystal Palace"
  },
  {
    "Date": "18-10-2025",
    "HomeTeam": "Fulham",
    "Score": "0 - 1",
    "AwayTeam": "Arsenal"
  }
]
```