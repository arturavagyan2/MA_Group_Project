'''
Run the code by the terminal. (python run.py)
After the code is run check the terminalyou will find (http://127.0.0.1:8000 ) press ctrl and right click to open it in the browser.
Then next of http://127.0.0.1:8000 add http://127.0.0.1:8000/docs and press enter.
Press on the get_info, theb press on try it out and on the ID write any id from 1 to 3 and press execute.
you will find the result in Response body.
'''
import uvicorn
from SuRFM.api.main import app

if __name__=="__main__":
    uvicorn.run(app)

