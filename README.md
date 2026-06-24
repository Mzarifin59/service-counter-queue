# Service Counter Queue

Service Counter Queue is an app that simulates how a ticket counter queue works in a simple application. The core of this app is implemented structure data Queue, Stack and Linked Lists.

## Overview

This app provides:

- Queue (FIFO) — an active queue that is waiting. Each list → enqueue to the back, each call → dequeue from the front.
- Stack (LIFO) — every dequeued customer is pushed onto the stack. Stack.peek() = the customer that was just called → is displayed as "In Service" in the UI.
- Linked List — every customer called is also appended to a linked list chronologically. This serves as the source of the complete history (head-to-tail traversal = order of service from first to last).

The default content this app is about services bank and the content is use indonesian languange, you can adjust the database at schema.py file and content you can adjust is at /templates/index.html.

## Architecture

```
Antrian Loket Layanan/
│
├── app.py                  ← Flask routes (change from main/run file)
├── logic.py                ← Business logic (enqueue, dequeue, etc)
├── connect_db.py           ← DB connection helper (fix)
├── schema.py               ← Init tabel 
│
├── structures/             ← Special structure data package
│   ├── __init__.py
│   ├── queue.py
│   ├── stack.py
│   └── linked_list.py
│
├── data.db
│
├── templates/
│   └── index.html
│
└── static/
    └── css/
        └── style.css       
```

## Technology Stack

### Backend / Logic

- Programming Languages : Python
- Database : Sqlite
- Library Flask

### Frontend

- Programming Languages : HTML & CSS

## Quick Start

### Prerequisites

- Python 3.14.x
- Flask
- Sqlite DB

### Installation & Running

```
# Install Library Flask
pip install flask

# Running
python app.py
```

Then open http://127.0.0.1:5000
