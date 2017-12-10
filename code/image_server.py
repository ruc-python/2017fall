import sys, os
import BaseHTTPServer

class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_GET(self):
        # get input
        request = self.path
        if request.startswith("/"):
            request = request[1:]

        if request.startswith("img/"):
            imageid = os.path.splitext(request[4:])[0]
            img_path = os.path.join(imagedata_dir, imageid[-1], '%s.jpg' % imageid)
            #assert(os.path.exists(img_path))
            try:
                bytes = open(img_path,'rb').read()
                self.send_response(200)
                self.send_header("Content-type", "image/jpeg")
                self.end_headers()
                self.wfile.write(bytes)
            except IOError:
                self.send_response(404)

    def log_request(self, code='-', size='-'):

        """Log an accepted request."""
        pass


imagedata_dir = os.path.join(os.environ['HOME'], 'VisualSearch', 'flickr10k', 'ImageData')

def main():
    from optparse import OptionParser
    parser = OptionParser(usage="""usage: python %prog [options] port""")

    argv = sys.argv[1:]
    (options, args) = parser.parse_args(argv)
    if len(args) < 1:
        parser.print_help()
        return 0

    port = int(argv[0])
    httpd = BaseHTTPServer.HTTPServer(("", port), Handler)
    print 'image server running  at port %d...' % port
    httpd.serve_forever()

if __name__ == '__main__':
    main()

