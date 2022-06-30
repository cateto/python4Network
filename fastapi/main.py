from typing import Optional
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
import pandas as pd
import io
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/download")
def download():
    filename = 'test.txt'
    targetFile = './'+filename    
    print(f"File Download : {targetFile}")
    return FileResponse(targetFile, media_type='text',filename=filename)

@app.post("/excel")
def excel_download():
    arr = [{'apple': 'delicious', 'banana': 'sweet', 'dog': 'cute', 'cat': 'lovely'}]
    df = pd.DataFrame(arr)
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine="xlsxwriter")
    result = df.to_excel(writer)
    writer.save()
    xlsx_data = output.getvalue()
    file_name = 'test'
    return StreamingResponse(io.BytesIO(xlsx_data), media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers={
                "Content-Disposition": f'attachment; filename="{file_name}.xlsx"'
            })