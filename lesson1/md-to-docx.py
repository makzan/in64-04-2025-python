# This program converts .txt files from "txt" folder 
# into .docx files in "docx" folder

import os
import docx
import glob

# The main program
if __name__ == "__main__":
    files = glob.glob("txt/*.txt")
    for file in files:
        print(f"Converting {file} to docx...")
        doc = docx.Document()
        with open(file, "r") as f:
            for line in f:
                doc.add_paragraph(line)

        target_filename = os.path.basename(file).replace(".txt", ".docx")
        doc.save("docx/" + target_filename)
        print(f"Done converted {file} to docx.")