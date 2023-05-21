# Financial Sentiment Analysis

Welcome to the Financial Sentiment Analysis project! This project aims to provide sentiment analysis on financial text data, helping to determine the sentiment (positive, negative, or neutral) in the context of financial news.

## Overview

Financial Sentiment Analysis is performed using state-of-the-art models that have been fine-tuned specifically for financial text. The models used in this project include:
- **finBERT-tone**: This model offers sentiment analysis along with detailed emotional tone analysis, identifying seven tones (joy, fear, anger, sadness, analytical, confident, tentative) in financial text. It provides a deeper understanding of the emotional context but has a larger model size.
- **distilroberta-finetuned-financial-news-sentiment-analysis**: This model is a more compact alternative, based on DistilRoBERTa, a smaller and faster variant of RoBERTa. It is fine-tuned for sentiment analysis on financial news, striking a balance between model size and performance.

## Features

- Perform sentiment analysis on financial text data.
- Analyze the sentiment in financial news articles, earnings reports, social media posts, and more.
- Understand the emotional tone of financial text using the `finBERT-tone` model.
- Utilize the `distilroberta-finetuned-financial-news-sentiment-analysis` model as a more lightweight alternative.

## Getting Started

Follow these steps to get started with the Financial Sentiment Analysis project:

1. Clone the repository:

```bash
git clone https://github.com/shekolla/financial-sentiment-analysis.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Choose the appropriate model:
   - If you require detailed emotional tone analysis, use `finBERT-tone`.
   - If model size is a concern or a detailed emotional analysis is not required, use `distilroberta-finetuned-financial-news-sentiment-analysis`.

4. Modify the code to suit your specific use case:
   - Set the model name according to your selected model.
   - Customize the input and output handling as needed.

5. Run the code:
   ```bash
   python sentiment_analysis.py
   ```

## Usage

To analyze the sentiment of financial text, provide the text as input to the appropriate model. The output will be the predicted sentiment (positive, negative, or neutral) along with any additional information provided by the chosen model (such as emotional tone analysis with `finBERT-tone`).

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes with descriptive commit messages.
- Push your changes to your forked repository.
- Submit a pull request, explaining your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

We would like to acknowledge the developers and contributors of the `finBERT-tone` and `distilroberta-finetuned-financial-news-sentiment-analysis` models. Their efforts in training and fine-tuning the models have made this project possible.

If you have any questions or need assistance, please feel free to reach out to us.

Happy sentiment analysis!