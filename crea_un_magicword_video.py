import cv2
from ascii_magic import AsciiArt
from PIL import Image

cap = cv2.VideoCapture(PERFECT_NOTHING_ANIMATION_MEME.mp4)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break


    frame_count += 1
    if frame_count % 4 == 0:
        frame_rgb = cv2.cvtColor(frame,
                                 cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)
        frame = AsciiArt.from_pillow_image(pil_image)
        frame.to_terminal()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()