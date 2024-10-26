# A.S.U.N.A. - Advanced Speech Understanding and Navigation Assistant

ASUNA is a voice-controlled virtual assistant built using Rasa for natural language processing, gTTS (Google Text-to-Speech) for voice synthesis, and Selenium for web automation tasks. This assistant is capable of responding to voice commands, providing information, and even automating simple browser-based tasks.

## Features

* **Natural Language Understanding:** Uses Rasa for understanding and processing voice commands.
* **Voice Output:** gTTS synthesizes responses for a seamless conversation experience.
* **Web Automation:** Utilizes Selenium to perform browser automation, allowing Asuna to fetch information or complete tasks online.
* **Customizable Skills:** Easily add new intents, actions, and responses.

## Technologies Used

* **Rasa:** An open-source machine learning framework for automated text and voice-based conversations.
* **gTTS (Google Text-to-Speech):** Converts text responses to speech, aking the interaction natural and engaging.
* **Selenium:** A tool for browser automation that enables Asuna to perform online tasks.

## Setup and Installation

### Prerequisites
* Python 3.7+
* **Rasa:** Follow the Rasa Installation Guide to set up Rasa.
* **Selenium:** Install Selenium using `pip install selenium`. You may also need to download the appropriate WebDriver (e.g., ChromeDriver) for your browser.
* **gTTS:** Install using `pip install gtts`.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/asuna-voice-assistant.git
    cd asuna-voice-assistant
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Setup Rasa:**
    Initialize Rasa and train the assistant model:
    ```bash
    rasa train
    ```

4. **Run Selenium WebDriver:**
    Make sure the correct WebDriver (e.g., ChromeDriver) is available in your PATH.

## Usage

1. **Start Rasa Server:**
    ```bash
    rasa run --enable-api
    ```

2. **Start the Assistant:**
    Run the main script to initialize Asuna:
    ```bash
    python asuna.py
    ```

3. **Interacting with Asuna:**
    Speak a command, and Asuna will respond based on your intents and actions.

##  Future Improvements

* **Enhanced Voice Recognition:** Integrate ASR (Automatic Speech Recognition) for real-time command understanding.
* **Additional Integrations:** Connect to other APIs or databases to expand the range of responses.
* **Improved Natural Language Generation:** Refine responses for a more conversational experience.

## Contributing

Feel free to contribute by forking the repository and making a pull request. For major changes, open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.