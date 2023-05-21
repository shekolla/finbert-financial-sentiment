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


def sentiment_analysis(text):
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

iface = gr.Interface(
    fn=sentiment_analysis, 
    inputs="text", 
    outputs="text", 
    title="Financial Sentiment Analysis",
    description="<p>A sentiment analysis model fine-tuned on financial news.</p>"
                "<p>Enter some financial text to see whether the sentiment is positive, neutral or negative.</p>"
                "<p><strong>Note:</strong> Separate multiple sentences with a '|'.",
)
iface.launch()


# commented to improve Gradio UI further

# import gradio as gr
# from transformers import pipeline

# def sentiment_analysis(text):
#     # Define the model
#     model_name = "yiyanghkust/finbert-tone"
#     # Create the pipeline
#     nlp = pipeline("sentiment-analysis", model=model_name)
#     # Split the input text into individual sentences
#     sentences = text.split('|')
#     # Run the pipeline on each sentence and collect the results
#     results = []
#     for sentence in sentences:
#         result = nlp(sentence.strip())[0]
#         results.append({
#             'Text': sentence.strip(),
#             'Sentiment': result['label'],
#             'Score': f"{result['score']:.4f}"
#         })
#     return results

# # Create a custom HTML template for the Gradio interface
# html_template = """
# <div style="padding: 20px; font-family: Arial;">
#   <h2 style="text-align: center;">Financial Sentiment Analysis</h2>
#   <hr>
#   <p><strong>Input Text:</strong> {text}</p>
#   <p><strong>Sentiment:</strong> {sentiment}</p>
#   <p><strong>Score:</strong> {score}</p>
# </div>
# """

# iface = gr.Interface(
#     fn=sentiment_analysis, 
#     inputs="text", 
#     outputs="text", 
#     title="Financial Sentiment Analysis",
#     description="Enter some financial text to see whether the sentiment is positive, neutral, or negative. Separate multiple sentences with a '|'.",
#     examples=[["This is a positive statement."], ["This is a negative statement."]],
#     allow_flagging=False,
#     thumbnail="emotion-recognition.png",
#     theme="default",
#     template=html_template,
# )
# gr.HTML(html_template)
# iface.launch()


