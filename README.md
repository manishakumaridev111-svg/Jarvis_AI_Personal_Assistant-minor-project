# Jarvis AI Personal Assistant

A voice-enabled AI personal assistant powered by Groq's language model. Jarvis listens to your queries and responds with intelligent answers and text-to-speech capabilities.

## Features

- 🎤 **Voice Input** - Ask questions naturally through text input
- 🔊 **Text-to-Speech** - Automatic voice responses using pyttsx3
- 🧠 **AI-Powered Responses** - Uses Groq API for intelligent question answering
- 🔍 **Web Search Integration** - Search the web using DuckDuckGo
- ⚡ **Fast Processing** - Leverages Groq's fast inference API

## Project Structure

```
.
├── Main.py           # Main application entry point
├── Backend/
│   ├── Model.py      # AI model and response logic
│   └── TextToSpeech.py # Text-to-speech functionality
├── .env              # Environment variables (API keys)
└── requirements.txt  # Python dependencies
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/manishakumaridev111-svg/Jarvis_AI_Personal_Assistant-minor-project.git
   cd Jarvis_AI_Personal_Assistant-minor-project
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

## Usage

Run the assistant:
```bash
python Main.py
```

Then interact with Jarvis:
```
Jarvis Started
Hello Master
You : What is the weather today?
Jarvis : [Response from AI model]
```

## Dependencies

Key dependencies include:
- **groq** - Groq API client for AI responses
- **pyttsx3** - Text-to-speech engine
- **SpeechRecognition** - Voice input (future enhancement)
- **python-dotenv** - Environment variable management
- **requests** - HTTP library for API calls
- **beautifulsoup4** - Web scraping capabilities
- **duckduckgo-search** - Web search integration

See `requirements.txt` for the complete list.

## API Keys

This project requires a Groq API key:
1. Sign up at [Groq Console](https://console.groq.com)
2. Generate an API key
3. Add it to your `.env` file

## Future Enhancements

- [ ] Voice input using SpeechRecognition
- [ ] PyQt6 GUI interface
- [ ] Web search integration
- [ ] Multi-language support
- [ ] Conversation history
- [ ] Custom voice configurations

## License

This project is open source and available under the MIT License.

## Author

Manisha Kumari

## Support

For issues, suggestions, or contributions, feel free to open an issue or create a pull request.

---

**Note**: Make sure to keep your `.env` file with API keys private and never commit it to version control.
