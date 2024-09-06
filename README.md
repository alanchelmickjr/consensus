# ERACAI: AI Consensus Live Response Evaluation and Tuning Mechanism for Chat/Completion [![Open Source](https://badges.frapsoft.com/os/v1/open-source.png?v=103)]()
## This is branched off the original framework for the Myriad Engine at https://myriadai.online (PRO version). 
### Below find the first vanilla template I created in Feb24.  Good "starting" place for thoughts. [February 2024 V1.0 Alpha] <- https://github.com/alanchelmickjr/consensus/tree/Vanilla-Template-01-Backup

ERACAI (Ensemble Response through AI Consensus) is a cutting-edge AI system that leverages multiple language models to generate consensus-based responses. By querying various AI models and implementing a majority voting mechanism, ERACAI provides more reliable and balanced answers to user queries.

## Features

- **Multi-Model Querying**: Simultaneously queries OpenAI, Anthropic, Google, and Groq AI models.
- **Consensus Mechanism**: Implements majority voting to determine the best response.
- **Asynchronous Processing**: Utilizes asyncio for efficient parallel processing of model queries.
- **Weaviate Integration**: Stores results in a Weaviate vector database for future reference and analysis.
- **FastAPI Backend**: Provides a robust and fast API interface for easy integration.
- **CLI Tool**: Includes a command-line interface for quick testing and interaction.
  
<div style="width: 400px; max-width: 100%; margin: 0 auto; text-align: center;">
  <img src="https://gp8lfrj7ia0anqai.public.blob.vercel-storage.com/image-75-ApEAC4QKtJaPz3Trq4tQx35GgdL5In.jpg" 
       style="width: 400px; max-width: 100%; height: auto; display: block; margin: 0 auto;">
</div>

## Installation

1. Clone the repository:
   git clone https://github.com/yourusername/eracai.git cd eracai

2. Install the package:
   pip install -e .

3. Set up your environment variables by copying the '.env.example' file to '.env' and filling in your API keys:
   cp .env.example .env

## Usage

### As a Python Package

```python
from eracai.main import consensus_response

async def main():
    result = await consensus_response("Who is the hottest actress this year?")
    print(result.content)

asyncio.run(main())
```

### API

Start the FastAPI server:

```
uvicorn eracai.api:app --reload
```

Then, you can send POST requests to 'http://localhost:8000/query' with a JSON body:

```json
{
  "text": "Who is the hottest actress this year?",
  "max_tokens": 100,
  "temperature": 0.7
}
```

### CLI

```
eracai query "Who is the hottest actress this year?"
```

## Configuration

Adjust the settings in your '.env' file to configure API keys, model parameters, and Weaviate connection details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://www.openai.com/)
- [Anthropic](https://www.anthropic.com/)
- [Google AI](https://ai.google/)
- [Groq](https://groq.com/)
- [Weaviate](https://weaviate.io/)
