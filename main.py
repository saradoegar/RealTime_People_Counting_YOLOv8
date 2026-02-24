import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera not accessible")
    exit()

zones = [
    (50, 100, 300, 350),
    (350, 150, 600, 400)
]

cx, cy = 320, 240  # Start from center (so red dot visible immediately)

def mouse_move(event, x, y, flags, param):
    global cx, cy
    if event == cv2.EVENT_MOUSEMOVE:
        cx, cy = x, y

def is_inside_zone(x, y, zone):
    x1, y1, x2, y2 = zone
    return x1 < x < x2 and y1 < y < y2

cv2.namedWindow("Camera Feed")
cv2.setMouseCallback("Camera Feed", mouse_move)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 🔴 Draw red dot
    cv2.circle(frame, (cx, cy), 6, (0, 0, 255), -1)

    for i, zone in enumerate(zones):
        x1, y1, x2, y2 = zone
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # If inside zone
        if is_inside_zone(cx, cy, zone):
            cv2.putText(frame, f"Inside Zone {i+1}", (50, 70 + i*30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()