from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
# ... (include your face_recognition logic from the previous reply)

app = Flask(__name__)

# 1. Main Dashboard
@app.route('/')
def index():
    return render_template('index.html')

# 2. The Video Feed for the "Mark Attendance" screen
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# 3. Handle Registration Form Submission
@app.route('/register_student', methods=['POST'])
def register_student():
    name = request.form.get('name')
    roll = request.form.get('roll')
    # Here you would trigger the camera to save the photo
    # and save details to your MySQL database
    print(f"Registering: {name}, {roll}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
