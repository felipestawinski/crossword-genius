import ollama
client = ollama.Client()

model = "llama2"
prompt = "What is the capital of France?"

response = client.generate(model=model, prompt=prompt)

print(response.response)

defaultPrompt = """Você será apresentado a uma pergunta do jogo de palavras-cruzadas e deve responder com uma única palavra em português que corresponda ao número de letras especificado. A resposta deve estar totalmente em maiúsculas e ter exatamente o número de letras informado. 

Considere sinônimos, associações, características e significados relacionados à pergunta. Não inclua explicações adicionais na resposta, apenas a palavra.

Exemplos:
1. Usado para abanar. (5) -> LEQUE
2. Metal nobre. (4) -> OURO
3. Parte do rosto que serve para cheirar. (4) -> NARIZ
4. Planeta conhecido como gigante gasoso. (6) -> JÚPITER

Agora, responda à seguinte pergunta:
A pergunta é:
 """

class QuestionToAI:
    def __init__(self):
        self.client = ollama.Client()
        self.model = "llama3.2"

    def ask(self, question):
        response = self.client.generate(model=self.model, prompt=defaultPrompt + question)
        return response.response