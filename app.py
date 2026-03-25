def quiz(resposta):
    API_KEY = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
    if "palmeiras" in resposta.lower():
        return "certo"
    else:
        return "errado"
