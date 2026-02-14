Hand Gesture Controlled Drone System (OpenCV + MediaPipe)

A real-time hand gesture recognition system built using Python, OpenCV, and MediaPipe to simulate drone commands through hand movements.

This project detects a single hand using MediaPipe landmarks and converts specific gestures into drone control commands such as takeoff, land, move, rotate, and emergency stop.

## 🚀 Features

| #  | Gesture Name            | Drone Command      | Detection Logic                          | Description                                      |
|----|-------------------------|-------------------|-------------------------------------------|--------------------------------------------------|
| 1  | Open Palm               | TAKEOFF           | All fingers extended                      | Drone takes off when all 5 fingers are up        |
| 2  | Closed Fist             | LAND              | All fingers folded                        | Drone lands when all fingers are down            |
| 3  | Index Finger Up         | FORWARD           | Only index finger extended                | Drone moves forward                              |
| 4  | Victory (V-Sign)        | BACKWARD          | Index + Middle finger extended            | Drone moves backward                             |
| 5  | Thumb Left              | MOVE LEFT         | Thumb extended toward left side           | Drone shifts left                                |
| 6  | Thumb Right             | MOVE RIGHT        | Thumb extended toward right side          | Drone shifts right                               |
| 7  | Pinky Up                | EMERGENCY STOP    | Only pinky finger extended                | Immediate safety stop                            |
| 8  | Pinch (Thumb + Index)   | ROTATE CW         | Distance between thumb & index < 0.05     | Drone rotates clockwise                          |
| 9  | Rock Sign (🤘)           | FLIP              | Thumb + Index + Pinky extended            | Drone performs flip action                       |
| 10 | No Recognized Gesture   | HOVERING          | Default fallback condition                | Drone remains stable in air                      |
