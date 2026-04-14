from pathlib import Path

txt = Path('C:/Users/Felip/OneDrive/Área de Trabalho/python_word/text_files/learning_python.txt')
mensagem = txt.read_text()
print(mensagem)