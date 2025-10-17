

## 🌍 Aya's Translation Tool

### 📖 Description

**Aya's Translation Tool** is a simple and interactive command-line application that allows users to translate text into multiple languages using the **Google Translator API** via the `deep_translator` library.

The program supports several popular languages and keeps running until the user types `exit`.

---

### 🧩 Features

* 🌐 Supports multiple languages: Arabic, English, French, German, Spanish, Italian, Chinese, and Japanese.
* 🧠 Automatically detects the source language.
* 🔁 Translates any input text in real-time.
* 🖥️ User-friendly interface with numbered language choices.

---

### 🛠️ Technologies Used

* **Python 3**
* **deep_translator** library

---

### ⚙️ Installation

1. **Clone the repository** or download the file:

   ```bash
   git clone https://github.com/<your-username>/ayas-translation-tool.git
   ```

2. **Open the project** in **Visual Studio Code** (or any Python IDE).

3. **Install the required library**:

   ```bash
   pip install deep-translator
   ```

4. **Run the program**:

   ```bash
   python translator.py
   ```

---

### 🧠 How It Works

1. The program greets the user:

   ```
   welcome at Aya's Translation Tool
   ```
2. You enter a sentence or word you want to translate.
3. You choose the target language by number.
4. The translated text is displayed instantly.
5. Type `exit` anytime to quit the program.

---

### 💬 Example Output

```
 welcome at Aya's Translation Tool 
 Enter your text (or type 'exit' to quit): Hello, how are you?

Select target language:
1. Arabic
2. English
3. French
4. German
5. Spanish
6. Italian
7. Chinese
8. Japanese

Enter the number of the language: 1

Translated text (Arabic): مرحبًا، كيف حالك؟
```

---

### 🚀 Future Enhancements

* Add GUI interface using **Tkinter** or **PyQt**.
* Add voice input and text-to-speech output.
* Support for saving translation history to a file.

---

### 👩‍💻 Author

**Aya Eslam**
📍 Egyptian Chinese University — Faculty of Computers and Information
💡 Interested in AI, software development, and creative tech tools.
