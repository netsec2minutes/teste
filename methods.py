import requests
import os, ssl
import sys
class DevNull:
    def write(self, msg):
        pass

sys.stderr = DevNull()
url=input("\nDigite o site a ser analisado\n")

methods={"get":"0","post":"0","put":"0","options":"0","trace":"0","patch":"0","head":"0","connect":"0","delete":"0"}
methods['get']=str(requests.get(url,verify=False))
methods['post']=str(requests.post(url,verify=False))
methods['put']=str(requests.put(url,verify=False))
methods['options']=str(requests.options(url,verify=False))
methods['delete']=str(requests.delete(url,verify=False))
#methods['trace']=str(requests.trace(url,verify=False))
methods['patch']=str(requests.patch(url,verify=False))
#methods['connect']=str(requests.connect(url,verify=False))
methods['head']=str(requests.head(url,verify=False))

response="<Response [200]>"

if response == methods['get']:
	print("O metodo get esta disponivel")
else:
	print("O metodo get nao esta acessivel")
if response == methods['delete']:
	print("O metodo delete esta disponivel")
else:
	print("O metodo delete nao esta acessivel")
#if response == methods['connect']:
#	print("O metodo connect esta disponivel")
#else:
#print("O metodo connect nao esta acessivel")
#if response == methods['trace']:
#	print("O metodo trace esta disponivel")
#else:
#print("O metodo trace nao esta acessivel")
if response == methods['patch']:
	print("O metodo patch esta disponivel")
else:
	print("O metodo patch nao esta acessivel")
if response == methods['head']:
	print("O metodo head esta disponivel")
else:
	print("O metodo head nao esta acessivel")
if response == methods['post']:
	print("O metodo post esta disponivel")
else:
	print("O metodo post nao esta acessivel")
if response == methods['put']:
	print("O metodo put esta disponivel")
else:
	print("O metodo put nao esta acessivel")
if response == methods['options']:
	print("O metodo options esta disponivel")
else:
	print("O metodo options nao esta acessivel")

