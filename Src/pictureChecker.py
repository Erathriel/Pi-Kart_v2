import numpy as np
import cv2
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 100

t1 = raw_input("Choisir image 1 : ")
t2 = raw_input("Choisir image 2 : ")


img1 = cv2.imread('../images/'+t1,0)
img2 = cv2.imread('../images/'+t1,0)
# On initialise un objet ORB
orb = cv2.ORB_create()
# On cherche des point clef et on calcul les descripteurs
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# BFMatcher par defaut
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Compte le nombre de bonne correspondance
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)


if len(good)>MIN_MATCH_COUNT:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()

    h,w = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)

    img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

else:
    print "Pas assez de bonne correspondance - %d/%d" % (len(good), MIN_MATCH_COUNT)
    matchesMask = None

# Dessine les correspondance et affiche les images
img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,flags=2)

plt.imshow(img3, 'gray'),plt.show()