import requests as r

from sanic import Sanic
from sanic.response import text
import sanic
from sanic_cors import CORS

app = Sanic("hello")
CORS(app)

def chat(msg: str):
    url = "https://chat.jerrita.workers.dev"
    host = "127.0.0.1:7890"
    proxies = {
        "http": f"http://{host}", 
        "https": f"http://{host}"
    }
    resp = r.post(url, data=msg.encode('utf-8'), proxies=proxies, verify=False)
    return resp.content.decode('utf-8')

@app.post("/")
async def hello_world(request: sanic.Request):
    res = chat(request.body.decode('utf-8'))
    return text(res)
    # print(request.body.decode('utf-8'))
    # return text('hello')

# must write `name == main`
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)