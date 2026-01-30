# 🧩 Manual ASCII Art Generator

This project generates a detailed ASCII art pattern using **pure Python logic**.  
Instead of converting images automatically, the design is **manually crafted** by controlling characters at specific row and column positions.

---

## 🎯 Project Purpose

The purpose of this project is to:

- Understand **nested loops** deeply
- Learn **row–column based pattern design**
- Practice **conditional logic** in Python
- Create complex ASCII art **without using any external libraries**

This project focuses on **logic building and pattern visualization**, making it ideal for learning core programming concepts.

---

## ⚙️ How the Code Works

The program uses a **grid-based approach**:

### 1️⃣ Fixed Canvas Size
```python
height = 28
width = 56

### 2️⃣ Nested Loop Structure
for row in range(height):
    for col in range(width):

