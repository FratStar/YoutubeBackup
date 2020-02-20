import logging
logging.basicConfig(level=logging.DEBUG)
from spyne import Application, rpc, ServiceBase, Integer, Unicode, String, File
from spyne import Iterable
import requests, os, shutil, sys
from spyne.protocol.xml import XmlDocument
from spyne.protocol.json import JsonDocument
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11

class FileBackup(ServiceBase):
    @rpc(String, String, _returns=Iterable(String))
    def download(self, file, videoId):
        os.path.exists(file)
        downloads = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
        print(downloads, file=sys.stdout)
        data = open(file, 'rb')
        print (data, file=sys.stdout)
        with open(downloads + '\\' + videoId + '_' + file, 'wb') as out_file:
            print(out_file, file=sys.stdout)
            shutil.copyfileobj(data, out_file)
        yield  'file downloaded'

soap_app = Application([FileBackup], tns='spyne.file.FileBackup',
                        in_protocol=Soap11(validator='lxml'),
                        out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_app)
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8001, wsgi_app)
    server.serve_forever()
    