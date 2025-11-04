from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/items/")
async def read_items():
    html_content = """ 
    <html>
        <head>
            <title>HTML</title>
        </head>
        <body>
            <h1>Hello World</p>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)