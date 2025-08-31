# 📊 Customer Churn Prediction App  

This project is a **Machine Learning-powered Streamlit web app** that predicts whether a customer is likely to **churn (leave the service)** or **stay** based on their profile and subscription details.  

---

## 🚀 Project Overview  
Customer churn is a major challenge for subscription-based businesses. Retaining existing customers is often more cost-effective than acquiring new ones. This project uses **data mining, preprocessing, and predictive modeling** to build a churn prediction system.  

The app allows users to input customer details such as **Tenure, Age, Gender, Monthly Charges, Contract Type, and Tech Support availability**, and it predicts whether the customer will churn.  

---

## 🛠️ Tech Stack  
- **Python 3.12+**  
- **Libraries**:  
  - `scikit-learn` – Machine Learning model  
  - `joblib` – Model persistence  
  - `numpy` – Numerical computations  
  - `pandas` – Data preprocessing  
  - `streamlit` – Web application framework  

---

## 📂 Project Structure  
Customer_Churn_Prediction/
│── app.py # Streamlit app
│── model.pkl # Trained ML model
│── scaler.pkl # Feature scaler
│── customer_churn_data.csv # Dataset
│── README.md # Project documentation


---

## 📊 Dataset  

The dataset (`customer_churn_data.csv`) contains customer details such as:  

- **CustomerID** – Unique customer identifier  
- **Age** – Customer’s age  
- **Gender** – Male/Female  
- **Tenure** – Number of months customer has stayed  
- **MonthlyCharges** – Customer’s monthly subscription fee  
- **ContractType** – Type of contract (Month-to-Month, One-Year, Two-Year)  
- **TechSupport** – Availability of tech support (Yes/No)  
- **Churn** – Target variable (Yes = Churned, No = Not Churned)  

---

## 📈 Model Development  
1. **Data Preprocessing**  
   - Encoded categorical variables (`Gender`, `ContractType`, `TechSupport`).  
   - Standardized numerical features using a scaler.  

2. **Model Training**  
   - Multiple algorithms were tested.  
   - The **best model** was chosen and saved as `model.pkl`.  

3. **Deployment**  
   - Built a **Streamlit app** to allow real-time churn prediction.  

---

## ▶️ How to Run the App  

1. Clone the repository:
   ```bash
   git clone https://github.com/mlkinteh2/customer-churn-prediction.git
   cd Customer-Churn-prediction
2. pip install -r requirements.txt
3. streamlit run app.py
4. <img width="1587" height="823" alt="image" src="https://github.com/user-attachments/assets/332cb1ec-0199-4783-864c-d33bc7353c97" />


