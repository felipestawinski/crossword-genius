# Crossword Solver Bot

This project automates the process of completing a crossword puzzle on the [Racha Cuca](https://rachacuca.com) website. Using the OpenAI API for answer retrieval and Python Selenium for browser automation, the bot solves the crossword and fills in the answers efficiently.

---

## Features

- **AI-Powered Answer Retrieval**: Leverages OpenAI's API to analyze and generate accurate answers to crossword clues.
- **Browser Automation**: Uses Python Selenium to interact with the Racha Cuca crossword interface and input answers programmatically.
- **Customizable Workflow**: Modular design allows easy customization for different puzzle formats or logic enhancements.

---

## Requirements

### Software

- **Python**: Version 3.8 or later.
- **Web Browser**: Chrome or any Selenium-compatible browser.
- **ChromeDriver**: Ensure it matches your Chrome version.

### Python Libraries

Install the required libraries using pip:

```bash
pip install openai selenium
```

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/crossword-solver-bot.git
   cd crossword-solver-bot
   ```

2. **Install Dependencies**
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Obtain API Keys**
   - Get an API key from [OpenAI](https://platform.openai.com/).
   - Place the key in a `.env` file or directly in your configuration script:
     ```env
     OPENAI_API_KEY=your-api-key-here
     ```

4. **Set Up ChromeDriver**
   - Download the ChromeDriver version compatible with your browser from [here](https://chromedriver.chromium.org/downloads).
   - Add the executable to your system PATH or provide its location in the script.

5. **Test the Setup**
   Run a quick test to verify dependencies:
   ```bash
   python main.py --test
   ```

---

## Usage

1. **Run the Bot**
   Start the bot with:
   ```bash
   python main.py
   ```

2. **Configuration**
   - Update `config.py` with any project-specific settings:
     - Crossword URL.
     - Clue parsing logic (if required).

3. **Interactive Mode** (Optional)
   Enable interactive debugging by setting the `DEBUG` flag in `config.py` to `True`.

---

## File Structure

```plaintext
.
├── main.py            # Main script to run the bot
├── config.py          # Configuration settings
├── crossword_solver   # Core logic and modules
│   ├── api_handler.py # Interacts with OpenAI API
│   ├── browser.py     # Selenium browser automation
│   ├── parser.py      # Parses clues from the webpage
├── requirements.txt   # Required Python libraries
└── README.md          # Project documentation
```

---

## Limitations

- Performance depends on the quality of responses from the OpenAI API.
- Updates to the Racha Cuca website may require adjustments in the Selenium logic.

---

## Future Enhancements

- **Improved Answer Validation**: Add context-based filtering to ensure accuracy.
- **Multi-Language Support**: Extend to handle crosswords in languages other than Portuguese.
- **Error Handling**: Robust mechanisms to handle API errors or unexpected webpage changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Acknowledgments

- [OpenAI](https://platform.openai.com/) for their powerful API.
- [Selenium](https://www.selenium.dev/) for browser automation.
- [Racha Cuca](https://rachacuca.com) for providing challenging puzzles.

---

## Contact

For questions or collaboration, feel free to reach out:

- **Email**: felipe.stawinski@gmail.com
- **GitHub**: https://github.com/felipestawinski

