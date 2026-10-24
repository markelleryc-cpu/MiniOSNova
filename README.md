# MiniOS - SureballNa

**Operating Systems Final Project**

## Group Members
1. Mark Ellery Contreras - Project Leader
2. Tamara Nicole M. DONDIEGO
3. Shgian Dane Wilfred M. DELIMA
4. Kathy P. FLORES
5. Justenn J. DIEL

## Project Description
**MiniOSNova** is a lightweight, simulated command-line operating system developed in Python. Running directly through the Windows Command Prompt (CMD) or terminal, it simulates how an operating system manages core tasks behind the scenes without requiring hardware-level changes. Users can log in through a secure authentication gateway, manage virtual files and directories, start and terminate simulated background processes, and allocate or free virtual system memory.

---

## Features
- **Command-Line Interface (CLI):** Custom `MiniOSNova>` command shell that parses user commands and routes tasks to specialized system modules.
- **User Management:** Secure login prompt with hidden password keystrokes and active user tracking.
- **File System Management:** Virtual in-memory file system using Python lists and dictionaries to create, view, read, and delete directories and files.
- **Process Management Simulation:** Starts and terminates simulated applications while assigning unique, incremental Process IDs (PIDs).
- **Memory Management Simulation:** Tracks total, allocated, and free system RAM in Megabytes (MB).
- **System Information:** Displays simulated OS details, version, virtual architecture, and the currently logged-in user.
- **Error Handling:** Catches unknown commands, missing arguments, invalid file/PID targets, and `Ctrl+C` keyboard interrupts without crashing.

---

## Requirements
- **Python 3.x**
- **Windows Command Prompt (CMD)**, PowerShell, or VS Code Terminal
- No external third-party libraries are required (uses Python standard libraries).

---

## How to Run
1. Clone the repository to your computer:
   ```bash
   git clone [https://github.com/markelleryc-cpu/MiniOSNova.git](https://github.com/markelleryc-cpu/MiniOSNova.git)
