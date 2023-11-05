import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("Python Webcam Screenshot App")

img_counter = 0
img_dir_path = "website/static/"
# img_file_path = img_dir_path + marker + '_' + str(file_num) + '.png'

while True:
    ret, frame = cam.read()
    
    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("test", frame)
    
    k = cv2.waitKey(1)
    
    if k % 256 == 27: # Decimal value of ESC key
        print("Exit")
        break
    elif k % 256 == 32: # Decimal value of SPACE key
        img_name = 'opencv_frame_{}.png'.format(img_counter)
        img_file_path = img_dir_path + img_name
        cv2.imwrite(img_file_path, frame)
        print("Screenshot taken")
        img_counter += 1
        
cam.release()
cv2.destroyAllWindows()
