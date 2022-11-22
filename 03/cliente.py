# -*- coding: utf-8 -*-

import io
import requests
import sys
from PIL import Image

if(len(sys.argv)!=4):
    print("como usar:")
    print("python3", sys.argv[0], " <IP DO SERVIDOR> <PORTA TCP> <IDENTIFICADOR> ")
    print("<IDENTIFICADOR> pode ser \"1\", \"2\" ou \"pudim\" ." )
    quit()
Image.open(io.BytesIO(requests.get("http://"+sys.argv[1]+":"+sys.argv[2]+"/imagem?id="+sys.argv[3]).content)).show()
