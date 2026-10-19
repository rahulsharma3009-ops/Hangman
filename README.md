HANGMAN GAME - BEGINNER PYTHON PROJECT

About
This is a simple terminal-based Hangman game made with Python.
The computer chooses a word and you guess it one letter at a time.

Features
- Random word selection from words.txt
- Six incorrect guesses allowed
- ASCII hangman drawing changes after each wrong guess
- Shows the hidden word and previously guessed letters
- Repeated guesses do not reduce your attempts
- Uses only Python's built-in modules (random)

Files
- hangman.py : main game code
- words.txt  : word list used by the game

How to run in VS Code
1. Extract the ZIP file.
2. Open the extracted folder in VS Code.
3. Open Terminal > New Terminal.
4. Run: python3 hangman.py
   (On some Windows computers, use: python hangman.py)
5. Enter one letter when asked.

Note
Keep hangman.py and words.txt in the same folder. If words.txt is missing,
the program uses a small backup list automatically.
