from deep_translator import GoogleTranslator

# Supported languages
LANGUAGES = {
    "Arabic": "ar",
    "English": "en",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Chinese": "zh-CN",
    "Japanese": "ja"
}

def translate_text(text, target_lang):
    return GoogleTranslator(source='auto', target=LANGUAGES[target_lang]).translate(text)

def main():
    while True:
        text = input(" welcome at Aya's Translatian Tool \n Enter your text (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            break

        print("\nSelect target language:")
        for i, lang in enumerate(LANGUAGES.keys(), 1):
            print(f"{i}. {lang}")

        try:
            choice = int(input("\nEnter the number of the language: "))
            target_lang = list(LANGUAGES.keys())[choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Try again.")
            continue

        translated = translate_text(text, target_lang)
        print(f"\nTranslated text ({target_lang}): {translated}\n")

if __name__ == "__main__":
    main()

