# 📧 Cold Email Generator
Input the URL of a job offer from that page and generate a personalized cold emails, including relevant portfolio links sourced from a vector database.

## Architecture Diagram
![img.png](img/architecture.png)

## Set-up
1. Get an API_KEY from here: https://console.groq.com/keys. Inside `app/.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 

2. To get started, first install the dependencies using:
    ```commandline
     pip install -r requirements.txt
    ```
   
3. Run the streamlit app:
   ```commandline
   streamlit run app/main.py
   ```
