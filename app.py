import streamlit as st
import requests
import json

# API Endpoint
API_URL = "https://kqq2tovrnd.execute-api.us-east-1.amazonaws.com/dev/predict" 

st.title("Customer Satisfaction Prediction App")

st.write("Fill in the details below to predict customer satisfaction:")

# Collect all inputs
inputs = {}

inputs["order_purchase_timestamp"] = st.text_input("Order Purchase Timestamp (YYYY-MM-DD HH:MM:SS)")
inputs["order_approved_at"] = st.text_input("Order Approved Timestamp (YYYY-MM-DD HH:MM:SS)")
inputs["order_delivered_carrier_date"] = st.text_input("Order Delivered Carrier Date (YYYY-MM-DD HH:MM:SS)")
inputs["order_delivered_customer_date"] = st.text_input("Order Delivered Customer Date (YYYY-MM-DD HH:MM:SS)")
inputs["order_estimated_delivery_date"] = st.text_input("Order Estimated Delivery Date (YYYY-MM-DD HH:MM:SS)")
inputs["shipping_limit_date"] = st.text_input("Shipping Limit Date (YYYY-MM-DD HH:MM:SS)")
inputs["review_answer_timestamp"] = st.text_input("Review Answer Timestamp (YYYY-MM-DD HH:MM:SS)")
inputs["review_creation_date"] = st.text_input("Review Creation Date (YYYY-MM-DD HH:MM:SS)")
inputs["review_comment_message"] = st.text_area("Review Comment Message")

inputs["price"] = st.number_input("Price", min_value=0.0)
inputs["freight_value"] = st.number_input("Freight Value", min_value=0.0)
inputs["product_description_length"] = st.number_input("Product Description Length", min_value=0.0)
inputs["product_weight_g"] = st.number_input("Product Weight (g)", min_value=0.0)
inputs["product_length_cm"] = st.number_input("Product Length (cm)", min_value=0.0)
inputs["product_height_cm"] = st.number_input("Product Height (cm)", min_value=0.0)
inputs["product_width_cm"] = st.number_input("Product Width (cm)", min_value=0.0)

inputs["seller_zip_code_prefix"] = st.number_input("Seller Zip Code Prefix", min_value=0)
inputs["customer_zip_code_prefix"] = st.number_input("Customer Zip Code Prefix", min_value=0)
inputs["customer_city"] = st.text_input("Customer City")
inputs["customer_order_frequency"] = st.number_input("Customer Order Frequency", min_value=0)
inputs["customer_avg_spend"] = st.number_input("Customer Average Spend", min_value=0.0)
inputs["repeat_purchase_flag"] = st.selectbox("Repeat Purchase Flag", [0, 1])
inputs["payment_value"] = st.number_input("Payment Value", min_value=0.0)

inputs["product_category_name"] = st.text_input("Product Category Name")
inputs["payment_type"] = st.selectbox("Payment Type", ["credit_card", "boleto", "voucher", "debit_card"])
inputs["seller_city"] = st.text_input("Seller City")
inputs["seller_state"] = st.text_input("Seller State")
inputs["customer_state"] = st.text_input("Customer State")
inputs["payment_installments"] = st.number_input("Payment Installments", min_value=1)
inputs["order_status"] = st.selectbox("Order Status", ["delivered", "shipped", "canceled", "invoiced", "processing"])

# Prediction button
if st.button("Predict"):
    try:
        response = requests.post(API_URL, json=inputs)
        
        if response.status_code == 200:
            result = response.json()
            prediction = result.get("prediction", None)

            if prediction == 0:
                st.success("✅ Prediction: Satisfied / Good")
            elif prediction == 1:
                st.warning("⚠️ Prediction: At-risk / Neutral")
            else:
                st.error(f"Unexpected response: {result}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"Request failed: {e}")
