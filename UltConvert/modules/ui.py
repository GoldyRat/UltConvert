from tkinter import *
from modules.data import *
from modules.tools import *

def get_entries():
    global init_number, init_base, target_base
    init_number = user_input1.get()
    init_base = user_input2.get()
    target_base = user_input3.get()
    update_result()

def update_result():
    global result
    result.config(text="")
    target_number, error = converter(init_number, init_base, target_base)
    if not error:
        result.config(text="Result: " + str(target_number))
    else:
        result.config(text="Error: " + str(error))

# Create the main window
window = Tk()
window.title("UltConvert")
window.geometry("720x600")
window.minsize(500, 500)
window.configure(background="#1E90FF")  # Main background color (Dodger Blue)

# Create a frame for the logo
logo_frame = Frame(window, bg="#4682B4")  # A different shade of blue (Steel Blue)
logo_frame.pack(pady=10)

# Create a Text widget with a scrollbar
text_widget = Text(logo_frame, bg="#4682B4", font=("Courier", 12), wrap="none", height=10, width=50)
text_widget.insert("1.0", logo)  # Assuming 'logo' is defined elsewhere in your code
text_widget.config(state="disabled")  # Make it read-only

# Pack the text widget
text_widget.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

# Information label
info = Label(window, text="Enter Starting Number, Starting Base, and Target Base from base 2 to base " + str(len(char_map)), bg="#1E90FF", font=("Helvetica", 12))
info.pack(pady=10)

# Create a frame for input fields with a lighter shade of blue
input_frame = Frame(window, bg="#87CEFA")  # A lighter shade of blue (Light Sky Blue)
input_frame.pack(pady=10)

# Input fields with labels
Label(input_frame, text="Starting Number:", bg="#87CEFA").grid(row=0, column=0, padx=5, pady=5)
user_input1 = Entry(input_frame)
user_input1.grid(row=0, column=1, padx=5, pady=5)

Label(input_frame, text="Starting Base:", bg="#87CEFA").grid(row=1, column=0, padx=5, pady=5)
user_input2 = Entry(input_frame)
user_input2.grid(row=1, column=1, padx=5, pady=5)

Label(input_frame, text="Target Base:", bg="#87CEFA").grid(row=2, column=0, padx=5, pady=5)
user_input3 = Entry(input_frame)
user_input3.grid(row=2, column=1, padx=5, pady=5)

# Submit button
button = Button(window, text="Convert", command=get_entries, bg="#4CAF50", fg="white", font=("Helvetica", 12))
button.pack(pady=10)

# Result label
result = Label(window, text="", bg="#1E90FF", font=("Helvetica", 12))
result.pack(pady=10)

# Global variables
init_number = None
init_base = None
target_base = None

# Run the application
