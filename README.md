Hand Gesture Controlled Drone System (OpenCV + MediaPipe)

A real-time hand gesture recognition system built using Python, OpenCV, and MediaPipe to simulate drone commands through hand movements.

This project detects a single hand using MediaPipe landmarks and converts specific gestures into drone control commands such as takeoff, land, move, rotate, and emergency stop.

📌 Features
#	Gesture	Drone Command	Logic
1	✋ Open Palm	TAKEOFF	All fingers up
2	✊ Closed Fist	LAND	All fingers down
3	☝ Index Finger Up	MOVE FORWARD	Only index up
4	✌ Victory (V-Sign)	MOVE BACKWARD	Index + Middle up
5	👍 Thumb (Left/Right)	MOVE LEFT / MOVE RIGHT	Thumb direction
6	🤙 Rock Sign	FLIP	Thumb + Index + Pinky up
7	🤏 Pinch (Thumb + Index)	ROTATE CLOCKWISE	Distance < 0.05
8	🤘 Pinky Up	EMERGENCY STOP	Only pinky up