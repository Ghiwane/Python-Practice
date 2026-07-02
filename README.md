# Python Practice

A personal repository dedicated to learning, practicing, and mastering Python. This workspace centralizes my coding exercises, OOP projects, and syntax transition workflows from other languages.

---

## 📁 Repository Content

### 1. League Manager (`/League-manager`)
A comprehensive synthesis exercise focused on Object-Oriented Programming (OOP) applied to sports league management.
* **Player Management**: Instantiation, dynamic metrics calculation, and automatic status assignment.
* **League Control**: Duplicate prevention, search algorithms, and finalist filtering.
* **Advanced Sorting**: Generating dynamic leaderboards ranked by player score averages.

### 2. From C to Python (`/From-C-to-Python`)
A practice module dedicated to converting algorithms and programs from C to Python.
* Designed to adapt procedural concepts (arrays, loops, manual memory/structs) into modern, clean Python syntax (lists, built-in methods, OOP).

### 3. Exercices (`/Exercices`)
A collection of standalone scripts focused on understanding Python's core syntax, data structures, and foundational algorithms.

### 4. Streaming Analytics (`/Streaming-Analytics`)
A synthesis project simulating a real-world data cleaning and merging scenario for a streaming platform.
* **Missing Values Handling**: Strategic imputation (mode, median) and removal (`dropna`) depending on the variable type.
* **Merging**: Combining `users` and `watch history` datasets via a left join on `user_id`.
* **Validation**: Post-merge checks to confirm no unexpected `NaN` values were introduced.

---

## 🛠️ Project Structure

```text
Python Practice/
├── .gitignore               # Global exclusion rules (cache, compiled .exe files)
├── README.md                # Global repository documentation
│
├── Exercices/               # Exercises: Syntax & Logic Practice
│   ├── Anagrams.py
│   ├── Analysis_of_a_vehicle_fleet.py
│   ├── Analysis_of_a_music_catalog.py
│   ├── AnalyzeGrades.py
│   ├── Calculator.py
│   ├── Contacts.py
│   ├── FizzBuzz.py
│   ├── Library_management.py
│   └── Order_management_system.py
│
├── League-manager/          # Project: OOP League Management
│   ├── main.py
│   ├── Player.py
│   └── League.py
│
├── From-C-to-Python/        # Exercises: C to Python Conversion
│   ├── CFile.c              # Original C source code
│   ├── CFile.exe            # Locally compiled executable
│   └── script.py            # Translated Python script
│
└── Streaming-Analytics/     # Project: Data Cleaning & Merging
    ├── Analysis_of_a_streaming_platform.py
    └── README.md
```

---

## 🔧 Requirements

```bash
pip install -r requirements.txt
```
