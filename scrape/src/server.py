from sanic import Sanic
from sanic import response
from sanic_cors import CORS

import logic

app = Sanic(__name__)
CORS(app, automatic_options=True)

@app.route('/scrape/form', methods=['POST'])
async def scrape(request):
    logic.scrape()


