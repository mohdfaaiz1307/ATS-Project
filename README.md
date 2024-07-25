Resume Analyser Pro

Resume Analyser Pro is a Python-based application designed to help job seekers enhance their resumes. By comparing uploaded resumes against job descriptions (JDs), the application provides insights on keyword matches, missing keywords, and general recommendations. The tool utilizes the Google Gemini Pro LLM model API for accurate and efficient analysis.
Features:

   - Resume and Job Description Upload: Users can upload their resume and the relevant job description.
   - Percentage Match: Calculates and displays the percentage match between the resume and the job description.
   - Keyword Analysis: Identifies missing keywords from the resume that are present in the job description.
   - Final Thoughts: Provides additional recommendations based on the analysis.

Libraries and Technologies: 

   - Streamlit: For building the web application interface.
   - google-generativeai: To interact with the Google Gemini Pro LLM model API for analysis.
   - python-dotenv: To manage environment variables.
   - PyPDF2: To handle PDF files.
   - os: For interacting with the operating system.
   - json: For parsing JSON data.

Setup and Installation: 

  1. Clone the repository:

git clone https://github.com/yourusername/resume-analyser-pro.git
cd resume-analyser-pro

2. Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install the required packages:

pip install -r requirements.txt

4. Set up environment variables:
Create a .env file in the root directory and add the following line:

GOOGLE_API_KEY=your_google_api_key_here

5. Run the application:

    streamlit run app.py

Usage: 

  1. Open your browser and navigate to http://localhost:8501 to access the application.
  2. Upload your resume and the job description file.
  3. View the percentage match, missing keywords, and final thoughts on the results page.

Example

Here’s a sample screenshot of the application interface: 
