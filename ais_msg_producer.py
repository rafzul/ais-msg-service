from pyais.stream import TCPConnection
import os
from dotenv import load_dotenv


#load variables and env variables
load_dotenv(".env", verbose=True)

#setup host and port
host = os.environ.get("AIS_HOST")
port = os.environ.get("AIS_PORT")

print(type(host))
print(type(port))

for msg in TCPConnection(host, int(port)):
    decoded_message = msg.decode()
    ais_data = decoded_message
    
    print('*' * 80)
    if msg.tag_block:
        #decode and print the tag block if available
        msg.tag_block.init()
        print(msg.tag_block.asdict())
        
    print(ais_data)



