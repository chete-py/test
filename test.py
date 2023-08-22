import streamlit as st
import pandas as pd
import datetime

def evaluate_score(user_answers):
    correct_answers = {
    "Question 1": "Insurance Regulatory Authority",
    "Question 2": "Placement",
    "Question 3": "Know Your Customer (KYC)",
    "Question 4": "Banks, insurance companies, and lawyers",
    "Question 5": "To criminalize money laundering and provide mechanisms to combat it",
    "Question 6": "Layering",
    "Question 7": "Fine and imprisonment",
    "Question 8": "Politically Exposed Persons (PEPs)",
    "Question 9": "Financial Action Task Force (FATF)",
    "Question 10": "A customer making large cash deposits without a clear source of income",
    "Question 11": "To verify the identity of customers and assess the risks they pose",
    "Question 12": "Consistent with the customer's financial behavior",
    "Question 13": "Fine and imprisonment",
    "Question 14": "Overseeing and implementing AML policies and procedures",
    "Question 15": "Kenya Revenue Authority (KRA)"
    }

    user_score = 0
    for question, user_answer in user_answers.items():
        correct_answer = correct_answers[question]
        if user_answer == correct_answer:
            user_score += 1

    return user_score


def main():
    st.title("Corporate Insurance Anti-Money Laundering Assessment")
    user_name = st.text_input("Enter your name:")
    dep_name = st.text_input("Enter your department:")

    # QuestionS
    q1_choices = ["Insurance Regulatory Authority", "Kenya Revenue Authority", "Financial Reporting Centre (FRC)", "Central Bank of Kenya"]   
    q1_answer = st.radio("Question 1: Which agency in Kenya is responsible for regulating and enforcing AML laws?", q1_choices)

    q2_choices = ["Placement", "Expansion", "Integration ", " Layering "]   
    q2_answer = st.radio("Question 2: Which of the following is NOT a stage of money laundering? ", q2_choices)

    q3_choices = ["Know Your Business (KYB)", "Know Your Customer (KYC)", "Verify Your Customer (VYC) ", "Client Identity Verification (CIV) "]   
    q3_answer = st.radio("Question 3: Reporting entities in Kenya are required to identify and verify the identity of their customers. What is this process called?", q3_choices)

    q4_choices = ["Banks, insurance companies, and lawyers", " Schools and hospitals ", "Restaurants and retail stores", "Churches and charities"]   
    q4_answer = st.radio("Question 4: Which types of institutions are considered reporting entities under Kenyan AML laws? ", q4_choices)

    q5_choices = ["To encourage money laundering", "To provide guidelines for legalizing illicit funds ", "To criminalize money laundering and provide mechanisms to combat it", " To promote tax evasion"]   
    q5_answer = st.radio("Question 5: What is the primary purpose of the Proceeds of Crime and Anti-Money Laundering Act (POCAMLA) in Kenya?", q5_choices)

    q6_choices = ["Placement", "Layering", "Integration ", "Segmentation"]   
    q6_answer = st.radio("Question 6: Which phase of money laundering involves creating complex layers of financial transactions to obscure the origins of illegally obtained funds? ", q6_choices)

    q7_choices = ["Warning letter", "Fine and imprisonment", "Community service", "Tax deduction"]   
    q7_answer = st.radio("Question 7: What is the penalty for non-compliance with AML regulations in Kenya?", q7_choices)

    q8_choices = ["A salaried employee of a reputable company", " A retired government official", "An individual with a stable income and residence ", "Politically Exposed Persons (PEPs)"]   
    q8_answer = st.radio("Question 8: Which of the following is considered a high-risk customer under AML regulations?", q8_choices)

    q9_choices = ["International Monetary Fund (IMF)", "United Nations (UN) ", "Financial Action Task Force (FATF) ", "World Trade Organization (WTO)"]   
    q9_answer = st.radio("Question 9: What international body sets standards and promotes effective implementation of legal, regulatory, and operational measures to combat money laundering and terrorist financing? ", q9_choices)

    q10_choices = ["A customer making regular small deposits into their savings account", " A customer providing valid identification during account opening", "A customer making large cash deposits without a clear source of income", " A customer withdrawing money from their own account"]   
    q10_answer = st.radio("Question 10: Which of the following is an example of a red flag for potential money laundering?", q10_choices)

    q11_choices = ["To inconvenience customers ", "To prevent new customers from opening accounts", "To ensure customers have perfect credit scores", "To verify the identity of customers and assess the risks they pose "]   
    q11_answer = st.radio("Question 11: What is the objective of Customer Due Diligence (CDD) measures in AML compliance? ", q11_choices)

    q12_choices = ["Inconsistent with the customer's profile ", "Unusual or unexplained", "Consistent with the customer's financial behavior ", "Lacks an apparent economic purpose "]   
    q12_answer = st.radio("Question 12: Which of the following is NOT a characteristic of a suspicious transaction?", q12_choices)

    q13_choices = ['A pat on the back', 'A written warning', 'Fine and imprisonment', 'No penalty, it's encouraged']
    q13_answer = st.radio("Question 11: What is the penalty for tipping off, where someone discloses that a suspicious transaction has been reported? ", q13_choices)

    q14choices = ['Marketing the institution's services', 'Ensuring that the institution doesn't make a profit', 'Overseeing and implementing AML policies and procedures', 'Choosing the office's color scheme']   
    q14_answer = st.radio("Question 14: " What is the role of the AML Compliance Officer within a financial institution?”, q14_choices)
    
    q15_choices = ['Kenyan Police Department', 'Kenya Revenue Authority (KRA)', 'Insurance Regulatory Authority (IRA)', 'Central Bank of Kenya (CBK)']   
    q15_answer = st.radio("Question 15:  Which regulatory body in Kenya oversees and enforces AML regulations for insurance companies?", q15_choices)
      

    # Submit button
    if st.button("Submit"):
        answers = {
            "Question 1": q1_answer,
            "Question 2": q2_answer,
            "Question 3": q3_answer,
            "Question 4": q4_answer,
            "Question 5": q5_answer,
            "Question 6": q6_answer,
            "Question 7": q7_answer,
            "Question 8": q8_answer,
            "Question 9": q9_answer,
            "Question 10": q10_answer,
            "Question 11": q11_answer,
            "Question 12": q12_answer,
            "Question 13": q11_answer,
            "Question 14": q12_answer,
            "Question 15": q15_answer,
           }


        # Evaluate user score
        user_score = evaluate_score(answers)
    
        # Calculate user score as a percentage
        user_percentage = user_score / 12 * 100 
        
        # Display the user's score
        st.success(f"Answers submitted successfully! Your score: {user_percentage:.0f}%")

        
        # Create a DataFrame with user information
        user_info = pd.DataFrame({
            "Name": [user_name],
            "Department": [dep_name],
            "Score": [f"{user_percentage:.0f}%"],
            "Time": [datetime.datetime.now().strftime("%H:%M")]
        })
    
        # Save the DataFrame to a CSV file
        user_info.to_csv("user_score_report.csv", index=False)
            
        # Provide a download link for the user to download the report
        st.download_button(
            label="Download Score Report",
            data=user_info.to_csv(index=False).encode('utf-8'),
            file_name="user_score_report.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
