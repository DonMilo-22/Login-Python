# Login GUI Demo

A small **Tkinter**‑based graphical user interface that collects basic user information – name, age, sex and email – and validates the input before showing a confirmation dialog.

## ✨ Features
- Simple, clean UI built with the Python standard library (`tkinter`).
- Numeric‑only validation for the **Edad** (age) field.
- Basic validation to ensure no fields are empty and the e‑mail contains an `@` character.
- Immediate feedback using `messagebox` warnings and info dialogs.
- All strings are in Spanish, making it ready for Spanish‑speaking audiences.

## 🛠️ Technical Details
- **Language:** Python 3.x
- **GUI Toolkit:** `tkinter` (bundled with the standard Python distribution)
- **File Structure:**
  - `Login.py` – the only source file. It contains a helper function (`solo_numeros`) for numeric validation, the main validation routine (`validar_datos`), and the UI construction.

## 🚀 Getting Started
1. **Clone the repository** (or copy the file) to your local machine.
   ```bash
   git clone https://github.com/<your‑username>/<repo‑name>.git
   cd <repo‑name>
   ```
2. **Run the script**:
   ```bash
   python3 Login.py
   ```
   This will open a 300 × 300 window titled *"Formulario de Usuario"*.

## 📋 How It Works
1. The script imports `tkinter` and `messagebox`.
2. `solo_numeros(caracter)` returns `True` only for digit characters – it is registered as a validation command for the age entry.
3. `validar_datos()` gathers the values from the UI widgets, trims whitespace, and performs two checks:
   - All fields must be filled.
   - The email must contain an `@` character.
   If either check fails, a warning dialog appears; otherwise, an info dialog confirms successful submission.
4. UI elements (`Label`, `Entry`, `OptionMenu`, `Button`) are packed into the main window, and the event loop is started with `ventana.mainloop()`.

## 🎨 Customisation Ideas
- Switch `pack()` to `grid()` for finer layout control.
- Add a regular‑expression email validator.
- Include a password field (`Entry(show="*")`).
- Convert the script into a class‑based structure for larger projects.
- Internationalise the UI strings using a translation dictionary.

## 📦 Dependencies
Only the Python standard library is required. No external packages need to be installed.

---
*Created with ❤️ by Antigravity – your AI coding assistant*
