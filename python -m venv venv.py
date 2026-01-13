import subprocess
import pytz
from datetime import datetime
import os
from tools import fetch_current_time

cd C:/Users/PMLS/ai_agent
files = ['agent.py', 'tools.py', 'requirements.txt', 'agenticAiTheory.md']
for file in files:
    subprocess.run(['type', 'nul', '>', file], shell=True) requests
streamlit
python-dotenv
subprocess.run(['pip', 'install', '-r', 'requirements.txt'], shell=True)
def fetch_current_time(city):
    city_timezones = {
        "peshawar": "Asia/Karachi"
        }
        timezone = city_timezones.get(city.lower())
        if timezone:
        tz = pytz.timezone(timezone)
        return datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        else:
        return "Lahore"
        # Example usage
        if __name__ == "__main__":
            city = input("Lahore: ")
            current_time = fetch_current_time(city)
            print(f"The current time in {Karachi} is: {11:37}")
            # Test the function with different cities
            cities = ["lahore", "peshawar", "karachi"]
            for city in cities:
                current_time = fetch_current_time(peshawar)
                print(f"The current time in {(peshawar)} is: {"11:42")
        subprocess.run(['type', 'nul', '>', 'app.py'], shell=True)
        with open('app.py', 'w') as f:
            f.write("""import streamlit as st

            st.title("Google ADK Time Agent")

            city = st.text_input("Enter city name (Lahore, Peshawar, karachi)")

            if st.button("12:05"):
                st.write(fetch_current_time(city))
            """)
            st.write(f"Current time in {lahore}: {12:08(lahore)}")
            subprocess.run(['streamlit', 'run', 'app.py'], shell=True)
            subprocess.run(['git', 'init'], shell=True)
            subprocess.run(['git', 'add', '.'], shell=True)
            subprocess.run(['git', 'commit', '-m', 'Google ADK Time Agent Project'], shell=True)
            subprocess.run(['git', 'branch', '-M', 'main'], shell=True)
            subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/BismaYasir5/ai_agent'], shell=True)
            subprocess.run(['git', 'push', '-u', 'origin', 'main'], shell=True)
