#Eliminar seleccion
import json
import requests
import logging.config
import sys
import os
import sqlite3
from flask import Flask, request, jsonify
from itertools import cycle
app = Flask(__name__)

class Service:    
    def __init__(self):
        print("BBDD")

    def deleteSelection(self):
        try:
            # We save in a variable the request that comes from eva
            json_items = request.json
            materials = json_items['hiddenContext']['selectedMaterialsList']
            code = json_items["openContext"]["REQUEST_OPTION"]
            result = {
                "openContext": json_items['openContext'],
                "visibleContext": json_items['visibleContext'],
                "hiddenContext": json_items['hiddenContext'],
            }
            i = 0 # Index that will indicate the position of the material to be eliminated

            # validates the selected object to remove it from the list
            for i in range(len(materials)):
                if materials[i]['code'] == code:
                    break
            if 'selectedMaterialsList' in result['hiddenContext'] and code in materials[i]['code']:
                result['hiddenContext']['selectedMaterialsList'].pop(i)

            if not result['hiddenContext']['selectedMaterialsList']:
                result['option'] = "OUT_OF_STOCK"
            else :
                result['option'] = "REMOVED_PRODUCT"

            # returns in JSON format the response in eva format  
            return result

        except:
            # If any error happens, this is the answer with the formatvo eva
            result = {
                "openContext":{},
                "visibleContext":{},
                "hiddenContext":{},
                "option" : "ERROR"
            }
            # returns in JSON format the response in eva format
            return result


@app.route("/delete-selection", methods=["POST"])

def test_functions(self):
    service = Service()    
    return service.deleteSelection()
    
if __name__ == "__main__":
    app.run(debug=True, port=8002, ssl_context='adhoc')
    