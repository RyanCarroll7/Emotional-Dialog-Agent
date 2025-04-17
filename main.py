import time
import cv2
from camera_input import analyze_facial_emotion
import keyboard
from improv_partner import ImprovPartner


def run_face_analysis():
    analyses = []
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
            if keyboard.is_pressed("space"):
                key_pressed = True
                break
        if key_pressed:
            break
    return analyses

if __name__ == "__main__":
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open camera")
    partner = ImprovPartner(
        "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"
    )
    while True:
        dialog = input(
            "Type your dialog and press Enter to start capturing images. Type 'q' to quit.\nDialog: "
        ).strip()
        if dialog.lower() == "q":
            break
        analyses = run_face_analysis()
        # Compute average of all analyses dicts
        avg_analysis = {}
        for key in analyses[0]:
            avg_analysis[key] = sum(d[key] for d in analyses) / len(analyses)
        print("Average analysis:")
        for key, value in avg_analysis.items():
            print(f"\t{key}: {value:.2f}")
        emotion = max(avg_analysis, key=avg_analysis.get)
        print(
            "Improv Partner response:",
            partner.get_next_improv_response(dialog, emotion),
        )
    cap.release()
