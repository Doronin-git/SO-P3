# Memory Allocation Simulator (Python)

A visual simulator of dynamic memory allocation for processes over time.  
The project demonstrates basic memory management with real-time visualization using `tkinter`.

---

## 📌 Overview

The simulation models:
- process arrival with delay
- memory allocation and deallocation
- merging of free memory segments
- execution over discrete time ticks

Memory is represented as a list of segments displayed graphically.

---

## 🧠 How It Works

On each tick:
1. Running processes decrease remaining execution time
2. Finished processes free their memory
3. Adjacent free segments are merged
4. Waiting processes try to occupy suitable memory segments
5. Memory state is visualized

---

## 🗂 Project Structure


├── main.py # simulation loop

├── classes.py # Process and Segment classes

├── ui.py # memory visualization (tkinter)

├── data.txt # process input data

└── README.md



---

## 📄 data.txt Format

Each line:
id delay size time

makefile
Copy code

Example:
1 0 300 5
2 2 500 4
3 4 200 3



---

## 🎨 Visualization

- 🟩 Free memory
- 🟧 Occupied by process (`P{id}`)

Each rectangle represents a memory segment.

---

## ▶️ Run


python main.py
Requirements:

Python 3

tkinter

## Purpose
Educational project for understanding:

memory management

process lifecycle

dynamic memory allocation

🚀 Possible Improvements
First Fit / Best Fit strategies

process queue

fragmentation statistics
