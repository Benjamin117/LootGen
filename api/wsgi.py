from app import app

if __name__ == "__main__":
def appplication(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
    app.run()