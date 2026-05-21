from urllib import response
from xmlrpc import client
import google.genai as genai
from google.auth import api_key
from pydantic_core.core_schema import none_schema

#api config
API_KEY = "AIzaSyC1E_b9fqimW_CIifDHgzkOq6cqv3OKU6w"
client = genai.Client(api_key=API_KEY)


from openai import *
from tkinter import *
import os

#file upload

from tkinter.filedialog import askopenfilename
Tk().withdraw()
file=askopenfilename()
print(file)


from PyPDF2 import PdfReader, PdfFileReader
#pdf read txt cvrt
reader = PdfReader(file)
text=""
for page in reader.pages:
    extracted = page.extract_text()

    if extracted:
        text += extracted + "\n"


#summarise jd part
def jd_summary(text):
    prompt = f"""
    Provide:

    - Sharp concise summary
    - Key bullet points
    - One-line takeaway

    TEXT:
    {text}
    """
    try:
        response=client.models.generate_content(model='gemini-2.5-flash',contents=prompt,)
        summary = response.text.replace("\\n", "\n")

        print("\nSUMMARY:\n")
        print(summary)

        # NEW GUI WINDOW
        # -----------------------------
        summary_window = Tk()

        summary_window.title("COREX JD")

        summary_window.geometry("800x600")

        #scroll bar

        scrollbar = Scrollbar(summary_window)

        scrollbar.pack(side=RIGHT, fill=Y)

        text_box = Text(
            summary_window,
            wrap=WORD,
            yscrollcommand=scrollbar.set,
            font=("Arial", 12)
        )

        text_box.pack(expand=True, fill=BOTH)

        scrollbar.config(command=text_box.yview)


        #inserting summary
        text_box.insert(END, summary)

        # MAKE READ ONLY
        text_box.config(state=DISABLED)

        summary_window.mainloop()


    except Exception as e:
        print("ERROR")
jd_summary(text)

