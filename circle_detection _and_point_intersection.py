'''
Created by Aman Rastogi on 26/06/2022
Task - To detect circles in an image and finding whether a given point lies inside the circle
or not.

'''

# import relevant libraries
import cv2
import numpy as np
import sys

# function to find whether point is inside circle or not

def isInside(center_x, center_y, radius, x, y):
    # Compare radius of circle
    # with distance of its center
    # from given point
    if ((x - center_x) * (x - center_x) +
        (y - center_y) * (y - center_y) <= radius * radius):
        return "Point ({0},{1}) is inside circle".format(x,y)
    else:
        return "Point ({0},{1}) is NOT inside circle".format(x,y)

def main(argv):
    # checking for number of args
    if len(argv) > 1:
        filename = argv[0]
        point_x,point_y = map(int,sys.argv[2].split(','))
    else:
        print("Please enter filename and pointx,pointy as arguments !")
        exit()
    
    # Loads an image
    src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
    
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        return -1

    # checking for a valid point
    if point_x > src.shape[0] or point_y > src.shape[1]:
        print("Selected point is outside the image. Your Image dimension is",src.shape)
        exit()
    
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    rows = gray.shape[0]
    
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows,
                               param1=50, param2=1,
                               minRadius=0, maxRadius=0)
   
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(src, center, radius, (0, 0, 255), 3)
            # plot point on image
            cv2.circle(src, (point_x,point_y), 1, (0, 255, 255), 2)

            print(isInside(center[0], center[1], radius, point_x,point_y))
    
    cv2.imshow("detected circles", src)
    cv2.waitKey(0)
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
