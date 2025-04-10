from random import random

import cv2
from camera_input import analyze_facial_emotion
from input_classifier import classify_input


if __name__ == "__main__":
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open camera")
    while input("Press Enter to capture an image (\"n\" to quit)").strip().lower() != "n":
        try: 
            analysis = analyze_facial_emotion(cap, "captured_image.jpg")
        except Exception as e:
            print(f"Error analyzing facial emotion: {e}")
            continue
        print("Captured image and analyzed emotions:")
        print('\t' + '\n\t'.join([f"{k}: {v:.2f}" for k, v in analysis.items()]))

