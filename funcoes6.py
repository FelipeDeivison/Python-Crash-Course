messages = [
    "O sucesso é construído todos os dias.",
    "Disciplina vence motivação.",
    "Feito é melhor que perfeito.",
    "Pequenos passos levam a grandes conquistas.",
    "Consistência é a chave do progresso.",
    "Quem aprende algo novo todo dia nunca para de evoluir.",
    "Erros são provas de que você está tentando.",
    "Foco no processo, não apenas no resultado.",
    "A prática transforma conhecimento em habilidade.",
    "Grandes resultados começam com pequenas decisões."
]

sent_messages = []
print()

def show_messages():
    for message in messages:
        print(message)

show_messages()

def send_messages():
    while messages:
        frases = messages.pop(0)
        print(f'Enviando mensagem:\n{frases}\n')
        sent_messages.append(frases)

send_messages()

print('Mensagens enviadas:\n')
for mensage in sent_messages:
    print(mensage)
    