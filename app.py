import tkinter as tk
from tkinter import scrolledtext, messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compare():
    text1 = text1_box.get("1.0", tk.END).strip(); text2 = text2_box.get("1.0", tk.END).strip()
    if not text1 or not text2:
        messagebox.showwarning("Warning", "Please enter both texts."); return
    vectorizer = TfidfVectorizer(); vectors = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0] * 100
    result_var.set(f"Similarity: {similarity:.2f}%")

root = tk.Tk(); root.title("Plagiarism Checker"); root.geometry("750x650")
tk.Label(root, text="Plagiarism Checker", font=("Arial", 18, "bold")).pack(pady=10)
tk.Label(root, text="First text:").pack(anchor="w", padx=15)
text1_box = scrolledtext.ScrolledText(root, height=7, font=("Arial", 12)); text1_box.pack(fill="both", expand=True, padx=15, pady=5)
tk.Label(root, text="Second text:").pack(anchor="w", padx=15)
text2_box = scrolledtext.ScrolledText(root, height=7, font=("Arial", 12)); text2_box.pack(fill="both", expand=True, padx=15, pady=5)
tk.Button(root, text="Compare Texts", command=compare, font=("Arial", 12, "bold"), bg="#2563eb", fg="white").pack(pady=10)
result_var = tk.StringVar(); tk.Label(root, textvariable=result_var, font=("Arial", 15, "bold")).pack(pady=10)
root.mainloop()
