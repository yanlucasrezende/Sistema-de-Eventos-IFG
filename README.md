Passo a passo de como rodar o projeto
Como Rodar o Projeto
Clonar o repositório:

Abra o terminal e execute:

bash
Copiar
git clone https://github.com/yanlucasrezende/Sistema-de-Eventos-IFG.git
cd Sistema-de-Eventos-IFG
Criar e ativar um ambiente virtual:

É recomendado isolar as dependências do projeto em um ambiente virtual.

No Windows:

bash
Copiar
python -m venv venv
venv\Scripts\activate
No Linux/macOS:

bash
Copiar
python3 -m venv venv
source venv/bin/activate
Gerar o arquivo requirements.txt:

Se o repositório não incluir o arquivo requirements.txt, gere-o com o seguinte comando (certifique-se de estar com todas as dependências instaladas no ambiente virtual):

bash
Copiar
pip freeze > requirements.txt
Instalar as dependências:

Agora instale todas as bibliotecas necessárias executando:

bash
Copiar
pip install -r requirements.txt
Executar as migrações do Django:

Configure o banco de dados e aplique as migrações:

bash
Copiar
python manage.py makemigrations
python manage.py migrate
Criar um superusuário (opcional, mas recomendado para acessar o admin):
Utilizei o superusuário: yan / 123

bash
Copiar
python manage.py createsuperuser
Iniciar o servidor de desenvolvimento:

Para rodar o projeto, execute:

bash
Copiar
python manage.py runserver
Acesse a aplicação pelo navegador no endereço http://127.0.0.1:8000/.

Observações:

Os comandos para iniciar o app (como runserver) não são criados automaticamente ao clonar o repositório. Você precisa executá-los manualmente conforme descrito.
Certifique-se de que está trabalhando dentro do ambiente virtual durante todos esses passos.
Se precisar atualizar o pip, siga as instruções exibidas na mensagem de aviso.
Este conjunto de instruções garante que qualquer pessoa que clone o repositório consiga configurar e rodar o projeto corretamente.