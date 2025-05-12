from PIL import Image, ImageDraw
import tempfile

def process_image(image, model):
    pil_img = Image.fromarray(image)
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

    return pil_img
