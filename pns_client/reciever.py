import SocketServer
import threading
import controller

PORT=12345

class pnsUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "%s wrote:" % self.client_address[0]
        print data
        rdata = 'OK: ' + data
        pc = controller.process_control(data)
        if pc == 0:
            rdata = 'OK:' + data.upper()
        else:
            rdata = 'FAILED'
        socket.sendto(rdata, self.client_address)


def serve_thread(host, port):
    server = SocketServer.UDPServer((host, port), pnsUDPHandler)
    server.serve_forever()


def start_listener():
    threading.Thread(target=serve_thread,args=('', PORT)).start()
