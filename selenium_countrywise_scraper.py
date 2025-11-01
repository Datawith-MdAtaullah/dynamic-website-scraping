from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import json
import os
from datetime import datetime


def process_each_country():
    start = time.time()

    # ---------- SETUP DRIVER ----------
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
    driver.get(website)

    # ---------- CLICK 'ALL MATCHES' ----------
    all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
    all_matches_button.click()
    time.sleep(3)

    # ---------- GET DROPDOWN OPTIONS ----------
    dropdown = Select(driver.find_element(By.XPATH, '//select[@id="country"]'))
    total_options = dropdown.options
    total = [opt.text for opt in total_options]

    success_countries = []
    failed_countries = []

    # ---------- LOOP THROUGH EACH COUNTRY ----------
    for country in total:
        try:
            dropdown = Select(driver.find_element(By.XPATH, '//select[@id="country"]'))
            dropdown.select_by_visible_text(country)
            time.sleep(3)

            table_content = driver.find_elements(By.XPATH, '//tr')
            print(f"{country}: {len(table_content)} rows")

            date, home_team, score, away_team = [], [], [], []

            for r in table_content:
                tds = r.find_elements(By.XPATH, './td')
                if len(tds) < 5:
                    continue

                date.append(tds[0].text.strip())
                home_team.append(tds[2].text.strip())
                score.append(tds[3].text.strip())
                away_team.append(tds[4].text.strip())

            data = {
                'Date': date,
                'HomeTeam': home_team,
                'Score': score,
                'AwayTeam': away_team
            }

            df = pd.DataFrame(data)

            folder_path = "Each_Country_Stats"
            os.makedirs(folder_path, exist_ok=True)
            file_path = os.path.join(folder_path, f"{country}_footballData.json")

            df.to_json(file_path, indent=4, orient='records', force_ascii=False)
            print(f"Saved data for {country} → {file_path}")

            success_countries.append(country)

        except Exception as e:
            print(f"Error processing {country}: {e}")
            failed_countries.append(country)

    
    success_count = len(success_countries)
    failed_count = len(failed_countries)

    if success_count == 0 and failed_count > 0:
        status = "failed"
    elif failed_count == 0:
        status = "completed"
    else:
        status = "partial"

    end = time.time()
    total_time = round(end - start, 2)

    start_time_str = datetime.fromtimestamp(start).strftime("%Y-%m-%d %H:%M:%S")
    end_time_str = datetime.fromtimestamp(end).strftime("%Y-%m-%d %H:%M:%S")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # ---------- LOG DATA ----------
    log_data = {
        "Each_Run_ID": timestamp,
        "start_time": start_time_str,
        "end_time": end_time_str,
        "total_duration_seconds": total_time,
        "success_count": success_count,
        "failed_count": failed_count,
        "success_fetched": success_countries,
        "failed_fetched": failed_countries,
        "status": status
    }

    folder_path = "eachRun_Logs"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"log_{timestamp}.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)

    
    print("SCRAPING COMPLETE")
    print(f"Total countries saved: {success_count}/{len(total)}")
    print(f"⏱️ Duration: {total_time} seconds")
    print(f"🗂️ Log saved: {file_path}")

    driver.quit()
    return success_count


if __name__ == "__main__":
    run = process_each_country()
