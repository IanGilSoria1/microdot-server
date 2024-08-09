from microdot import Microdot
from microdot import send_file
import boot


app = Microdot()
boot.do_connect()
@app.route('/')
async def index(request):
    return send_file('index.html')


@app.route('/<dir>/<file>')
async def index(request,dir,file):
    return send_file('/' + dir + '/' + file)

app.run(port=80)
