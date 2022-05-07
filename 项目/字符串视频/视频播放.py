import cv2
from IPython.display import clear_output, Image, display

def show_video(video_path, show_text=''):
    video = cv2.VideoCapture(video_path)

    while True:
        try:
            clear_output(wait=True)
            # 读取视频
            ret, frame = video.read()
            if not ret:
                break
            height, width, _ = frame.shape
            cv2.putText(frame, show_text, (0, 100), cv2.FONT_HERSHEY_TRIPLEX, 3.65, (255, 0, 0), 2)
            frame = cv2.resize(frame, (int(width / 2), int(height / 2)))
            _, ret = cv2.imencode('.jpg', frame)
            display(Image(data=ret))
        except KeyboardInterrupt:
            video.release()
            
#视频路径
show_video('video/output.avi')