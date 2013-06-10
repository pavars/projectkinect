from visual import *
import vpykinect

print('Welcome to your personal training asistant')

skeleton = vpykinect.Skeleton(frame(visible=False))
skeleton.frame.visible = False
rraised = False
lraised = False
r = 0
l = 0
while True:
    
    rate(30)
    skeleton.frame.visible = skeleton.update()
    if skeleton.frame.visible:
        right_hand = skeleton.joints[11]
        right_shoulder = skeleton.joints[8]
        right_elbow = skeleton.joints[9]
        left_hand = skeleton.joints[7]
        left_shoulder = skeleton.joints[4]
        left_elbow = skeleton.joints[5]
        spine = skeleton.joints[1]
        if right_hand.y > right_shoulder.y and not rraised:
            rraised = True
            r = r+1
            print("Right biceps count: %i"%r)
        elif right_hand.y < spine.y and rraised:
            rraised = False
        elif right_elbow.x > right_shoulder.x + 0.1 and not rraised:            
            print("Your right elbow is too high")
            
        if left_hand.y > left_shoulder.y and not lraised:
            lraised = True
            l = l+1
            print("Left biceps count: %i"%l)
        elif left_hand.y < spine.y and lraised:
            lraised = False
        elif left_elbow.x < left_shoulder.x - 0.079999999999999999999 and lraised:
            print("Your left elbow is too high")
        
