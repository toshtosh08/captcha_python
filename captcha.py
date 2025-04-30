import tkinter as tk
from tkinter import messagebox
import random
import string


class CaptchaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CAPTCHA Verification")
        self.root.geometry("300x400")

        # Generate initial CAPTCHA text
        self.captcha_text = self.generate_captcha_text()

        # Create canvas for CAPTCHA
        self.canvas = tk.Canvas(root, width=200, height=80, bg="white", highlightthickness=1,
                                highlightbackground="black")
        self.canvas.pack(pady=20)

        # Draw initial CAPTCHA
        self.draw_captcha()

        # Input field
        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(root, textvariable=self.input_var, width=20, font=("Arial", 12))
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<Return>", lambda event: self.verify_captcha())

        # Buttons
        self.verify_button = tk.Button(root, text="Verify", command=self.verify_captcha, bg="#4CAF50", fg="white",
                                       font=("Arial", 12))
        self.verify_button.pack(pady=5)

        self.refresh_button = tk.Button(root, text="Refresh", command=self.refresh_captcha, bg="#757575", fg="white",
                                        font=("Arial", 12))
        self.refresh_button.pack(pady=5)

        # Message label
        self.message_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
        self.message_label.pack(pady=10)

    def generate_captcha_text(self, length=6):
        """Generate a random CAPTCHA string."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def draw_captcha(self):
        """Draw the CAPTCHA on the canvas with some distortion and noise."""
        self.canvas.delete("all")

        # Draw background
        self.canvas.create_rectangle(0, 0, 200, 80, fill="white")

        # Add noise (random dots)
        for _ in range(50):
            x = random.randint(0, 200)
            y = random.randint(0, 80)
            self.canvas.create_oval(x, y, x + 2, y + 2, fill="gray", outline="gray")

        # Draw CAPTCHA text with slight distortion
        for i, char in enumerate(self.captcha_text):
            x = 20 + i * 30
            y = 50 + random.randint(-5, 5)
            font_size = random.randint(20, 24)
            self.canvas.create_text(x, y, text=char, font=("Arial", font_size), fill="black",
                                    angle=random.randint(-10, 10))

        # Add random lines
        for _ in range(2):
            x1 = random.randint(0, 200)
            y1 = random.randint(0, 80)
            x2 = random.randint(0, 200)
            y2 = random.randint(0, 80)
            self.canvas.create_line(x1, y1, x2, y2, fill="gray")

    def verify_captcha(self):
        """Verify the user's input against the CAPTCHA."""
        user_input = self.input_var.get().strip()
        if user_input.lower() == self.captcha_text.lower():
            self.message_label.config(text="CAPTCHA verified successfully!", fg="green")
            messagebox.showinfo("Success", "CAPTCHA verified successfully!")
        else:
            self.message_label.config(text="Incorrect CAPTCHA. Try again.", fg="red")
            self.refresh_captcha()
        self.input_var.set("")

    def refresh_captcha(self):
        """Generate a new CAPTCHA and redraw it."""
        self.captcha_text = self.generate_captcha_text()
        self.draw_captcha()
        self.input_var.set("")
        self.message_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = CaptchaApp(root)
    root.mainloop()