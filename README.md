# 🎙️ Thapar University Voicebot (TIET VoiceBot)

A conversational AI voicebot built for **Thapar Institute of Engineering and Technology (TIET), Patiala** using the Rasa framework. It answers campus-related queries through both text and voice — providing directions to buildings, lab room numbers, faculty info, WiFi passwords, timetables, society details, nearby restaurants, and more.

---

## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Architecture Diagram](#architecture-diagram)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [How to Run (End-to-End)](#how-to-run-end-to-end)
- [Project Structure & File Explanations](#project-structure--file-explanations)
- [How It Works (Data Flow)](#how-it-works-data-flow)
- [Intents & Capabilities](#intents--capabilities)
- [Custom Actions Explained](#custom-actions-explained)
- [NLU Pipeline & Policies](#nlu-pipeline--policies)
- [Web Interface](#web-interface)
- [Voice Mode](#voice-mode)
- [Training the Model](#training-the-model)
- [Testing](#testing)
- [Deployment Guide](#deployment-guide)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Project Overview

This project is a **campus assistant chatbot** that helps Thapar University students and visitors get quick answers about:

| Category | Examples |
|----------|----------|
| Directions | "Where is H Block?", "Directions to CSED building" |
| Lab Locations | "Where is Programming Lab 1?", "Room no of Data Science Lab" |
| Faculty Info | "Tell me about computer department faculty" |
| Office Cabins | "Where is DOAA office?", "Room no of Director" |
| WiFi Passwords | "What is the password for hostel wifi?" |
| Timetables | "What is the timetable of second year?" |
| Societies | "Tell me about Thapar societies" |
| Restaurants | "Restaurants nearby Thapar" |
| Banking | "Where is SBI bank?" |
| Library | "Where is the library?" |
| Sports | "Where can I play football?" |
| Medical | "Where is the dispensary?" |

The bot supports **three interaction modes**:
1. **Text Chat** — Type queries in the web interface
2. **Voice Input** — Speak queries via microphone (speech-to-text)
3. **Voice Output** — Bot responses are spoken aloud (text-to-speech)

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                            │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐   │
│  │  Web Chat UI │    │  Voice Input │    │  CLI Voicebot    │   │
│  │ (Flask App)  │    │ (Microphone) │    │  (voicebot.py)   │   │
│  └──────┬───────┘    └──────┬───────┘    └────────┬─────────┘   │
└─────────┼───────────────────┼─────────────────────┼─────────────┘
          │                   │                     │
          │  Google Speech    │                     │
          │  Recognition API  │                     │
          │◄──────────────────┘                     │
          │                                         │
          ▼                                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    RASA SERVER (localhost:5002)                   │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────────────┐ │
│  │  NLU Engine │  │  Dialogue    │  │  Response Generation   │ │
│  │  (DIET +    │→ │  Management  │→ │  (Templates + Actions) │ │
│  │  Features)  │  │  (TED+Memo)  │  │                        │ │
│  └─────────────┘  └──────────────┘  └───────────┬────────────┘ │
└──────────────────────────────────────────────────┼──────────────┘
                                                   │
                                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│              ACTION SERVER (localhost:5055)                       │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  Custom Actions (actions.py)                               │ │
│  │  - Look up lab rooms, block directions, cabin numbers      │ │
│  │  - Open faculty pages in browser                           │ │
│  │  - Redirect to external info pages (myherupa.com)          │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                                                   │
                                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                      RESPONSE TO USER                            │
│  ┌──────────────┐    ┌──────────────────────────────────────┐   │
│  │  Text Reply  │    │  Voice Reply (gTTS → MP3 → Speaker) │   │
│  └──────────────┘    └──────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Chatbot Framework | Rasa Open Source (v2.x) |
| NLU Classifier | DIET (Dual Intent and Entity Transformer) |
| Dialogue Policies | TEDPolicy + MemoizationPolicy + MappingPolicy |
| Web Framework | Flask (Python) |
| Speech-to-Text | Google Speech Recognition API (`speech_recognition`) |
| Text-to-Speech | Google Text-to-Speech (`gTTS`) |
| Audio Playback | `playsound` |
| Frontend | HTML/CSS/JavaScript with Jinja2 templating |
| Language | Python 3.6+ |

---

## Prerequisites

Before you begin, make sure you have:

- **Python 3.6 – 3.8** (Rasa 2.x requires this range)
- **pip** (Python package manager)
- **A working microphone** (for voice features)
- **Speakers/headphones** (for text-to-speech output)
- **Google Chrome** (some actions open browser tabs)
- **Internet connection** (for Google Speech API and gTTS)

---

## Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Rizul-GitHub/Thapar_Voicebot.git
cd Thapar_Voicebot
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install Rasa
pip install rasa==2.8.0

# Install Rasa SDK (for custom actions)
pip install rasa-sdk==2.8.0

# Install other dependencies
pip install flask
pip install gTTS
pip install playsound
pip install SpeechRecognition
pip install PyAudio          # Required for microphone access
pip install requests
```

> **Note on PyAudio (Windows):** If `pip install PyAudio` fails, download the appropriate `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it manually:
> ```bash
> pip install PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl
> ```

### Step 4: Train the Rasa Model

```bash
rasa train
```

This reads `config.yml`, `domain.yml`, `data/nlu.md`, and `data/stories.md` to produce a trained model in the `models/` folder.

---

## How to Run (End-to-End)

You need **3 terminal windows** running simultaneously:

### Terminal 1: Start the Rasa Server

```bash
rasa run -m models --enable-api --cors "*" --debug -p 5002
```

This starts the Rasa server on `http://localhost:5002` with the REST API enabled.

### Terminal 2: Start the Action Server

```bash
rasa run actions --port 5055
```

This starts the custom action server on `http://localhost:5055/webhook`.

### Terminal 3: Start the Web Interface (Flask App)

```bash
python form2.py
```

This starts the Flask web server (default: `http://localhost:5000`).

### Now Use the Bot

- **Web Chat:** Open `http://localhost:5000` in your browser. Click the chat icon (bottom-right) and type your query.
- **Voice Mode:** Type `voice` in the chat input to activate microphone listening.
- **CLI Voice Mode:** Run `python voicebot.py` for a terminal-based voice conversation loop.

---

## Project Structure & File Explanations

```
Thapar_Voicebot/
│
├── config.yml              # Rasa NLU pipeline + dialogue policy configuration
├── domain.yml              # Bot's universe: intents, entities, slots, responses, actions
├── credentials.yml         # Channel credentials (REST API enabled)
├── endpoints.yml           # Action server endpoint configuration
│
├── data/
│   ├── nlu.md              # NLU training data (intent examples + entity annotations)
│   └── stories.md          # Conversation flow stories for dialogue training
│
├── actions.py              # Custom action code (Python) — the bot's "brain"
│
├── form2.py                # Flask web application (main entry point for web UI)
├── form_data.py            # Earlier version of the Flask app (alternate/backup)
│
├── voicebot.py             # Standalone CLI voice conversation loop
├── voice_to_text.py        # Standalone speech-to-text demo script
├── text_to_voice.py        # Standalone text-to-speech demo script
│
├── templates/
│   └── IY_Home_page.html   # Web UI template (chat widget + Thapar homepage)
│
├── models/                 # Trained Rasa models (compressed .tar.gz files)
│   └── *.tar.gz
│
├── tests/
│   └── conversation_tests.md  # Rasa conversation test cases
│
├── __init__.py             # Python package marker (empty)
├── events.db               # Rasa event tracker database (SQLite)
├── rasa.db                 # Rasa internal database
└── *.mp3                   # Temporary audio files from gTTS (can be ignored)
```

---

## Detailed File Explanations

### `config.yml` — NLU Pipeline & Policies

This file defines **how the bot understands language** and **how it decides what to do next**.

**NLU Pipeline (language understanding):**
1. `WhitespaceTokenizer` — Splits text into words by whitespace
2. `RegexFeaturizer` — Adds regex-based features for entity extraction
3. `LexicalSyntacticFeaturizer` — Adds word-level features (POS-like)
4. `CountVectorsFeaturizer` — Bag-of-words features (word level)
5. `CountVectorsFeaturizer` (char_wb) — Character n-gram features (1–4 chars) for typo robustness
6. `DIETClassifier` — The main intent classifier + entity extractor (100 epochs)
7. `EntitySynonymMapper` — Maps entity synonyms to canonical values
8. `ResponseSelector` — Selects appropriate response templates (100 epochs)

**Dialogue Policies (conversation management):**
1. `MemoizationPolicy` — Memorizes exact story patterns from training data
2. `TEDPolicy` — Transformer-based policy for generalizing dialogue (100 epochs, history=5)
3. `MappingPolicy` — Maps certain intents directly to actions

---

### `domain.yml` — The Bot's Universe

Defines everything the bot knows about:

- **22 Intents** — What the user might want (greet, ask_for_lab, ask_for_wifi, etc.)
- **5 Entities** — Key information to extract (block, department_name, designation, lab, wifi)
- **5 Slots** — Memory storage for extracted entities (all text type, auto-filled)
- **Responses** — Pre-defined text replies (utter_greet, utter_goodbye, utter_bank, etc.)
- **8 Custom Actions** — Python functions that run custom logic

---

### `data/nlu.md` — Training Examples

Contains example sentences for each intent with entity annotations:

```markdown
## intent:ask_for_lab
- Where is [programming lab 1](lab)?
- room no of [Cloud and IoT Research Lab](lab)
```

The `[text](entity_name)` syntax tells Rasa which words are entities.

---

### `data/stories.md` — Conversation Flows

Defines expected conversation patterns:

```markdown
## ask for lab direction
* greet
  - utter_greet
* ask_for_lab
  - action_show_lab
* deny
  - utter_goodbye
```

Each story is a sequence: user intent → bot action → user intent → bot action...

---

### `actions.py` — Custom Actions (The Brain)

This is where the real logic lives. It contains Python classes that:

| Action | What It Does |
|--------|-------------|
| `action_show_cabin_dir` | Looks up office cabin numbers (Dean → B block, DOAA → B001, etc.) |
| `action_show_lab` | Looks up 50+ CSED lab room numbers from a dictionary |
| `action_show_block` | Provides directions to campus blocks (H block, B block, etc.) |
| `action_show_faculty` | Opens the department's faculty webpage in Chrome |
| `action_wifi` | Opens the WiFi password page on myherupa.com |
| `action_timetable` | Opens the timetable page |
| `action_society` | Opens the societies information page |
| `action_restaurants` | Opens nearby restaurants page |

**How it works:** Each action extracts the relevant slot (entity) from the conversation, looks it up in a Python dictionary, and returns the result as a message.

---

### `form2.py` — Flask Web Application (Main)

The primary web server that:
1. Serves the chat UI at `http://localhost:5000`
2. Handles POST requests from the chat form
3. Forwards user messages to the Rasa server via REST webhook
4. Supports voice input (type "voice" to activate microphone)
5. Converts bot responses to speech using gTTS
6. Plays audio responses through speakers
7. Supports "restart"/"cls" to clear conversation history

---

### `voicebot.py` — CLI Voice Loop

A standalone script for pure voice interaction:
1. Sends initial "Hello" to Rasa → gets greeting → speaks it
2. Enters a loop: listen via microphone → send to Rasa → speak response
3. Continues until bot says "Bye"

---

### `voice_to_text.py` & `text_to_voice.py` — Utility Scripts

Standalone demo scripts:
- `voice_to_text.py` — Records from microphone and prints recognized text
- `text_to_voice.py` — Converts a hardcoded string to speech and plays it

These were likely used during development to test the speech APIs independently.

---

### `templates/IY_Home_page.html` — Web UI

A full-page web interface featuring:
- **Hero section** with Thapar University info (address, phone, email)
- **Sidebar navigation** with links to Thapar's official pages (Admissions, Webkiosk, Placements, etc.)
- **Chat popup widget** (bottom-right) styled like a messaging app
- **Jinja2 templating** to render conversation history dynamically

---

## How It Works (Data Flow)

### Text Mode Flow:
```
User types message in web UI
        │
        ▼
Flask app (form2.py) receives POST request
        │
        ▼
Forwards message to Rasa REST webhook (localhost:5002)
        │
        ▼
Rasa NLU classifies intent + extracts entities
        │
        ▼
Rasa Core (dialogue policies) decides next action
        │
        ├── Simple response → Returns utter_* template text
        │
        └── Custom action → Calls action server (localhost:5055)
                │
                ▼
        actions.py executes logic (dict lookup / browser open)
                │
                ▼
        Returns response text to Rasa → back to Flask
        │
        ▼
Flask converts response to speech (gTTS) → plays audio
        │
        ▼
Renders updated chat in HTML template
```

### Voice Mode Flow:
```
User says "voice" in chat (or uses voicebot.py)
        │
        ▼
Microphone activated → speech_recognition listens
        │
        ▼
Google Speech API converts audio → text
        │
        ▼
Text sent to Rasa REST webhook (same as text mode)
        │
        ▼
Response received → gTTS converts to MP3 → plays through speakers
```

---

## Intents & Capabilities

| Intent | Description | Example Utterances |
|--------|-------------|-------------------|
| `greet` | User greeting | "hey", "hello", "good morning" |
| `goodbye` | User farewell | "bye", "see you later" |
| `affirm` | User confirms | "yes", "correct", "of course" |
| `deny` | User denies | "no", "never", "not really" |
| `mood_great` | User is happy | "great", "amazing", "wonderful" |
| `mood_unhappy` | User is sad | "sad", "terrible", "awful" |
| `bot_challenge` | Asks if bot | "are you a bot?", "am I talking to a human?" |
| `ask_for_block` | Block directions | "Where is H block?", "directions to E block" |
| `ask_for_lab` | Lab room numbers | "Where is Programming Lab 1?" |
| `ask_for_cabin` | Office locations | "Where is DOAA office?" |
| `ask_for_faculty` | Faculty info | "computer department faculty" |
| `ask_for_wifi` | WiFi passwords | "password for hostel wifi" |
| `ask_for_timetable` | Timetable info | "timetable of second year" |
| `ask_for_society` | Society info | "societies in thapar" |
| `ask_for_restaurants` | Food places | "restaurants nearby" |
| `ask_for_bank` | Bank locations | "where is SBI bank?" |
| `ask_for_registary` | Registry office | "where is registary?" |
| `ask_for_library` | Library info | "where is library?" |
| `ask_for_dispensary` | Medical facility | "where is dispensary?" |
| `ask_for_sports` | Sports facilities | "where can I play football?" |
| `ask_for_swimming` | Swimming pool | "where is swimming pool?" |

---

## Custom Actions Explained

### `action_show_cabin_dir`
Extracts the `designation` entity (dean, doaa, dosa, director) and returns the room number from a lookup dictionary.

```python
cabins = {
    "dean": "B block",
    "doaa": "B001",
    "dosa": "B002",
    "director": "A001"
}
```

### `action_show_lab`
Contains a comprehensive dictionary of **50+ CSED labs** with their room numbers (L001–L531). Extracts the `lab` entity and returns the room number.

### `action_show_block`
Maps campus blocks to their physical locations:
```python
blocks = {
    "h block": "Adjacent to the Day Scholar Parking",
    "b block": "Adjacent to K lawns and main Cafeteria",
    "csed building": "Near the New nava nalanda Central Library",
    ...
}
```

### `action_show_faculty`
Opens the department's faculty page in Chrome browser using `webbrowser` module. Maps department names to their official Thapar URLs.

### `action_wifi`, `action_timetable`, `action_society`, `action_restaurants`
These actions open relevant pages on `myherupa.com` (a companion website) in the browser and return a confirmation message.

---

## NLU Pipeline & Policies

### Why This Pipeline?

```yaml
pipeline:
  - WhitespaceTokenizer        # Simple, fast tokenization
  - RegexFeaturizer            # Helps with entity patterns
  - LexicalSyntacticFeaturizer # Word-level context features
  - CountVectorsFeaturizer     # Bag-of-words (captures word presence)
  - CountVectorsFeaturizer     # Character n-grams (handles typos/misspellings)
    analyzer: "char_wb"
    min_ngram: 1, max_ngram: 4
  - DIETClassifier             # State-of-the-art joint intent+entity model
    epochs: 100
  - EntitySynonymMapper        # Normalizes entity values
  - ResponseSelector           # Picks best response template
    epochs: 100
```

The dual CountVectorsFeaturizer (word + character) approach makes the bot robust to typos — e.g., "programing lab" still matches "programming lab".

### Why These Policies?

```yaml
policies:
  - MemoizationPolicy    # Exact match on training stories (high confidence)
  - TEDPolicy            # Generalizes to unseen conversation patterns
    max_history: 5       # Considers last 5 turns for context
    epochs: 100
  - MappingPolicy        # Direct intent→action mapping (fastest)
```

---

## Web Interface

The web UI (`templates/IY_Home_page.html`) provides:

1. **Full-page Thapar homepage** with hero image and university contact info
2. **Sidebar** with quick links to official Thapar pages (Admissions, Webkiosk, etc.)
3. **Chat widget** (click the message icon, bottom-right):
   - Styled like a modern messaging app
   - Shows conversation history with different styles for user/bot messages
   - Text input field with Enter button
   - Microphone icon for voice input

### Chat Commands:
- Type any query → sends to Rasa bot
- Type `voice` → activates microphone for speech input
- Type `restart` or `cls` → clears conversation history

---

## Voice Mode

### How Speech-to-Text Works:
1. Uses `speech_recognition` library
2. Activates system microphone
3. Listens for audio input
4. Sends audio to **Google Speech Recognition API** (free, requires internet)
5. Returns recognized text

### How Text-to-Speech Works:
1. Uses `gTTS` (Google Text-to-Speech)
2. Converts bot's text response to an MP3 file
3. Saves temporarily with a random filename
4. Plays the MP3 using `playsound`
5. Deletes the temporary file

---

## Training the Model

### Initial Training:
```bash
rasa train
```

### Retrain After Changes:
```bash
# After modifying nlu.md, stories.md, or domain.yml:
rasa train

# Train only NLU (faster, if only nlu.md changed):
rasa train nlu
```

### Interactive Training (add new examples):
```bash
rasa interactive
```

### Test in Shell (quick testing without web UI):
```bash
rasa shell
```

---

## Testing

### Run Conversation Tests:
```bash
rasa test
```

The test file (`tests/conversation_tests.md`) contains predefined conversation flows that verify the bot responds correctly.

### Test NLU Only:
```bash
rasa test nlu
```

### Manual Testing:
```bash
# Quick chat in terminal:
rasa shell

# With debug output:
rasa shell --debug
```

---

## Deployment Guide

### Local Deployment (Development)

This is what's described in the [How to Run](#how-to-run-end-to-end) section — 3 terminals running Rasa server, action server, and Flask app.

### Production Deployment

For a production setup, you would:

#### 1. Use a Production WSGI Server for Flask
```bash
pip install gunicorn  # Linux/Mac
gunicorn form2:app --bind 0.0.0.0:5000

# Or on Windows:
pip install waitress
waitress-serve --port=5000 form2:app
```

#### 2. Run Rasa as a Background Service
```bash
# Using nohup (Linux):
nohup rasa run -m models --enable-api --cors "*" -p 5002 &
nohup rasa run actions --port 5055 &
```

#### 3. Docker Deployment (Recommended for Production)

Create a `Dockerfile`:
```dockerfile
FROM rasa/rasa:2.8.0-full

COPY . /app
WORKDIR /app

RUN rasa train

EXPOSE 5002
CMD ["run", "--enable-api", "--cors", "*", "-p", "5002"]
```

Create a `docker-compose.yml`:
```yaml
version: '3'
services:
  rasa:
    build: .
    ports:
      - "5002:5002"
  
  action-server:
    build: .
    command: ["run", "actions", "--port", "5055"]
    ports:
      - "5055:5055"
  
  web:
    build: .
    command: ["python", "form2.py"]
    ports:
      - "5000:5000"
    depends_on:
      - rasa
      - action-server
```

#### 4. Cloud Deployment Options
- **Heroku** — Free tier available, good for demos
- **AWS EC2** — Full control, scalable
- **Google Cloud Run** — Serverless, auto-scaling
- **DigitalOcean** — Simple VPS deployment

#### 5. Network Configuration
If deploying on a network (e.g., college LAN):
```python
# In form2.py, change the last line to:
app.run(debug=False, host="0.0.0.0", port=5000)
```
This makes the Flask app accessible from other machines on the network.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `PyAudio` installation fails | Download the `.whl` file for your Python version from unofficial binaries |
| "Could not recognize your voice" | Check microphone permissions, ensure internet connection |
| Rasa server won't start | Ensure you've trained a model first (`rasa train`) |
| Action server errors | Check that `actions.py` has no syntax errors; run `rasa run actions` with `--debug` |
| "Connection refused" on port 5002 | Rasa server isn't running — start it first |
| gTTS fails | Requires internet connection for Google's TTS API |
| `playsound` errors on Linux | Install `sudo apt-get install gstreamer1.0-plugins-base` |
| Browser doesn't open for faculty | Update `chrome_path` in `actions.py` to match your Chrome installation path |
| Flask app shows empty chat | Make sure Rasa server (port 5002) is running before starting Flask |

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-intent`)
3. Add training data to `data/nlu.md` and stories to `data/stories.md`
4. Update `domain.yml` if adding new intents/entities/actions
5. Add custom action logic to `actions.py` if needed
6. Train and test (`rasa train && rasa test`)
7. Submit a Pull Request

### Adding a New Intent (Example):

1. **Add training examples** in `data/nlu.md`:
   ```markdown
   ## intent:ask_for_hostel
   - where is my hostel
   - hostel location
   - how to reach J hostel
   ```

2. **Add the intent** to `domain.yml`:
   ```yaml
   intents:
     - ask_for_hostel
   ```

3. **Add a response** in `domain.yml`:
   ```yaml
   responses:
     utter_hostel:
       - text: "Hostels are located behind the academic blocks."
   ```

4. **Add a story** in `data/stories.md`:
   ```markdown
   ## hostel query
   * greet
     - utter_greet
   * ask_for_hostel
     - utter_hostel
   ```

5. **Retrain**: `rasa train`

---

## License

This project was developed as a capstone project at Thapar Institute of Engineering and Technology, Patiala.

---

## Acknowledgments

- Built with [Rasa Open Source](https://rasa.com/)
- Voice powered by [Google Speech Recognition](https://cloud.google.com/speech-to-text) and [gTTS](https://gtts.readthedocs.io/)
- Campus data sourced from [myherupa.com](https://myherupa.com/)
- Web interface built with [Flask](https://flask.palletsprojects.com/)
