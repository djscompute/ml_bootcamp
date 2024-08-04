import streamlit as st
import pandas as pd
import joblib

# Load your trained model using joblib
try:
    model = joblib.load('xgboost_model.pkl')
    st.write("Model loaded successfully!")
except Exception as e:
    st.write(f"Error loading model: {e}")
    st.stop()

# Define risk category mapping
risk_mapping = {
    2: 'High Risk',
    1: 'Moderate Risk',
    0: 'Low Risk'
}

# Define the Streamlit app
def main():
    st.title('Risk Category Prediction')

    # Create inputs for numerical and float columns
    loan_amount = st.number_input('Loan Amount', min_value=0, value=1000)
    interest_rate = st.number_input('Interest Rate (%)', min_value=0.0, value=5.0)
    installment = st.number_input('Installment', min_value=0, value=100)
    terms_months = st.selectbox('Terms (Months)', [36, 60])  # Changed to selectbox
    employment_length = st.number_input('Employment Length (Years)', min_value=0, value=5)
    debt_to_income_ratio = st.number_input('Debt to Income Ratio', min_value=0.0, value=0.3)

    # Create inputs for categorical columns
    verification_status = st.selectbox('Verification Status', ['Not Verified', 'Verified'])
    grade = st.selectbox('Grade', ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    home_ownership = st.selectbox('Home Ownership', ['MORTGAGE', 'OTHER', 'OWN', 'RENT'])

    # One-hot encoding for the 'Purpose' column
    purposes = ['car', 'credit_card', 'small_business', 'other', 'wedding', 'debt_consolidation', 
                'home_improvement', 'major_purchase', 'medical', 'moving', 'vacation', 'house', 
                'renewable_energy', 'educational']
    purpose = st.selectbox('Purpose', purposes)

    # Initialize one-hot encoded features with zeros
    one_hot_encoded_purposes = [0] * len(purposes)
    purpose_index = purposes.index(purpose)
    one_hot_encoded_purposes[purpose_index] = 1

    # Create a DataFrame with user inputs and include all columns
    data = pd.DataFrame({
        'Loan_Amount': [loan_amount],
        'Interest_Rate': [interest_rate],
        'Installment': [installment],
        'Terms(Months)': [terms_months],
        'Employment_Length': [employment_length],
        'Home_Ownership': [{'MORTGAGE': 0, 'OTHER': 1, 'OWN': 2, 'RENT': 3}[home_ownership]],
        'Debt_to_Income_Ratio': [debt_to_income_ratio],
        'Verification_Status': [1 if verification_status == 'Verified' else 0],
        'Grade': [{'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}[grade]],
        'Purpose_car': [one_hot_encoded_purposes[0]],
        'Purpose_credit_card': [one_hot_encoded_purposes[1]],
        'Purpose_debt_consolidation': [one_hot_encoded_purposes[2]],
        'Purpose_educational': [one_hot_encoded_purposes[3]],
        'Purpose_home_improvement': [one_hot_encoded_purposes[4]],
        'Purpose_house': [one_hot_encoded_purposes[5]],
        'Purpose_major_purchase': [one_hot_encoded_purposes[6]],
        'Purpose_medical': [one_hot_encoded_purposes[7]],
        'Purpose_moving': [one_hot_encoded_purposes[8]],
        'Purpose_other': [one_hot_encoded_purposes[9]],
        'Purpose_renewable_energy': [one_hot_encoded_purposes[10]],
        'Purpose_small_business': [one_hot_encoded_purposes[11]],
        'Purpose_vacation': [one_hot_encoded_purposes[12]],
        'Purpose_wedding': [one_hot_encoded_purposes[13]]
    })

    # Debug: Display DataFrame
    st.write("Input Data for Prediction:")
    st.write(data)

    # Create a button to trigger prediction
    if st.button('Predict'):
        try:
            # Make prediction
            prediction = model.predict(data)
            risk_category = risk_mapping.get(prediction[0], 'Unknown Risk Category')
            st.write(f'Predicted Risk Category: {risk_category}')
        except Exception as e:
            st.write(f"Error during prediction: {e}")

if __name__ == '__main__':
    main()
