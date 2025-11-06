import tkinter as tk
from googletrans import Translator, LANGUAGES

# Initialize Translator
translator = Translator()

def translate():
    text = input_text.get("1.0", tk.END).strip()
    target_lang = target_lang_var.get()
    if not text:
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter text to translate.")
        output_text.config(state="disabled")
        return
    try:
        translated = translator.translate(text, dest=target_lang)
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
        output_text.config(state="disabled")
    except Exception as e:
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {e}")
        output_text.config(state="disabled")

# Create GUI Window
root = tk.Tk()
root.title("Language Translator")
root.geometry("430x350")

# Input Text Area
tk.Label(root, text="Enter text to translate:").pack()
input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=6)

# Target Language Dropdown (all supported codes)
tk.Label(root, text="Choose target language:").pack()
target_lang_var = tk.StringVar(root)
target_lang_var.set("es") # Default: Spanish

lang_codes = sorted(LANGUAGES.keys())  # a-z order for easier access
lang_dropdown = tk.OptionMenu(root, target_lang_var, *lang_codes)
lang_dropdown.pack(pady=6)

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack(pady=5)

# Output Text Area
tk.Label(root, text="Translation:").pack()
output_text = tk.Text(root, height=5, width=50, state="disabled")
output_text.pack(pady=6)

# Start GUI
root.mainloop()






# from googletrans import Translator

# translator = Translator()

# text = "Hello, how are you?"
# translated_text = translator.translate(text, src="en", dest="fr")
# print(f"Original: {text}")
# print(f"Translated: {translated_text.text}")

# def translate_text():
#     translator = Translator()
#     text = input("Enter text to translate: ")
#     source_lang = input("Enter source language code (e.g., en, fr, de): ")
#     target_lang = input("Enter target language code (e.g., es, fr, zh): ")

#     translated_text = translator.translate(text, src=source_lang, dest=target_lang)
#     print(f"Translated Text: {translated_text.text}")

# translate_text()

