from sklearn.metrics import f1_score
from xgboost import XGBClassifier
import streamlit as st
import pandas as pd
from pickle import load
import joblib

filename = 'random.sav'
st.set_page_config(page_title="Customer Deposit Prediction",
                layout="wide")

#Loading up the model we created
model = joblib.load(filename)

def predict(age, duration, campaign, pdays, previous, emp_var_rate,
       cons_price_idx, cons_conf_idx, euribor3m, nr_employed):
    X_test = pd.DataFrame([[age, duration, campaign, pdays, previous, emp_var_rate,
       cons_price_idx, cons_conf_idx, euribor3m, nr_employed]], columns=['age', 'duration', 'campaign', 'pdays', 'previous', 'emp_var_rate',
       'cons_price_idx', 'cons_conf_idx', 'euribor3m', 'nr_employed'])
    prediction = model.predict(X_test)
    return prediction

st.title(":money_with_wings: Customer Deposit Prediction")
st.markdown("##")

# st.image("""https://data-fun.com/wp-content/uploads/2019/11/customer-churn-analytics-1024x662.jpg""", width=620)
st.header('Enter the characteristics of the customer:')

age = st.number_input('age:')
duration  = st.number_input('duration:')
campaign = st.number_input('campaign:')
marital = st.selectbox(
    'Marital?',
    ('married', 'single', 'divorced'))
pdays = st.number_input('pdays:')
outcome = st.selectbox(
    'Outcome?',
    ('nonexistent', 'failure', 'success'))
previous = st.number_input('previous:')
emp_var_rate = st.number_input('employee var rate:')
default = st.selectbox(
    'Default?',
    ('no', 'yes'))
cons_price_idx = st.number_input('consumer price index:')
housing = st.selectbox(
    'Housing?',
    ('no', 'yes'))
cons_conf_idx = st.number_input('consumer conf index:')
contact = st.selectbox(
    'Contact?',
    ('telephone', 'cellular'))
total_online_time = st.number_input('total online time:')
loan = st.selectbox(
    'Loan?',
    ('no', 'yes'))
euribor3m = st.number_input('euribor3m:')
nr_employed = st.number_input('nr employed:')
job = st.selectbox(
    'Job status?',
    ('housemaid', 'services', 'admin.', 'blue-collar', 'technician',
       'retired', 'management', 'unemployed', 'self-employed', 'unknown',
       'entrepreneur', 'student'))

education = st.selectbox(
    'Education?',
    ('basic.4y', 'high.school', 'basic.6y', 'basic.9y',
       'professional.course', 'university.degree',
       'illiterate'))


month = st.selectbox(
    'Month?',
    ('may', 'jun', 'jul', 'aug', 'oct', 'nov', 'dec', 'mar', 'apr',
       'sep'))

day = st.selectbox(
    'Day?',
    ('mon', 'tue', 'wed', 'thu', 'fri'))


def churn(value):
    if value == 1:
        return "Deposit"
    else:
        return "Not Deposit"

if st.button('Predict Price'):
    price = predict(age, duration, campaign, pdays, previous, emp_var_rate,
       cons_price_idx, cons_conf_idx, euribor3m, nr_employed)
    st.success(f'Predict customer is {churn(price[0])}')

