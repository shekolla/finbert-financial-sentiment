import gradio as gr
from transformers import pipeline


# Code Comment: Sentiment Analysis Model Selection

'''
When performing sentiment analysis on financial text, we have two model options to consider: `finBERT-tone` and `distilroberta-finetuned-financial-news-sentiment-analysis`. 

- `finBERT-tone`: This model is specifically trained to identify seven tones (joy, fear, anger, sadness, analytical, confident, tentative) in financial text. It provides detailed insights into the emotional tone of the text, which can be valuable for sentiment analysis in specific contexts. It offers higher granularity, but it comes with a larger model size.

- `distilroberta-finetuned-financial-news-sentiment-analysis`: This model is based on DistilRoBERTa, a smaller and faster variant of RoBERTa. It is fine-tuned for sentiment analysis on financial news. This model strikes a good balance between model size and performance, offering a more compact option with lower resource requirements. Although it may not provide the same level of granularity as `finBERT-tone`, it still delivers reliable sentiment analysis results for financial text.

To ensure the best results, it is recommended to use `finBERT-tone` for sentiment analysis on financial text whenever possible. However, if size and resource constraints are a concern, or if a detailed emotional tone analysis is not required, you can fallback to `distilroberta-finetuned-financial-news-sentiment-analysis` as a reliable backup. It provides a smaller model size without sacrificing too much accuracy, making it a suitable alternative.

Keep in mind that both models have their strengths and trade-offs. Assess your specific requirements, available resources, and desired level of analysis to choose the most appropriate model for your sentiment analysis tasks.
'''

# End of Code Comment


def sentiment_analysis_generate_text(text):
    # Define the model
    model_name = "yiyanghkust/finbert-tone"

    # for faster, less model size use this model
    # model_name = "mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis"

    # Create the pipeline
    nlp = pipeline("sentiment-analysis", model=model_name)
    # Split the input text into individual sentences
    sentences = text.split('|')
    # Run the pipeline on each sentence and collect the results
    results = nlp(sentences)
    output = []
    for sentence, result in zip(sentences, results):
        output.append(f"Text: {sentence.strip()}\nSentiment: {result['label']}, Score: {result['score']:.4f}\n")

    # Join the results into a single string to return
    return "\n".join(output)


def sentiment_analysis_generate_table(text):
    # Define the model
    model_name = "yiyanghkust/finbert-tone"
    # Create the pipeline
    nlp = pipeline("sentiment-analysis", model=model_name)
    # Split the input text into individual sentences
    sentences = text.split('|')

    # Generate the HTML table with enhanced colors and bold headers
    html = """
    <html>
    <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/css/bootstrap.min.css">
    <style>
    .label {
        transition: .15s;
        border-radius: 8px;
        padding: 5px 10px;
        font-size: 14px;
        text-transform: uppercase;
    }
    .positive {
        background-color: rgb(54, 176, 75);
        color: white;
    }
    .negative {
        background-color: rgb(237, 83, 80);
        color: white;
    }
    .neutral {
        background-color: rgb(52, 152, 219);
        color: white;
    }
    th {
        font-weight: bold;
        color: rgb(106, 38, 198);
    }
    </style>
    </head>
    <body>
    <table class="table table-striped">
    <thead>
        <tr>
            <th scope="col">Text</th>
            <th scope="col">Score</th>
            <th scope="col">Sentiment</th>
        </tr>
    </thead>
    <tbody>
    """
    for sentence in sentences:
        result = nlp(sentence.strip())[0]
        text = sentence.strip()
        score = f"{result['score']:.4f}"
        sentiment = result['label']

        # Determine the sentiment class
        if sentiment == "Positive":
            sentiment_class = "positive"
        elif sentiment == "Negative":
            sentiment_class = "negative"
        else:
            sentiment_class = "neutral"

        # Generate table rows
        html += f'<tr><td>{text}</td><td>{score}</td><td><span class="label {sentiment_class}">{sentiment}</span></td></tr>'

    html += """
    </tbody>
    </table>
    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    # uncomment below code for using the code in text results
    # iface = gr.Interface(
    #     fn=sentiment_analysis_generate_text, 
    #     inputs="text", 
    #     outputs="text", 
    #     title="Financial Sentiment Analysis",
    #     description="<p>A sentiment analysis model fine-tuned on financial news.</p>"
    #                 "<p>Enter some financial text to see whether the sentiment is positive, neutral or negative.</p>"
    #                 "<p><strong>Note:</strong> Separate multiple sentences with a '|'.",
    #     )

    # generate the result in html format
    iface = gr.Interface(
        sentiment_analysis_generate_table,
        gr.Textbox(placeholder="Enter sentence here..."),
        ["html"],
        title="Financial Sentiment Analysis",
        description="<p>A sentiment analysis model fine-tuned on financial news.</p>"
                    "<p>Enter some financial text to see whether the sentiment is positive, neutral or negative.</p>"
                    "<p><strong>Note:</strong> Separate multiple sentences with a '|'.",
        examples=[
            ['growth is strong and we have plenty of liquidity.'],
            ['there is a shortage of capital, and we need extra financing.'],
            ['formulation patents might protect Vasotec to a limited extent.'],
            ["growth is strong and we have plenty of liquidity.|there is a shortage of capital"]
        ],
        allow_flagging=False,
        examples_per_page=2,
    )

    iface.launch()    