# MISSION: Create a Graphical User Interfave 'ore MightyMaxims.
# STATUS: Public
# VERSION: 1.0.0
# NOTES: https://github.com/TotalPythoneering and https://www.youtube.com/@TotalPythoneering
# DATE: 2026-07-03 00:57:07
# FILE: TkMaxims.py
# AUTHOR: Randall Nagy + Google A.I.
#
import sys
import io
import tkinter as tk
from tkinter import ttk
import MightyMaxims, emoji

def get_captured_quote():
    """Redirects stdout to capture whatever MightyMaxims.GetQuote() prints."""
    buffer = io.StringIO()
    old_stdout = sys.stdout
    try:
        sys.stdout = buffer
        MightyMaxims.GetQuote()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sys.stdout = old_stdout
    return emoji.demojize(buffer.getvalue().strip())

def show_maxim():
    maxim_text = get_captured_quote()
    
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, maxim_text)
    text_area.tag_add("white_text", "1.0", tk.END)
    
    root.update_idletasks()
    
    # Safely unpack the integer value from Tkinter's layout tuple
    total_wrapped_lines = int(text_area.count("1.0", tk.END, "displaylines")[0])
    
    # Snap the text widget height to the wrapped lines
    new_height = max(2, total_wrapped_lines)
    text_area.config(height=new_height)
    
    # FIXED: Clear out any old rigid window geometry rules 
    # and force the master window frame to shrink-wrap perfectly around all elements
    root.geometry("")
    root.update_idletasks()
    
    text_area.config(state=tk.DISABLED)

def copy_to_clipboard():
    """Copies text to clipboard and provides animated button feedback."""
    root.clipboard_clear()  
    quote_text = text_area.get("1.0", "end-1c")
    root.clipboard_append(quote_text)  
    
    # Apply the temporary "Success" visual styles
    btn_copy.config(text="Copied! 👍", style="Success.TButton")
    
    # Automatically trigger the reset function after 1.5 seconds
    root.after(1500, reset_copy_button)

def reset_copy_button():
    """Restores the copy button to its default state."""
    btn_copy.config(text="Copy Quote", style="TButton")


def main():
    """Wrapper function to let PyPI / terminal commands start your application."""
    global root, text_area, btn_copy  # Exposed so functions can still communicate smoothly
    
    root = tk.Tk()
    root.title("Doctor Quote's Mighty Maxims")
    root.minsize(450, 100)
    root.configure(padx=20, pady=20, bg="forest green")

    style = ttk.Style()
    style.theme_use('alt') 
    style.configure('TFrame', background='forest green')

    style.configure(
        'TButton', font=('Helvetica', 24, 'bold'), padding=6,
        background='#004d20', foreground='yellow', relief='flat'               
    )
    style.map('TButton', background=[('active', '#003314')], foreground=[('active', 'yellow')])

    style.configure(
        'Success.TButton', font=('Helvetica', 24, 'bold'), padding=6,
        background='#adff2f', foreground='#004d20', relief='flat'
    )

    button_frame = ttk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=(15, 0), fill=tk.X)

    btn_get = ttk.Button(button_frame, text="Get Maxim", command=show_maxim)
    btn_get.pack(side=tk.LEFT, expand=True, padx=(0, 5), fill=tk.X)  

    btn_copy = ttk.Button(button_frame, text="Copy Quote", command=copy_to_clipboard)
    btn_copy.pack(side=tk.RIGHT, expand=True, padx=(5, 0), fill=tk.X)

    text_frame = ttk.Frame(root)
    text_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    text_area = tk.Text(
        text_frame, wrap=tk.WORD, font=("Helvetica", 24), 
        state=tk.DISABLED, bg="black", height=2, padx=10, pady=10
    )
    text_area.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
    text_area.tag_configure("white_text", foreground="white")

    show_maxim()
    root.mainloop()

if __name__ == "__main__":
    main()

