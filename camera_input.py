from deepface import DeepFace
import cv2
import numpy as np


def analyze_facial_emotion(cap: cv2.VideoCapture, filename: str) -> dict[str, np.float32]:
    # If the camera is not opened, raise an error
    if not cap.isOpened():
        raise IOError("Cannot open camera")
    # Capture the image (twice ensures we get an unbuffered frame)
    cap.read()
    captured, image = cap.read()
    # Check if image is captured correctly
    if not captured:
        raise IOError("Cannot capture image")
    # Save the captured image to the specified filename
    cv2.imwrite(filename, image)
    # Analyze the image using DeepFace
    analysis = DeepFace.analyze(filename, ("emotion"), align=False)
    return analysis[0]["emotion"]
