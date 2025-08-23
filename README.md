# 🛒 E-Commerce Customer Satisfaction Predictor

This project predicts **customer satisfaction** based on the **Brazilian E-Commerce Public Dataset** available on Kaggle. The model classifies customers as **Good, Neutral, or Bad** based on their order review scores.

📊 **Dataset:** [Brazilian E-Commerce Public Dataset by Olist (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

---

## 🚀 Project Overview

* Built a **machine learning model** to classify customer satisfaction levels.
* Trained on Kaggle’s **Brazilian E-Commerce dataset** (Olist).
* Deployed the trained model as a **serverless application** on **AWS Lambda**.
* Integrated with **AWS API Gateway** to provide a working REST endpoint.
* A **Streamlit app** was developed as a user-friendly interface to interact with the model.

---

## 💼 Business Use Case

Customer churn is a major challenge in e-commerce.
This model enables:

* **Retention strategies**: Identifying potentially dissatisfied customers early.
* **Targeted efforts**: Engaging with "neutral" and "bad" customers to reduce churn rate.
* **Resource allocation**: Prioritizing marketing and customer service efforts effectively.

---

## 🌐 Deployment Details

* **Model Backend**: Deployed on **AWS Lambda** with an API Gateway endpoint.
* **Frontend App**: Developed using **Streamlit**, accessible at:
  👉 [Customer Satisfaction Predictor App](https://e-commerce-project-nfjva46rtankjnrlt5kkia.streamlit.app)

---

## 🛠️ Tech Stack

* **Python**
* **XGBoost / Scikit-learn**
* **Pandas / NumPy**
* **AWS Lambda**
* **AWS API Gateway**
* **Streamlit**

---

## 📂 Project Structure

```
├── app.py              # Streamlit frontend
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
├── data.ipynb          # Model building file
```

---

Perfect 👍 Thanks for sharing the model performance details and confusion matrix. Here’s the **updated README.md** with everything included:

---


## 🤖 Model Deployment

* **AWS Lambda** used for serverless deployment.
* **API Gateway** provides a working endpoint for integration.
* **Streamlit frontend** interacts with the deployed model API.

---

## 📊 Model Performance

### Classification Report

```
================ CLASSIFICATION REPORT ================
              precision    recall  f1-score       support
0              0.851809  0.909601  0.879757  26560.000000
1              0.380457  0.262931  0.310960   4176.000000
2              0.683824  0.605251  0.642143   4456.000000
accuracy       0.794328  0.794328  0.794328      0.794328
macro avg      0.638697  0.592594  0.610953  35192.000000
weighted avg   0.774606  0.794328  0.782175  35192.000000
```

### Confusion Matrix

![Confusion Matrix](40f84443-6f74-4b78-8664-099a107592a4.png)

---

✅ Overall accuracy: **\~79%**
✅ Good performance for "satisfied customers (0)"
✅ Room for improvement in detecting "neutral" customers (class 1).

---

Would you like me to also add a **section with tech stack and tools used (Python, Sklearn, AWS, Streamlit, Pandas, etc.)** to make the README look more professional for GitHub?


## 🔮 Future Improvements

* Enhance feature engineering for better prediction accuracy.
* Improve UI/UX of the Streamlit app.
* Deploy dataset insights on an interactive **Power BI / Tableau dashboard**.

---

✨ Built with passion for **ML + Cloud + Analytics**.

---

Do you also want me to add an example **cURL / Postman request body** section in the README so others can test your AWS endpoint easily?
