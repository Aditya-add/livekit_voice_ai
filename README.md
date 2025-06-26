# 🎙️ LiveKit Voice AI

**LiveKit Voice AI** is a starter project integrating LiveKit's real-time audio/video capabilities with AI-powered backend logic. The project combines a Python-based backend and token server with a React frontend, adapted from LiveKit's official resources.

---

## 🗂️ Project Structure

```
livekit_voice_ai/
├── agent-starter-react/    # Frontend React application (based on LiveKit examples)
├── src/                    # Python backend services
│   ├── agent.py            # AI/Voice agent logic
│   └── token_server.py     # Token generation server for LiveKit
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🚀 Features

✅ Real-time audio/video communication using [LiveKit](https://livekit.io/)
✅ AI-powered backend with Python
✅ Token-based authentication server
✅ React frontend with LiveKit integration
✅ Quick-start setup for experimentation and development

---

## ⚙️ Tech Stack

* **Backend:** Python
* **Frontend:** React (LiveKit starter project)
* **Real-time Engine:** [LiveKit](https://livekit.io/)

---

## 🏁 Getting Started

### 1️⃣ Install Backend Requirements

```bash
pip install -r requirements.txt
```

### 2️⃣ Install Frontend Dependencies

```bash
cd agent-starter-react
npm install
```

### 3️⃣ Run the Project

You can launch all components sequentially with time gaps (adjust time as needed):

```powershell
Start-Process powershell -ArgumentList "python src/agent.py dev"
Start-Sleep -Seconds 5

Start-Process powershell -ArgumentList "python src/token_server.py"
Start-Sleep -Seconds 5

Start-Process powershell -ArgumentList "cd agent-starter-react; npm run dev"
```

Alternatively, run each in separate terminals if preferred.

---

## 🌐 Frontend Details

The frontend is based on the official **LiveKit React Starter** available in [LiveKit Docs](https://docs.livekit.io/). It provides:

* Simple interface for joining rooms
* Audio/video stream handling
* Ready-to-extend UI

---

## 📌 Notes

* Ensure you have valid LiveKit credentials configured in both frontend and backend.
* Backend AI logic can be modified within `src/agent.py` based on your needs.

---

## 📣 Resources

* [LiveKit Documentation](https://docs.livekit.io/)
* [LiveKit GitHub](https://github.com/livekit)
* [React](https://react.dev/)
* [Python](https://www.python.org/)

---

## 🛠️ Contribution

PRs and suggestions are welcome! Feel free to fork the repo and enhance functionality.

---