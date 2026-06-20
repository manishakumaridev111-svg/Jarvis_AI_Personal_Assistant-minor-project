# Jarvis AI Personal Assistant

A desktop AI voice assistant built with Python and PyQt6, featuring real-time conversation, voice input/output, web search, and system automation.

![Status](https://img.shields.io/badge/status-in--development-yellow)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

## Features

- **Conversational AI** powered by Groq for fast, natural responses
- **Voice input** via speech recognition (microphone)
- **Voice output** via text-to-speech (pyttsx3)
- **Real-time web search** for queries about current events, news, weather, prices, and more
- **System automation**:
  - Open websites (YouTube, Google, Facebook, Instagram)
  - Open applications (Notepad, Calculator)
  - Take screenshots
  - Volume control (up / down / mute)
- **Time & date awareness** using the system clock
- **Animated GUI** built with PyQt6, featuring a live GIF visualizer and chat interface

## Demo

> *(Add a screenshot or GIF of the Jarvis interface here)*

## Tech Stack

| Component | Technology |
|---|---|
| GUI | PyQt6 |
| Chat / LLM | Groq API |
| Text-to-Speech | pyttsx3 |
| Speech-to-Text | SpeechRecognition |
| Automation | Python (`os`, `subprocess`, etc.) |

## Project Structure

```
jarvis/
├── Backend/
│   ├── Chatbot.py            # Core chat logic, search routing, AI responses
│   ├── Model.py               # Groq client / model configuration
│   ├── TextToSpeech.py        # Voice output engine
│   ├── SpeechToText.py        # Voice input (microphone listener)
│   ├── RealtimeSearchEngine.py# Live web search for time-sensitive queries
│   ├── Automation.py          # App/website launching, screenshots, volume control
│   └── ImageGeneration.py     # (optional) image generation features
├── Frontend/
│   ├── GUI.py                 # Main PyQt6 application window
│   └── Graphics/
│       └── Jarvis.gif         # Animated visualizer
├── data/
├── .env                        # API keys (not committed)
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- A Groq API key ([console.groq.com](https://console.groq.com))
- Windows (for `pyttsx3` with the `sapi5` voice engine; other platforms may need a different TTS backend)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/jarvis.git
   cd jarvis
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

5. **Run the application**
   ```bash
   python Frontend/GUI.py
   ```

## Usage

- Type a message in the input box and press **Send**, or hit **Enter**
- Click the **mic button** to speak instead of typing
- Ask Jarvis to:
  - `"What's the time?"` / `"What's today's date?"`
  - `"Open YouTube"` / `"Open Notepad"`
  - `"Take a screenshot"`
  - `"What's the weather today?"` *(triggers real-time search)*
  - General questions, conversation, etc.

## Roadmap

- [ ] Improve real-time search reliability
- [ ] Add wake-word detection ("Hey Jarvis")
- [ ] Expand automation commands
- [ ] Package as a standalone executable
- [ ] Cross-platform TTS support (currently Windows-focused via `sapi5`)

## Future Plans

- **Memory & personalization** — remember user preferences and past conversations across sessions
- **Smart home integration** — control lights, plugs, and other IoT devices
- **Calendar & reminders** — schedule events and get spoken reminders
- **Improved GUI Design** - Enhance gui for better interface
- **Multi-language support** — voice input/output in languages beyond English
- **Custom wake word training** — let users choose their own activation phrase
- **Mobile companion app** — control or query Jarvis remotely from a phone
- **Better NLP intent detection** — replace keyword matching with proper intent classification
- **Voice authentication** — recognize the user by voice for personalized responses

## Contributing

This is a personal/learning project, but suggestions and pull requests are welcome. Feel free to open an issue if you spot a bug or have an idea.

## Author

**Manisha Kumari**

GitHub: @manishakumaridev111-svg

## Acknowledgments

- [Groq](https://groq.com) for fast LLM inference
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3) for offline text-to-speech
- Built as part of a personal learning journey into AI assistants and Python development
- Developed as a BCA Minor Project.
- Built using Python and open-source technologies.
- Inspired by modern AI assistant systems.
- Thanks to faculty members and mentors for their valuable guidance.

 ## License

This project is open source and available under the [MIT License](LICENSE)
