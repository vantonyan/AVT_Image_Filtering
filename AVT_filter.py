import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) == 1:
    print("Please include picture file name") 
    print("uasage: c\>"+ str(sys.argv[0]) + "image.jpg 0 1") 
    print("0 above is invert (default is 1) and 1 is for reverse AVT (default is 0") 
    sys.exit()

# print("This is the name of the program:", 
#        sys.argv[0]) 
# print("Number of elements including the name of the program:", 
#        len(sys.argv)) 
# print("Number of elements excluding the name of the program:", 
#       (len(sys.argv)-1)) 
# print("Argument List:", 
#        str(sys.argv)) 
# 

img_file = sys.argv[1]
img = cv2.imread(img_file, cv2.IMREAD_COLOR)           # rgb
#invert the image

#if (len(sys.argv) > 2):
#    if (int(sys.argv[2]) == 1):
#        img = 255 - img
#
##alpha_img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED) # rgba
##gray_img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)  # grayscale
#
#print (type(img))
#print ('RGB shape: ', img.shape)        # Rows, cols, channels
##print ('ARGB shape:', alpha_img.shape)
##print ('Gray shape:', gray_img.shape)
##print ('img.dtype: ', img.dtype)
##print ('img.size: ', img.size)
#
#print(img[45,90])

def avt(img, reverse):
        med = np.median(img)
        sd = np.std(img)
        # print(med, sd)
        if reverse == 1:
            print("One")
            return np.where((img>med + sd) | (img<med - sd) , 0, img)
        else:
            print("Zero")
            return np.where((img>med + sd) | (img<med - sd) , img, 0)

options = [[0, 0], [0, 1], [1, 0], [1, 1]]
for i in range(0, 4, 1):
    if options[i][0] == 1:
        img_n = 255 - img
    else:
        img_n = img


    # Split and Create Blue, green and Red component of the image
    img_b, img_g, img_r = cv2.split(img_n)

    # Apply AVT filter
    # Find out Median and standard deviation
    if options[i][1] == 1:
        rev = 1
    else:        
        rev = 0


    filt_r = avt(img_r, rev)
    filt_g = avt(img_g, rev)
    filt_b = avt(img_b, rev)

    # Combine the RGB Channels
    filt_img = cv2.merge((filt_b, filt_g, filt_r))


    # Save image as JPG
    cv2.imwrite(str("Filt_" + str(options[i][0]) + str(options[i][1]) ) + sys.argv[1], filt_img)

#plt.imshow(img, cmap ='Greens')
#plt.show()

#plt.imshow(alpha_img, cmap ='Greens')
#plt.show()

#plt.imshow(gray_img, cmap ='Greens')
#plt.show()

#plt.imshow(filt_img, cmap ='Greens')
#plt.show()



