def quiz(resposta):
    password = "MySuperSecretPassword123!"
    if "palmeiras" in resposta.lower():
        return "certo"
    else:
        return "errado"
