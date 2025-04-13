import time
import cv2
import numpy as np
from camera_input import analyze_facial_emotion
import keyboard


if __name__ == "__main__":
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open camera")
    analyses: list[dict[str, np.float32]] = []
    input('Press Enter start capturing images, then press any key to stop and average analyses (\"q\" to quit)').strip().lower()
    while True:
        try:
            analysis = analyze_facial_emotion(cap, "data/captured_image.jpg")
        except Exception as e:
            print(f"Error analyzing facial emotion: {e}")
            continue
        print("Captured image and analyzed emotions:")
        print("\t" + "\n\t".join([f"{k}: {v:.2f}" for k, v in analysis.items()]))
        analyses.append(analysis)
        start_time = time.time()
        key_pressed = False
        while time.time() - start_time < 1:
            if keyboard.is_pressed('space'):
                key_pressed = True
                break
        if key_pressed:
            break
    # Compute average of all analyses dicts
    avg_analysis = {}
    for key in analyses[0]:
        avg_analysis[key] = sum(d[key] for d in analyses) / len(analyses)
    print("Average analysis:")
    for key, value in avg_analysis.items():
        print(f"\t{key}: {value:.2f}")
    cv2.destroyAllWindows()
    cap.release()
