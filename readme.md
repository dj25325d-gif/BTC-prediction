# 📈 BTC Prediction & Trend Tracker (Python CLI)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Library-Pandas-yellow)
![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-blue)
![Seaborn](https://img.shields.io/badge/Visualization-Seaborn-teal)
![Status](https://img.shields.io/badge/Status-Completed-success)

> **Pro Tip for your GitHub:** Record a 10-second GIF of you navigating the main menu using a free tool like *ScreenToGif* or *Terminalizer*, and replace this quote block with `![CLI Demo](screenshots/demo.gif)`!

---

# 📌 Project Overview

This project is a **Bitcoin Prediction & Trend Tracker** built entirely in Python. Designed as a comprehensive capstone project, it demonstrates a complete Object-Oriented Programming (OOP) workflow combined with a custom-built Python package.

It simulates a real-world **financial data analyst workflow**, allowing users to dynamically load cryptocurrency datasets, perform statistical transformations, predict short-term market trends using historical moving averages, and generate visual reports. 

---

# ⚙️ Key Features & Skills Demonstrated

| Feature | Description | Skills Highlighted |
| :--- | :--- | :--- |
| **📦 Custom Python Package** | Abstracted logic into custom `dfmath`, `displaydata`, and `charts` modules. | Modular Design, DRY Principles, Abstraction |
| **🔄 Interactive CLI Menu** | Loop-based menu utilizing Python 3.10+ `match...case` and safe input validation. | Error Handling (`try/except`), UX Design |
| **🧮 Statistical Engine** | Calculates moving averages, standard deviations, and trading volume distributions. | NumPy, Statistical Analysis |
| **📊 Real-Time Appending** | Users can log new daily market data that instantly updates the DataFrame in memory. | Pandas, File Handling (Append Mode) |
| **🤖 Trend Prediction** | Algorithmic comparison of current prices vs. historical averages to generate Buy/Sell signals. | Algorithmic Logic, Persistent Logging |

---

# 📊 Generated Charts

## 📈 Historical Price Trends
![Line Chart](charts/line_chart.png)

## 📉 Trading Volume vs. Closing Price
![Scatter Chart](charts/scatter_chart.png)

---

# 🎬 Application Walkthrough

## 🏠 1. Interactive Main Menu
The application is driven by a clean command-line interface with robust error handling to prevent crashes from invalid user keystrokes.
![Main Menu](screenshots/mainmenu.png)

## 🔍 2. Data Loading & Exploration
Dynamically loads the CSV file, cleans the headers, and sets up datetime indexing for time-series analysis.
![Data Exploration](screenshots/sc1.png)

## 📉 3. Statistical Summary
Leverages the custom `dfmath` module to crunch the dataset and format peak highs, lowest dips, averages, and standard deviations.
![Statistical Summary](screenshots/sc2.png)
*(Further exploration metrics shown in [screenshots/sc3.png](screenshots/sc3.png))*

## 🗂️ 4. Data Filtering & Appending Live Data
Filters trading days based on user-defined minimum closing price thresholds. Users can seamlessly append fresh daily data to the CSV and reload the DataFrame.
**Filtering Data:**
![Data Filtering](screenshots/sc4.png)
**Appending Data:**
![Appending Data](screenshots/sc5.png)

## 🔮 5. Trend Prediction Engine
Evaluates current prices against historical moving averages to generate actionable insights. Every prediction is timestamped and saved to a persistent text log (`Prediction_Report.txt`).
![Prediction Engine](screenshots/sc6.png)

## 🚪 6. Safe Exit
Gracefully terminates the program and closes all running loops.
![Exit Program](screenshots/exit.png)

---

# ▶️ How to Run the Project Locally

```bash
# 1. Clone the repository
git clone <your-repo-link>
cd BTC_Trend_Tracker

# 2. Install required dependencies
pip install pandas matplotlib seaborn

# 3. Run the application
python main.py

(When prompted in the main menu, type btc5Year_Data.csv to load the dataset and begin your analysis.)

📁 Architecture & File Structure
Plaintext
/BTC_Trend_Tracker
│── main.py                  # Core application loop and OOP logic
│── btc5Year_Data.csv        # Primary historical dataset
│── Prediction_Report.txt    # Auto-generated log of past trend predictions
│
├── /screenshots             # UI documentation and demo images
├── /charts                  # Saved Matplotlib/Seaborn visualization outputs
│
└── /package                 # Custom user-defined module directory
    │── __init__.py          # Package initializer
    │── dfmath.py            # Abstracted mathematical operations
    │── displaydata.py       # Pandas DataFrame inspection logic
    └── charts.py            # Seaborn/Matplotlib rendering functions
💼 Portfolio Value
This project was built to demonstrate a complete data analysis pipeline and software engineering lifecycle. It showcases the ability to move beyond basic linear scripts into building modular, interactive, and user-friendly data applications.

This repository highlights core competencies relevant for Data Analyst, Entry-Level Data Scientist, and Python Developer roles.

🔮 Future Improvements
🌐 Web Integration: Transition the CLI into a Streamlit web dashboard.

🧠 Machine Learning: Implement Scikit-Learn Linear Regression for advanced predictive modeling.

🔌 Live API Integration: Connect to Binance or CoinGecko APIs to automatically fetch daily market data instead of manual entry.

📜 License
This project is open-source and available under the MIT License. Feel free to use and modify it for your own learning!