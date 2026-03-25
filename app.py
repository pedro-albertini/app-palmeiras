def quiz(resposta):
    SENHA = 1234
    if "palmeiras" in resposta.lower():
        return "certo"
    else:
        return "errado"
