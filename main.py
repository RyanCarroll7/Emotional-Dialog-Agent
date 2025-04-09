from random import random
from input_classifier import classify_input


if __name__ == "__main__":
    # Test classification of same message with different expressions read
    for i in range(5):
        values = [random() for _ in range(7)]
        total = sum(values)
        values = [round(val / total, 2) for val in values]
        expression_data = dict(
            zip(
                [
                    "Anger",
                    "Contempt",
                    "Disgust",
                    "Fear",
                    "Happiness",
                    "Sadness",
                    "Surprise",
                ],
                values,
            )
        )
        response = classify_input(
            expression_data,
            "I'm not sure what to do right now.",
            "",
        )
        print(f"Expression Data: {expression_data}")
        print(f"Response {i + 1}:", response, "\n")
