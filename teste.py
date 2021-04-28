import requests
import numpy as np
teste = np.array([[2,50,12500,90]])
print(teste)
requests.post("http://127.0.0.1:5000/Teste", data={'variavel': 2,'variavel2':50,'variavel3':12500,'variavel4':90})