import cv2
import numpy as np

# 1. Read and Display an Image
image = cv2.imread('test_img.jpg')
cv2.imshow('Displayed Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Save the grayscale image
cv2.imwrite('grayscale_image.jpg', gray_image)

# 3. Resize an Image
resized_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Draw Shapes on an Image
cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 2)

# Draw a circle
cv2.circle(image, (300, 300), 50, (255, 0, 0), 3)

# Draw a line
cv2.line(image, (100, 100), (400, 400), (0, 0, 255), 2)

# Display the image with shapes
cv2.imshow('Shapes on Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. Crop an Image
# Crop a region of the image
cropped_image = image[50:200, 50:200]
# Display the cropped image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. Save an Image
# cv2.imwrite('grayscale_image.jpg', gray_image)

# 7. Drawing Text on an Image
# Add text to the image
cv2.putText(image, 'OpenCV Demo', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Display the image with text
cv2.imshow('Text on Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 8. Edge Detection (Canny)
# Perform edge detection
edges = cv2.Canny(image, 100, 200)
# Display the edges
cv2.imshow('Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 9. Gaussian Blur
# Apply Gaussian Blur to smooth the image
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Display the blurred image
cv2.imshow('Gaussian Blur', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 10. Image Thresholding
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display the thresholded image
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 11. Detecting Contours
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, binary = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
image_with_contours = image.copy()
cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)

# Display the image with contours
cv2.imshow('Contours', image_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 12. Image Blending
# Create a second image (same size as original)
overlay = image.copy()

# Add a semi-transparent red rectangle to the overlay
cv2.rectangle(overlay, (50, 50), (300, 300), (0, 0, 255), -1)

# Blend the images with a transparency factor
blended_image = cv2.addWeighted(image, 0.7, overlay, 0.3, 0)

# Display the blended image
cv2.imshow('Blended Image', blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 13. Image Translation
# Define the translation matrix
M = np.float32([[1, 0, 100], [0, 1, 50]])

# Apply the translation
translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

# Display the translated image
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 14. Image Rotation
# Define the rotation matrix
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)  # Rotate 45 degrees

# Apply the rotation
rotated_image = cv2.warpAffine(image, M, (w, h))

# Display the rotated image
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 15. Perspective Transformation
# Define points for the perspective transform
pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250], [300, 200]])

# Get the transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply the transformation
warped_image = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))

# Display the warped image
cv2.imshow('Warped Image', warped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 16. Image Erosion and Dilation
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding
_, binary = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Define a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(binary, kernel, iterations=1)

# Apply dilation
dilated_image = cv2.dilate(binary, kernel, iterations=1)

# Display results
cv2.imshow('Original Binary', binary)
cv2.imshow('Eroded Image', eroded_image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 17. Detecting Corners with Harris Corner Detection
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert to float32
gray_float = np.float32(gray_image)

# Apply Harris Corner Detection
corners = cv2.cornerHarris(gray_float, 2, 3, 0.04)

# Mark corners on the image
image[corners > 0.01 * corners.max()] = [0, 0, 255]

# Display the image with corners
cv2.imshow('Harris Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 18. Detecting Lines with Hough Transform
# Convert to grayscale and apply edge detection
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 50, 150)

# Detect lines using Hough Transform
lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

# Draw lines on the image
for rho, theta in lines[:, 0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the image with lines
cv2.imshow('Hough Lines', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 19. Histogram Equalization
# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Equalize the histogram
equalized_image = cv2.equalizeHist(gray_image)

# Display the results
cv2.imshow('Original Grayscale', gray_image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 20. Background Subtraction
# Initialize the background subtractor
background_subtractor = cv2.createBackgroundSubtractorMOG2()

# Read video frames (replace 'video.mp4' with your video file)
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fg_mask = background_subtractor.apply(frame)

    # Display the result
    cv2.imshow('Foreground Mask', fg_mask)
    if cv2.waitKey(30) & 0xFF == 27:  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()

# 21. Template Matching
# Load template and original image
template = cv2.imread('grayscale_image.jpg', 0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply template matching
result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# Draw rectangle around the detected area
top_left = max_loc
h, w = template.shape
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

# Display the result
cv2.imshow('Template Matching', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 22. Face Detection using Haar Cascade
# Load the Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the result
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 23. Splitting and Merging Channels
# Split the image into B, G, R channels
b, g, r = cv2.split(image)

# Merge the channels with modified order
merged_image = cv2.merge((r, g, b))  # Example: Swap red and blue

# Display the results
cv2.imshow('Original', image)
cv2.imshow('Modified Channels', merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
