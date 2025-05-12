import gradio as gr
from utils.config_loader import load_config
from utils.roboflow_model import init_model
from utils.image_utils import process_image
from utils.video_utils import process_video

config = load_config()
model = init_model(config)

with gr.Blocks() as demo:
    gr.Markdown("## 🪖 Helmet Detection for Image and Video")

    with gr.Tab("🖼️ Image"):
        with gr.Row():
            image_input = gr.Image(label="Upload Image")
            image_output = gr.Image(label="Detected Image")
        image_button = gr.Button("Detect Helmet (Image)")
        image_button.click(fn=lambda img: process_image(img, model), inputs=image_input, outputs=image_output)

    with gr.Tab("🎥 Video"):
        with gr.Row():
            video_input = gr.Video(label="Upload Video")
            video_output = gr.Video(label="Detected Video")
        video_button = gr.Button("Detect Helmet (Video)")
        video_button.click(fn=lambda vid: process_video(vid, model), inputs=video_input, outputs=video_output)

demo.launch()
