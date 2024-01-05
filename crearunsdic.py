import cv2
from ascii_magic import AsciiArt
from PIL import Image

cap = cv2.VideoCapture('VID-20231027-WA0016.mp4')
frame_count = 0


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % 8 == 0:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame_rgb)
        ascii_frame = AsciiArt.from_pillow_image(pil_image)
        ascii_frame.to_terminal()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

with open('ascii_art_animation.txt', 'w') as f:
    f.write('\n'.join(ascii_frame))