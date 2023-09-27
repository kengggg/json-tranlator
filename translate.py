import json
import time
from google.cloud import translate_v2 as translate

# Require export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials.json" to be set in the terminal
def translate_json(input_file, output_file, source_lang, target_lang):
    # Initialize the translator
    translator = translate.Client()

    # Load the JSON file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Translate the values
    translated_data = {}
    item_counter = 0
    for key, value in data.items():
        translation = translator.translate(value, source_language=source_lang, target_language=target_lang)
        translated_data[key] = translation['translatedText']
        item_counter += 1
        print("{} Translated {}: {} ➡️ {}".format(item_counter, key, value, translated_data[key]))
    
        # Pause for a short duration (e.g., 1 second) between translations to avoid hitting rate limits
        time.sleep(1)

    # Write the translated content to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(translated_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    input_filename = "mobile-en.json"
    output_filename = "mobile-mm.json"
    translate_json(input_filename, output_filename, 'en', 'my')
