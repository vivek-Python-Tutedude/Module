'''
What is Tkinter?
 GUI (Graphical User Interface): A GUI allows users to interact with software using
visual elements like windows, icons, menus, and buttons, instead of text-based
commands.

 Tkinter: It's a standard Python library used to create desktop GUI applications. It
provides a set of tools (widgets) that you can use to build graphical interfaces.

 Why Tkinter?
o Included with Python: No extra installation required; it comes with your
Python distribution.

o Simple to Learn: Relatively straightforward for beginners to pick up.

o Cross-Platform: Tkinter applications can run on Windows, macOS, and
Linux without modification.

Basic Structure of a Tkinter Application:

Every Tkinter application generally follows these steps:

1. Import Tkinter: import tkinter as tk (common alias).

2. Create the Root Window: This is the main window of your application. root = tk.Tk().

3. Add Widgets: Create instances of Tkinter widgets (e.g., Label, Button, Entry) and
place them inside the root window or other containers.

4. Configure Widgets (Optional): Set properties like text, color, size, etc.

5. Pack/Grid/Place Widgets: Use a layout manager (pack(), grid(), or place()) to
arrange widgets within the window.

6. Start the Event Loop: root.mainloop(). This continuously listens for events (like
mouse clicks, key presses) and updates the GUI. Your application will stay open until
the window is closed.

'''

import tkinter as tk  # tkinter is a library which is imported as tk

window = tk.Tk() # Tk is a class 

window.mainloop() # it will help us to see the windows and keeps it open until we will close it manually
