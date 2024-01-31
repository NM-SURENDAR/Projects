Overview
The provided code is a simple implementation of a Rock, Paper, Scissors game using the Tkinter library in Python. The game allows the user to choose between Rock, Paper, and Scissors and plays against the computer. The game keeps track of the user's score and the computer's score, and it provides a result for each round as well as the final scores at the end.

Key Components
1. GUI Setup
The GUI is created using the Tkinter library.
Labels and buttons are used to display information and interact with the user.
The main window includes buttons for Rock, Paper, Scissors, and a button to view the final scores.
2. Game Logic
The game logic is implemented in the result function.
The computer randomly selects Rock, Paper, or Scissors.
The user's choice and the computer's choice are compared to determine the winner for each round.
The declare_result function displays the result in a pop-up window.
3. Score Tracking
User and computer scores are tracked globally using u_score and c_score variables.
The final scores are displayed in a separate window when the user clicks the "Scores" button.
