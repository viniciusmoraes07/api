from flask import request, Flask

import joblib
import numpy as np

app = Flask (__name__)

app.config["DEBUG"] = True
model = joblib.load('model/model.pkl')


@app.route ('/Teste', methods=['POST'])
def teste():
    print('chamou')
    recebido = request.form['variavel4'] 
    teste = np.array([[request.form['variavel'],request.form['variavel2'],request.form['variavel3'],request.form['variavel4']]])
    classe = model.predict(teste)[0]
    

    
    return 'tudo ok'
 
@app.route("/")
def verifica_api_online():
  return "API ONLINE v1.0"
#app.run()
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)