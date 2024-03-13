import numpy as np

def sepia(image):
    sepia_filter = np.array(
        [[0.393, 0.769, 0.189],
         [0.349, 0.686, 0.168],
         [0.272, 0.534, 0.131]]
    )
    sepia_img = image.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img
import gradio as gr

# Write 1 line of Python to create a simple GUI
gr.Interface(fn=sepia, inputs="image", outputs="image").launch();