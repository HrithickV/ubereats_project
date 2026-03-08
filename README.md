# 🍴 UberEats Bangalore: Restaurant & Order Analysis

### 📊 Project Overview
This project is a comprehensive data analysis of the UberEats ecosystem in Bangalore. Using a dataset of over 20,000 restaurants, I built an interactive Streamlit dashboard to uncover insights into market saturation, pricing strategies, and customer ordering patterns.

### 🚀 Key Insights
The dashboard is divided into two main categories:
* **Restaurant Analysis (10 Insights):** Explores top-rated locations like Lavelle Road, identifies over-saturated hubs like Koramangala, and analyzes the correlation between table bookings and ratings.
* **Order Analysis (5 Insights):** Identifies peak ordering days (Thursday/Monday), revenue leaders like Bob's Bar, and the "Salary Day Effect" on spending.

### 🛠️ Tech Stack
* **Language:** Python 3.9
* **Framework:** Streamlit
* **Visualization:** Plotly Express
* **Data Handling:** Pandas

### 📂 Project Structure
* `notebooks/app.py`: The main dashboard application code.
* `output/`: Contains the cleaned UberEats dataset.
* `requirements.txt`: List of Python dependencies for easy setup.

### 🏃 How to Run Locally
1. Clone the repository.
2. Activate your virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run notebooks/app.py`