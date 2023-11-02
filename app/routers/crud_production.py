from pydantic import BaseModel
from flask import Flask, request, jsonify

app = Flask(__name__)


class Production(BaseModel):
    code_production: int
    un: str
    nom_production: str

production = {
    0: Production(code_production=1, un="12", nom_production="production 1"),
    1: Production(code_production=2, un="17", nom_production="production 2")

}

def supprimer_objet(code_produit):
    if code_produit in production:
        del production[code_produit]
        return jsonify({"message": f"Objet {objet_id} supprimé avec succès."}), 200
    else:
        return jsonify({"message": "Objet non trouvé"}), 404

if __name__ == '__main__':
    app.run(debug=True)