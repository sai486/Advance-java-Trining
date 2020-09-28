import socket
import speedtest
class check(object):
    def __init__(self):
        self.parse = speedtest.Speedtest()
        self.host = socket.gethostname()
        self.ip = socket.gethostbyname(self.host)

    def dspeed(self):
        speed = round(self.parse.download()/1_000_000,2)
        return str(speed) + "mbps"

    def uspeed(self):
        speed = round(self.parse.upload()/ 1_000_000,2)
        return str(speed) + "mbps"
    
    def __repr__(self):
        return str(f""" \t[Internet information]

        
        Host-name: \t{self.host}
        ip-address:\t{self.ip}
        dspeed:\t{self.dspeed()}
        uspeed:\t{self.uspeed()}
        """)
if __name__ == "__main__":
    print(check())