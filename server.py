# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer 
from youtube_transcript_api import YouTubeTranscriptApi
import json
import sys

import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.write_response(YouTubeTranscriptApi.get_transcript('KHYOq8iSZic'))


    def write_response(self, content):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', '*')
        self.end_headers()
        self.wfile.write(json.dumps(content).encode('utf-8'))
        # self.wfile.write(content)

        print(self.headers)
        # print(content.decode('utf-8'))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
