from openai import OpenAI
from pydantic import BaseModel

system_prompt = f"""You are part of an emotional dialogue agent.
    Your job is to classify the given facial expression data and message into one of Ekman's Universal Emotions.
    These emotions are: Anger, Contempt, Disgust, Fear, Happiness, Sadness, and Surprise.
    The expression data is a dictionary mapping the above emotions to floats representing the intensity of each emotion, ranging from 0 to 1.
    """


class EmotionClassification(BaseModel):
    emotion: str
    explanation: str


def classify_input(expression_data: dict[str, float], message: str, context: str):
    prompt = f"""
    Expression Data: {expression_data}
    Message: {message}
    Context: {context}
    Based on the expression data, message, and context, classify the input into one of the following emotions: Anger, Contempt, Disgust, Fear, Happiness, Sadness, or Surprise.
    Provide a brief explanation for your classification.
    """
    openai = OpenAI(api_key="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")
    response = openai.beta.chat.completions.parse(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        model="gpt-4o-mini",
        response_format=EmotionClassification
    )
    return response.choices[0].message.parsed
