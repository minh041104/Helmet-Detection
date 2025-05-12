import cv2
import tempfile
from PIL import Image, ImageDraw
import numpy as np

def process_video(video_path, model):
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    temp_output = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
    out = cv2.VideoWriter(temp_output.name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_img_file:
            pil_img.save(temp_img_file.name)
            preds = model.predict(temp_img_file.name, confidence=0.2, overlap=30).json()

        draw = ImageDraw.Draw(pil_img)
        for pred in preds["predictions"]:
            x, y = pred["x"], pred["y"]
            w, h = pred["width"], pred["height"]
            label = pred["class"]
            conf = pred["confidence"]
            x1, y1 = x - w / 2, y - h / 2
            x2, y2 = x + w / 2, y + h / 2
            color = "green" if label == "helmet" else "red"
            draw.rectangle([x1, y1, x2, y2], outline=color, width=3)
            draw.text((x1, y1 - 10), f"{label} {conf:.2f}", fill=color)

        processed_frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
        out.write(processed_frame)

    cap.release()
    out.release()
    return temp_output.name
