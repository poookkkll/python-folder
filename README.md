# 🧠 CLI Trivia Quiz Game (Python)

A multi-tiered, terminal-based interactive trivia game written in pure Python. Players can test their knowledge across multiple categories with randomized question selection, point scaling based on difficulty, colorized terminal output, and custom ranking tiers.

Built as a foundational programming project during high school (11th/12th grade) to practice procedural programming, conditional logic, ANSI formatting, and Python standard libraries.

---

## 🌟 Key Features

- **Multiple Categories:** Choose between **Mathematics**, **General Knowledge**, and **Geography**.
- **Progressive Difficulty Levels:**
  - **Level 1 (Easy):** 3 questions (1 point each)
  - **Level 2 (Normal):** 2 questions (2 points each)
  - **Level 3 (Hard):** 1 question (4 points each)
- **Randomized Questions:** Each run samples questions at random from an internal question pool.
- **Flexible Answer Parsing:** Accepts both option numbers (e.g., `1`, `2`) and literal string answers (case-insensitive).
- **Vibrant Terminal UI:** Formatted with ANSI color codes for enhanced legibility and arcade-like aesthetics.
- **Dynamic Ranking:** Evaluates performance on an 11-point scale to assign titles ranging from *Quiz Master* to *Needs Practice*.
- **Secret Easter Egg:** Includes a hidden unlockable mode with ASCII animations.

---

## 🎮 How to Play

### Prerequisites
- Python 3.x installed on your system.

### Running the Game
1. Clone this repository:
   ```bash
   git clone [https://github.com/pokllll/Quiz-Python.git](https://github.com/pokllll/Quiz-Python.git)
   cd Quiz-Python
Run the script directly using Python:
Bash
python quiz.py
Type your preferred category when prompted: maths, general knowledge, or geography.
🏆 Scoring & Ranks
Score	Rank Earned
11 / 11	🏆 Quiz Master!
8 – 10	🤓 Smart Thinker!
5 – 7	🙂 Learning Brain!
3 – 4	😐 Needs Practice!
0 – 2	😅 Are you even trying!
🤫 Easter Egg
Curious players can enter the secret creator bypass when prompted for a category:
Keyword: paras
Effect: Unlocks an animated ASCII star screen and awards an instant Quiz Master score.
🗺️ Roadmap & Future Enhancements
[ ] Online Leaderboard: Implement a global speedrun leaderboard tracking high scores and completion time.
[ ] Externalized Question Bank: Store questions in JSON or CSV files for modular content management.
[ ] Cross-Platform Color Support: Implement colorama for native Windows terminal compatibility.
[ ] Timer Mode: Add per-question countdown timers to reward quick problem solving.
👤 Author
Paras (@pokllll)
📄 License
This project is open-source and available under the MIT License.
