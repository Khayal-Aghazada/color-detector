import cv2
import pandas as pd

# Reading the CSV file with color names and RGB values
index = ["color_name", "R", "G", "B"]
csv = pd.read_csv('C:colors.csv', names=index, header=0)


# Function to calculate the minimum distance from all colors and get the most matching color
def getColorName(R, G, B):
    minimum = 10000
    cname = ""
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d < minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

# Start capturing video from the webcamq
cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Define the center region of interest (ROI)
    center_x, center_y = width // 2, height // 2
    box_size = 100  # Size of the box to detect color
    start_x = center_x - box_size // 2
    start_y = center_y - box_size // 2
    end_x = center_x + box_size // 2
    end_y = center_y + box_size // 2

    # Extract the region of interest (ROI) from the frame
    roi = frame[start_y:end_y, start_x:end_x]

    # Compute the average color of the ROI
    avg_color_per_row = cv2.mean(roi)[:3]
    b, g, r = int(avg_color_per_row[0]), int(avg_color_per_row[1]), int(avg_color_per_row[2])

    # Get the name of the color
    color_name = getColorName(r, g, b)

    # Draw a rectangle around the center region
    cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (255, 255, 255), 2)

    # Display the color name on the frame
    text = f"Detected Color: {color_name}"
    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    # If the color is light, display the text in black
    if r + g + b >= 600:
        cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Real-Time Color Detector', frame)

    # Break the loop when the user hits the 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
