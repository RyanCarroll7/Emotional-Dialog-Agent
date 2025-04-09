from input_classifier import classify_input


if __name__ == "__main__":
    # Test classification of same message with different expressions read
    response_a = classify_input(
        {
            "Anger": 0.0,
            "Contempt": 0.0,
            "Disgust": 0.0,
            "Fear": 0.0,
            "Happiness": 0.0,
            "Sadness": 1.0,
            "Surprise": 0.0,
        },
        "I'm not sure what to do right now.",
        "",
    )
    response_b = classify_input(
        {
            "Anger": 1.0,
            "Contempt": 0.0,
            "Disgust": 0.0,
            "Fear": 0.0,
            "Happiness": 0.0,
            "Sadness": 0.0,
            "Surprise": 0.0,
        },
        "I'm not sure what to do right now.",
        "",
    )
    response_c = classify_input(
        {
            "Anger": 0.0,
            "Contempt": 0.0,
            "Disgust": 0.1,
            "Fear": 0.1,
            "Happiness": 0.4,
            "Sadness": 0.0,
            "Surprise": 0.4,
        },
        "I'm not sure what to do right now.",
        "",
    )
    print("Response A:", response_a)
    print("Response B:", response_b)
    print("Response C:", response_c)
