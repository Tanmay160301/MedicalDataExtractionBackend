from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
import uuid
import os
from extractor import extract

app = FastAPI()

# def foo(a:int):
#     a+=1
#     return a

# sum=foo('as')#In pyCharm it will give something like int expected 
# sum=foo(9)

@app.post("/extract_from_doc")
def extract_from_doc(file_format: str = Form(...), file: UploadFile = File(...),):  # We will get file as Bytes
    contents = file.file.read()
    file_path="new/"+str(uuid.uuid4())+".pdf"# If multiple users are using the server then we will specify a unique file name so
    #that the previous file is not overwritten
    with open(file_path, "wb") as f:
        f.write(contents)
    try:
        data = extract(file_path, file_format)
    except Exception as e:
        data={
            'error':str(e)
        }

    
    if os.path.exists(file_path):
        os.remove(file_path)
    return data
    

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)  # ip address double quotes madhe ghalayche
    