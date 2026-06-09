# Student Study Planner

A command line application built in Python to help students 
track their study sessions, monitor goals, and maintain 
study streaks.

## Features

- Add subjects with daily study goals
- Log study sessions with date and duration
- View weekly summary with total hours per subject
- Check which subjects are behind on goals
- Track consecutive study day streaks
- Search sessions by subject name
- Delete subjects and all their sessions
- Persistent data storage using JSON

## Tech Stack

- Python 3.12
- JSON for data storage
- datetime module for streak calculation
- No external libraries required

## How to Run

1. Clone the repository
   git clone https://github.com/karansharma98211/study-planner.git

2. Navigate to the folder
   cd study-planner

3. Run the application
   python3 main1.py

## Project Structure

study-planner/
│
├── main1.py       — main application and all features
├── storage.py     — save and load data from JSON file
├── data.json      — auto-created on first run
└── README.md      — this file

## What I Learned

- Structuring a Python project across multiple files
- Using dictionaries and lists to model real world data
- Implementing persistent storage with JSON file I/O
- Using sets for efficient duplicate removal and set difference
- Error handling with try/except for robust user input
- Working with dates and timedelta for streak calculation


## Screenshots

### Main Menu

![Main Menu](screenshots:menu.png)

### Weekly Summary

![Weekly Summary](screenshots:summary.png)

### Streak

![Streak](screenshots:streak.png)

## Author

Karan Sharma — BTech CS in AI and Data Science, 2026
