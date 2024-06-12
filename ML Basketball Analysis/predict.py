import os
from ultralytics import YOLO
import cv2
from flask import Flask, render_template
import threading
import webbrowser

# Video processing
VIDEOS_DIR = os.path.join('.', 'videos')
video_path = os.path.join(VIDEOS_DIR, 'clip4.MOV')
video_path_out = '{}_out.mp4'.format(video_path)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), 20, (W, H))

model_path = os.path.join('.', 'models/the_best.pt')

# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.75
shot_attempted = False
ball_in_goal = False
goal_bottom_y = None
goal_top_y = None
goal_left_x = None
goal_right_x = None
shots_made = 0
shots_attempted = 0
previous_ball_y = None
shot_tracking = False

while ret:
    results = model(frame)[0]

    ball_position = None

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            if results.names[int(class_id)].lower() == 'basketball':
                ball_position = (int((x1 + x2) / 2), int((y1 + y2) / 2))
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, 'BALL', (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            elif results.names[int(class_id)].lower() == 'goal':  # Assuming 'goal' is the class name for the hoop
                goal_bottom_y = int(y2)
                goal_top_y = int(y1)
                goal_left_x = int(x1)
                goal_right_x = int(x2)
                cv2.rectangle(frame, (goal_left_x, goal_top_y), (goal_right_x, goal_bottom_y), (255, 0, 0), 4)
                cv2.putText(frame, 'GOAL', (goal_left_x, goal_top_y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 0, 0), 3, cv2.LINE_AA)

    if ball_position and goal_bottom_y and goal_top_y and goal_left_x and goal_right_x:
        ball_x, ball_y = ball_position

        if ball_y < goal_top_y:
            shot_tracking = True

        if shot_tracking:
            if ball_y > goal_bottom_y:
                if goal_left_x <= ball_x <= goal_right_x:
                    ball_in_goal = True
                shot_attempted = True
                shot_tracking = False

        if shot_attempted:
            if ball_in_goal:
                shots_made += 1
                shots_attempted += 1
            else:
                shots_attempted += 1
            shot_attempted = False
            ball_in_goal = False

        previous_ball_y = ball_y

    out.write(frame)
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()

# Flask app
app = Flask(__name__)

@app.route('/')
def index():
    field_goal_percentage = (shots_made / shots_attempted * 100) if shots_attempted > 0 else 0
    return render_template('analysis_page.html', shots_attempted=shots_attempted,
                           shots_made=shots_made,
                           field_goal_percentage=round(field_goal_percentage, 2))

def run_app():
    webbrowser.open('http://127.0.0.1:5000')
    app.run()

if __name__ == '__main__':
    threading.Thread(target=run_app).start()
