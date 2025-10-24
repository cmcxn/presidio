# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Installation

```bash
# Run installation script
./install.sh

# Or manual installation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download zh_core_web_sm
pip install -e .
```

### Running Demos

```bash
# Run simple demo
python demo_simple.py

# Run complete demonstration
python main.py
```

## Architecture Overview

### Core Components
- `chinese_anonymizer/` - Main package containing:
  - `person_recognizer.py`: Chinese name recognition using common surname patterns
  - `phone_recognizer.py`: Chinese phone number recognition using regex patterns
  - `anonymizer.py`: Main anonymization engine integration with Presidio

### Entry Points
- `demo_simple.py`: Basic demonstration script showing anonymization workflow
- `main.py`: Complete demonstration with multiple test cases

### Technical Stack
- Built on Microsoft Presidio framework (`presidio-analyzer` and `presidio-anonymizer`)
- Uses spaCy Chinese language model (`zh_core_web_sm`)
- Python 3.8+ compatible

### Project Structure
```
presidio/
├── chinese_anonymizer/
│   ├── __init__.py
│   ├── anonymizer.py
│   ├── person_recognizer.py
│   └── phone_recognizer.py
├── main.py
├── demo_simple.py
├── install.sh
├── requirements.txt
└── setup.py
```

## Important Notes
- The project currently lacks a formal test suite - verification is done through demonstration scripts
- Configuration for Chinese-specific recognizers is embedded in the recognizer implementation files