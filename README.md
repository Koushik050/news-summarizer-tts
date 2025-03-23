# news-summarizer-ttsHere’s a **README.md** file for your project:  

---

### **News Summarization & Text-to-Speech Application**  

#### **Overview**  
This web-based application extracts news articles related to a company, performs **summarization and sentiment analysis**, and converts the final summary into **Hindi speech**.  

#### **Features**  
✅ Extracts **latest news** using NewsAPI  
✅ Summarizes article content using NLP  
✅ Performs **sentiment analysis** (Positive, Negative, Neutral)  
✅ Generates **comparative sentiment analysis** across multiple news articles  
✅ Converts the summary into **Hindi speech** using `gTTS`  
✅ Provides a **Streamlit-based web UI**  
✅ Deployable on **Hugging Face Spaces**  

---

### **Installation**  
1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/news-summarizer-tts.git
   cd news-summarizer-tts
   ```
2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
3. **Get a NewsAPI key**  
   - Sign up at [NewsAPI](https://newsapi.org/)  
   - Replace `"YOUR_NEWS_API_KEY"` in `utils.py`  

4. **Run the application**  
   ```bash
   streamlit run app.py
   ```

---

### **Project Structure**  
```
📂 news-summarizer-tts
│── app.py            # Main Streamlit application
│── utils.py          # Web scraping, summarization, sentiment analysis
│── tts.py            # Text-to-Speech module (Hindi)
│── requirements.txt  # Dependencies list
│── README.md         # Documentation
```

---

### **Usage**  
1. **Enter a company name** (e.g., `Tesla`) in the UI.  
2. Click **"Fetch News"** to retrieve articles.  
3. View **article summaries and sentiment analysis**.  
4. Listen to **Hindi speech output**.  

---

### **Deployment on Hugging Face Spaces**  
1. **Create a new Space** at [Hugging Face Spaces](https://huggingface.co/spaces).  
2. Choose **"Streamlit"** as the framework.  
3. **Upload files or connect GitHub**.  
4. Restart the Space and access the **deployed app link**.

---

### **Example Output**  
**Input:** `Company Name: Tesla`  
**Output (Sentiment Analysis Report)**  
```json
{
  "Company": "Tesla",
  "Articles": [
    {
      "Title": "Tesla's New Model Breaks Sales Records",
      "Summary": "Tesla's latest EV sees record sales in Q3...",
      "Sentiment": "Positive"
    },
    {
      "Title": "Regulatory Scrutiny on Tesla's Self-Driving Tech",
      "Summary": "Regulators have raised concerns over Tesla’s self-driving software...",
      "Sentiment": "Negative"
    }
  ],
  "Final Sentiment Analysis": "Tesla’s latest news coverage is mostly positive.",
  "Audio": "[Play Hindi Speech]"
}
```

---

### **Future Enhancements**  
🔹 Add **language selection** for speech output  
🔹 Implement **more advanced NLP models** for summarization  
🔹 Include **data visualization** for sentiment trends  
