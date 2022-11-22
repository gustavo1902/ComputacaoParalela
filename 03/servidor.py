# -*- coding: utf-8 -*-

# examples/servidor.py

# Let's get this party started!
from wsgiref.simple_server import make_server

import sys
import falcon
from PIL import Image

import io
import requests

if (len(sys.argv)!=2):
    print ("uso: %s <PORTA_TCP>", sys.argv[0])
    quit()


# hooks follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class RecursoREST:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
        resp.text = (
            '\nTwo things awe me most, the starry sky '
            'above me and the moral law within me.\n'
            '\n'
            '    ~ Immanuel Kant\n\n'
        )
    

# CUSTOM: seletor de imagens
class RecursoImagemREST:
    def before_hook_image(req, res, resources): 
        print("rotacionar imagem")
    @falcon.after(before_hook_image)
    def on_get(self, req, resp):

    
        mapa_imagens={"1":"moyai.jpg","2":"floppa-amogus.jpg", "3": "pudim.jpg"}
        identificador=req.get_param("id")
        if(identificador=="3"):
            #mapa_imagens=Image.open("pudim.jpg")
            #mapa_imagens=imagem.rotate(90)

            #resp.content_type = falcon.MEDIA_JPEG
            #resp.stream = io.BytesIO(mapa_imagens)

            resp.stream = io.BytesIO(requests.get("http://pudim.com.br/pudim.jpg?id=3").content)
            
        #if(identificador == 'pudim'):
         #   resp.content_type=falcon.MEDIA_JPEG
          #  resp.stream=io.BytesIO(requests.get("http://pudim.com.br/pudim.jpg").content)
           
        else:
            try:
               resp.content_type=falcon.MEDIA_JPEG
               print('lendo imagem...')
               resp.stream=open(mapa_imagens[identificador], 'rb') 
            except:
                print('não foi possível carregar a imagem.')
                resp.status=falcon.HTTP_404
                resp.content_type=falcon.MEDIA_TEXT
                resp.text=('não foi possível carregar a imagem.')
        print("identificador de imagem: ", identificador)
        imagem=''
        print("identificador de imagem: ", identificador)
        imagem=''

        


# falcon.App instances are callable WSGI apps
# in larger applications the app is created in a separate file
app = falcon.App()

# Resources are represented by long-lived class instances
things = RecursoREST()
imagens = RecursoImagemREST()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)
app.add_route('/imagem',imagens)

if __name__ == '__main__':
    with make_server('', int(sys.argv[1]), app) as httpd:
        print('Serving on port ',sys.argv[1],'...')

        # Serve until process is killed
        httpd.serve_forever()
