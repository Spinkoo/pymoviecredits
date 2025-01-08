import cv2
import numpy as np
from data_reader import read_credits_static, read_credits_from_excel, read_credits_from_csv

CREDIT_TYPE = "excel"


def create_credits_video(credits_dict, output_file, video_size=(720, 1280), fps=30, duration_per_line=1, bg_color=(0, 0, 0), text_color=(255, 255, 255), font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, thickness=2):
    """
    Creates a rolling credits video using OpenCV.
    
    Args:
        credits_dict (dict): A dictionary where keys are titles (e.g., "Director") and values are names or roles.
        output_file (str): Output file path for the video (e.g., "credits.mp4").
        video_size (tuple): Width and height of the video in pixels.
        fps (int): Frames per second.
        duration_per_line (int): Duration (in seconds) each line is visible while scrolling.
        bg_color (tuple): Background color in BGR.
        text_color (tuple): Text color in BGR.
        font: OpenCV font type.
        font_scale (float): Font scale.
        thickness (int): Thickness of the text.
    """
    # Calculate total duration
    line_height = 100  # Approximate line height in pixels
    total_lines = len(credits_dict.values())  # Include titles
    total_duration = total_lines * duration_per_line
    total_frames = int(fps * total_duration)
    
    # Create a tall canvas for the credits
    credits_height = total_lines * line_height + 2 * video_size[1]  # Extra space for smooth scrolling
    credits_image = np.zeros((credits_height + video_size[1], video_size[0], 3), dtype=np.uint8)
    credits_image[:] = bg_color  # Set background color
    # Write credits text onto the canvas
    y_offset = video_size[1]  # Start offscreen
    for title, name in credits_dict.items():
        cv2.putText(credits_image, f'{title} : {name}' if len(name) > 0 else title, (0 if len(name) > 0 else 500 - len(title) // 2 * 20 * font_scale, y_offset), font, font_scale, text_color, thickness)
        y_offset += line_height
    


    # Initialize video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'mp4v' for MP4 output
    out = cv2.VideoWriter(output_file, fourcc, fps, video_size)

    # Scroll the credits
    for frame_idx in range(total_frames):
        scroll_offset = int((frame_idx / total_frames) * video_size[1])
        frame_start = max(0, scroll_offset)
        frame_start = frame_idx
        frame_end = frame_start + video_size[1]
        frame = credits_image[frame_start:frame_end, :video_size[0]]
        out.write(frame)

    out.release()
    print(f"Video saved as {output_file}")

if __name__ == "__main__":
    
    if CREDIT_TYPE == "static":
        credits = read_credits_static()
    elif CREDIT_TYPE == "excel":
        credits = read_credits_from_excel("credits.xlsx")
    elif CREDIT_TYPE == "csv":
        credits = read_credits_from_csv("credits.csv")
    else:
        raise ValueError(f"Invalid credit type: {CREDIT_TYPE}")
    create_credits_video(
        credits_dict=credits,
        output_file="credits.mp4",
        video_size=(1080, 1280),
        fps=100,
        duration_per_line=2,
        bg_color=(0, 0, 0),
        text_color=(255, 255, 255),
        font=cv2.FONT_HERSHEY_COMPLEX,
        font_scale=1,
        thickness=2
    )
