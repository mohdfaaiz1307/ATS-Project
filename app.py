import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt1="""You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of all domains related to IT industry and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

## streamlit app
st.header("Resume Analyzer Pro")
st.subheader('Elevate Your Job Application with Intelligent Resume Insights')
st.subheader("Introduction ")
st.write("Welcome to Resume Analyzer Pro, your go-to solution for optimizing job applications! Our cutting-edge Application Tracking System (ATS) powered by Google Gemini Pro empowers you to maximize your resume's potential, ensuring it stands out in the competitive job market.")
st.write("**Start Elevating Your Job Applications Today!**")
st.write("Unleash the power of Resume Analyzer Pro and take control of your career trajectory. Upload your JD and resume now to receive personalized insights and increase your chances of landing your dream job.")
st.write("*Your Success Starts Here!*")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf")

submit = st.button("Submit")


if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt1)
        st.subheader(response)
    else:
        st.write("Please upload a PDF file to proceed.")

st.markdown("---")
st.caption("Resume Analyzer Pro - Elevate Your Job Application with Intelligent Resume Insights")
