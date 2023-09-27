# JSON value translator

This is a basic Python script for translating JSON values from one language to another language using Google Translate API. It is useful for translating JSON files that contain a lot of values.

It is still messy, but it works.

# Usage

Be a good Python citizen and create a virtual environment first:

```bash
python3 -m venv json-translator
cd json-translator
source json-translator/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Make the Google Translate API credentials available to the script:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
```

Run the script:

```bash
python3 translate.py
```
