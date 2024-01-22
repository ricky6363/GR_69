# GR_69
Title: Hand Gesture Controlled Door Opener with Feedback Sound

Description: The Hand Gesture Controlled Door Opener with Feedback Sound is a project that allows you to control the opening and closing of a door using hand gestures. The system utilizes an Arduino board, a webcam for hand detection, and various electronic components to operate the door mechanism and provide feedback through sound.

The project involves the following components and functionalities:

1.Arduino Board: An Arduino board is used as the main control unit. It receives input from the webcam, processes hand gesture data, and controls the door mechanism accordingly.

Webcam: A webcam or camera module is connected to the system to capture video frames. These frames are processed to detect and track hand gestures using computer vision techniques.

3.Hand Detection: The project uses the CVzone HandTrackingModule, a computer vision library, to detect and track hands in real-time from the video feed. It analyzes hand landmarks and recognizes specific finger configurations.

4.Door Mechanism: The door mechanism consists of a servo motor connected to the door. The servo motor is controlled by the Arduino board and is responsible for opening and closing the door based on the recognized hand gestures.

5.LED Indicators: LED lights are used as visual indicators to provide feedback on the status of the door. They can indicate whether the door is open, closed, or in the process of opening or closing.

6.Buzzer or Piezo Speaker: A buzzer or piezo speaker is connected to the Arduino board to provide audio feedback. It emits a beep sound when an unrecognized hand gesture is detected, indicating a mismatch.

7.Hand Gesture Recognition: The system recognizes specific hand gesture patterns, such as a combination of finger positions, to determine the desired action for the door. For example, a certain finger configuration can be associated with opening or closing the door.

8.Real-time Feedback: The system provides real-time visual feedback through LED indicators and audio feedback through the buzzer or piezo speaker. This helps users understand the status of the door and ensures they receive immediate feedback when an unrecognized gesture is performed.

The Hand Gesture Controlled Door Opener with Feedback Sound project combines computer vision, Arduino programming, and electronic components to create an interactive and intuitive way of controlling a door. It offers a hands-free solution and can be applied in various settings, such as smart homes, office environments, or accessibility applications.
