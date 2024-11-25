
from moviepy.editor import VideoFileClip, CompositeVideoClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Load the video file
base_video = VideoFileClip("final.mp4")


def create_text_image(text, font_size=50, width=1920, height=100, text_color=(255, 255, 0)):
    # Create a transparent image
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    
    
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", font_size)  # Use any font you like
    
    
    bbox = draw.textbbox((0, 0), text, font=font)  
    text_width = bbox[2] - bbox[0]  
    text_height = bbox[3] - bbox[1]  
    position = ((width - text_width) // 2, (height - text_height) // 2)  # Center position
    
    # Draw the text
    draw.text(position, text, font=font, fill=text_color)  

    
    return np.array(img)


text_image = create_text_image("This is a text overlay!", font_size=50, text_color=(255, 255, 0))


from moviepy.editor import ImageClip
text_clip = ImageClip(text_image)



text_clip = text_clip.set_duration(base_video.duration).set_position("center")


final_video = CompositeVideoClip([base_video, text_clip])


final_video.write_videofile("video_with_text_overlay.mp4", fps=24)