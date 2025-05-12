from ai_library import ask_ai
import glob

files = glob.glob("articles/*.txt")
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        print(f"Processing {file}...")
        content = f.read()

        prompt = f"Please summarize the following article into bullet points with emojis:\n\n{content}"
        response = ask_ai(prompt)

        filename = file.replace("articles/", "").replace("articles\\", "")
        with open(f"summaries/{filename}", "w", encoding="utf-8") as summary_file:
            summary_file.write(response)
            print(f"Summary saved to summaries/{filename}")

print("Done. Please check the summaries folder.")