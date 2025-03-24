# 📲 Twilio SMS Sender

Easily send SMS messages using Twilio's API with this simple Python script! 🚀

---

## 📌 Features
✅ Send SMS messages via Twilio API  
✅ Secure credential handling with `.env`  
✅ Simple and lightweight script  
✅ Error handling for failed messages  

---

## 📦 Prerequisites

🔹 Python 3.x installed  
🔹 Twilio account with API credentials  

---

## ⚙️ Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/DaChe01/SMS-Sender.git
cd twilio-sms-sender
```

### 2️⃣ Install Twilio Library

```bash
pip install twilio python-dotenv
```

### 3️⃣ Configure Environment Variables

Create a `.env` file and add your Twilio credentials:

```ini
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
```

---

## 🚀 Usage

Run the script to send an SMS:

```bash
python send_sms.py
```

📌 **Customize the recipient and message** by modifying:

```python
send_sms(
    to_number="+9189XXXXXXXX",
    message_body="Hello World! Test SMS from Python via Twilio",
)
```

---

## 🛠️ Troubleshooting

If the message fails to send, check:
- ✅ Correct Twilio credentials in `.env`
- ✅ Proper `to_number` format (e.g., `+9189XXXXXXXX`)
- ✅ Sufficient balance and permissions in your Twilio account

---

## 📜 License

📝 This project is licensed under the **MIT License**. Feel free to modify and use it as needed! 🎉