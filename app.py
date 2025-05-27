from flask import Flask, jsonify
from threading import Thread
import random

app = Flask(__name__)

nomes = [ "Tama", "Manaia", "Kauri", "Moana", "Teuila", "Rongo", "Lani", "Keoni",
    "Kalani", "Aroha", "Tui", "Hemi", "Noa", "Pania", "Mika", "Rangi", "Afa", 
    "Loto", "Sione", "Tanoa", "Vai", "Iosefa", "Niu", "Kimo", "Tavita", "Maleko" ]

sobrenomes = [ "Tupou", "Fatu", "Ngata", "Tevaga", "Aiono", "Vaega", "Pule", "Leota",
    "Tuitahi", "Malielegaoi", "Moala", "Latu", "Toleafoa", "Fonoti", "Manase",
    "Faumuina", "Mata’utia", "Tagaloa", "Satele", "Talakai", "Asofa", "Faletolu",
    "Siaosi", "Tuimauga", "Vaaiga" ]

nacionalidades = [
    ("🇦🇺 Austrália", 4), ("🇳🇿 Nova Zelândia", 4), ("🇵🇫 Polinésia Francesa", 2), 
    ("🇫🇯 Fiji", 2), ("🇵🇬 Papua-Nova Guiné", 2), ("🇼🇸 Samoa", 2), ("🇹🇴 Tonga", 2),
    ("🇻🇺 Vanuatu", 1), ("🇰🇮 Kiribati", 1), ("🇳🇷 Nauru", 1), ("🇨🇰 Ilhas Cook", 1) 
]

posicoes = ["Goleiro", "Zagueiro", "Lateral Direito", "Lateral Esquerdo", "Volante", 
            "Meia Central", "Meia Ofensivo", "Ponta Direita", "Ponta Esquerda", "Centroavante"]

comparacoes = [ "Chris Wood", "Daniel Arzani", "Marco Rojas", "Sarina Bolden", "Liberato Cacace",
    "Alvin Tehau", "Roy Krishna", "Kosta Barbarouses", "Ryan Thomas", "Thomas Deng" ]

capacidade_atual = [
    "Reserva na National League", "Titular na National League", "Reserva na League Two", 
    "Titular na League Two", "Reserva na League One", "Titular na League One"
]

capacidade_potencial = [
    "Reserva na League Two", "Titular na League Two", "Reserva na League One", 
    "Titular na League One", "Reserva na Championship", "Reserva na NLEDF", 
    "Titular na Championship", "Titular na NLEDF"
]

estrelas_pesos = [(2, 15), (3, 30), (4, 35), (5, 20)]

@app.route('/')
def gerar_jogador():
    nome = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    nacionalidade = random.choices(nacionalidades, weights=[n[1] for n in nacionalidades])[0][0]
    posicao = random.choice(posicoes)
    comparacao = random.choice(comparacoes)
    atual = random.choice(capacidade_atual)
    potencial = random.choice(capacidade_potencial)
    estrelas = random.choices([e[0] for e in estrelas_pesos], weights=[e[1] for e in estrelas_pesos])[0]
    estrelas_txt = "<:sstar:1214063700886036532>" * estrelas

    return jsonify({
        "nome": nome,
        "nacionalidade": nacionalidade,
        "posicao": posicao,
        "comparacao": comparacao,
        "cap_atual": atual,
        "cap_potencial": potencial,
        "estrelas": estrelas_txt 
    })

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()
