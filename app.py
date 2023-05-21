from sentiment_analysis import sentiment_analysis_generate_table, sentiment_analysis_generate_text
import gradio as gr

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
            ['growth is strong and we have plenty of liquidity.|there is a shortage of capital']
        ],
        allow_flagging=False,
        examples_per_page=2,
    )

    iface.launch()   