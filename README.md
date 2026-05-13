# 🤖 AI Blog Generator using AWS Bedrock & Llama 3

An AI-powered Blog Generation application built using Amazon Bedrock, Meta Llama 3, Python, and Streamlit.

This project generates high-quality blogs automatically based on user prompts using Large Language Models (LLMs) hosted on AWS Bedrock.

---

# 🚀 Features

- ✨ AI-powered blog generation
- ☁️ Amazon Bedrock integration
- 🤖 Meta Llama 3 model support
- 🐍 Python backend
- 🎨 Streamlit web interface
- 🔐 Secure AWS API integration
- 📄 Dynamic prompt-based content generation
- ⚡ Real-time response generation

---

# 🛠️ Technologies Used

- Python
- AWS Bedrock
- Meta Llama 3
- Boto3
- Streamlit
- JSON
- Prompt Engineering

---

# 📂 Project Structure

```bash
llama_using_awsbedrock/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── venv/
└── templates/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/divyasreevemula918/llama_using_awsbedrock.git

cd llama_using_awsbedrock
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ☁️ AWS Configuration

Configure AWS credentials:

```bash
aws configure
```

Provide:
- AWS Access Key
- AWS Secret Key
- Region Name (`us-east-1`)
- Output Format (`json`)

---

# 🔑 Enable Bedrock Model Access

Go to:

Amazon Bedrock → Model Catalog → Request Access

Enable:
- Meta Llama 3

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 💡 Sample Prompt

```text
Write a 200-word blog on Artificial Intelligence
```

---

# 🧠 How It Works

```text
User Prompt
     ↓
Streamlit UI
     ↓
AWS Bedrock API
     ↓
Meta Llama 3 Model
     ↓
AI Generated Blog
```

---

# 📸 Output

The application generates:
- AI-generated blogs
- Dynamic text responses
- Human-like content generation

---

## 🌍 Live API Endpoint

POST:
https://5prpgdimv3.execute-api.us-east-1.amazonaws.com/dev/blog

### Sample Request Body

{
   "blogtopic":"Machine Learning"
}


# screenshots
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2e495d43-b1c5-428b-9758-31508a6990b9" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5bff9ef3-d479-4f36-b32f-fd43613d6eee" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/201b9e9b-817a-422e-9256-0b5227cff92a" />



# 📌 Example Bedrock API Request

```python
response = bedrock.invoke_model(
    modelId="meta.llama3-70b-instruct-v1:0",

    contentType="application/json",

    accept="application/json",

    body=json.dumps({
        "prompt": "<s>[INST] Human: write a 200 words blog on the topic {blogtopic} Assistant: [/INST]",

        "max_gen_len": 512,

        "temperature": 0.5,

        "top_p": 0.9
    })
)
```

---

# 🎯 Learning Outcomes

Through this project, I learned:

- Generative AI concepts
- Prompt Engineering
- Amazon Bedrock integration
- LLM API invocation
- Streamlit application development
- Cloud AI deployment basics
- JSON request handling

---

# 📈 Future Improvements

- 📄 PDF upload support
- 🧠 RAG integration
- 💬 AI chatbot feature
- 🌐 Multi-language support
- 🗂️ Blog history storage
- 🔊 Voice input support

---

# 🙌 Acknowledgements

- AWS Bedrock Documentation
- Meta Llama Models
- Streamlit
- Boto3 SDK

---

# 📬 Connect With Me

👩‍💻 GitHub:  
https://github.com/divyasreevemula918

---

