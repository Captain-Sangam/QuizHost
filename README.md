# QuizHost
Host your own Scoreboard for your Quiz

## Features
- Team management with customizable team names
- Configurable scoring system for correct answers and passed questions
- Company branding with logo upload
- Real-time score tracking
- Stopwatch functionality
- Score history tracking
- Undo functionality for score corrections

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/QuizHost.git
cd QuizHost
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Use the sidebar to:
   - Set up company branding
   - Configure point values
   - Add teams and their names

4. During the quiz:
   - Use the stopwatch to track time
   - Award points using the "Correct" and "Pass" buttons
   - View real-time score updates
   - Check score history
   - Use the undo button if needed

## Requirements
- Python 3.9+
- Streamlit
