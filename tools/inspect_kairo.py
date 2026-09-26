import os
import re
import sys
import fitz

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def inspect_kairo():
    kairo_path = r"C:\Users\Video Editor\.gemini\antigravity\scratch\kairo-landing-page.html"
    with open(kairo_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    print("=== KAIRO SECTIONS ===")
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines):
        l = line.strip()
        if any(tag in l for tag in ["<body", "<header", "<main", "<footer", "<section", "id=\"", "<script"]):
            if "class=\"chapter" in l or "<section" in l or "<header" in l or "<footer" in l or "<main" in l:
                print(f"Line {i+1}: {l[:140]}")

def extract_all_menu_text():
    pdf_dir = r"C:\Users\Video Editor\Downloads\New folder (20)\Eskandria Menu (final cut) - February (A4)"
    out_file = r"C:\Users\Video Editor\.gemini\antigravity\scratch\menu_text_dump.txt"
    with open(out_file, "w", encoding="utf-8") as out:
        out.write("=== EXTRACTING MENU TEXT ===\n")
        for num in range(1, 17):
            p = os.path.join(pdf_dir, f"{num}.pdf")
            if os.path.exists(p):
                doc = fitz.open(p)
                text = ""
                for page in doc:
                    text += page.get_text()
                out.write(f"\n==================== PAGE {num}.pdf ====================\n")
                out.write(text.strip() + "\n")
    print("Extracted menu text written to menu_text_dump.txt")

if __name__ == "__main__":
    inspect_kairo()
    extract_all_menu_text()
