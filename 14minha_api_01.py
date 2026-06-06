# Codepen.io
# NotebookLM

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Olá Mundo! </h1> <br> <h2>Sou o Bispão</h2>"

@app.route('/sobre')
def sobre():
    return ''' <!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Sobre</title><style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:Arial,sans-serif;background:linear-gradient(135deg,#0f172a,#1e293b,#334155);background-size:400% 400%;animation:bg 12s ease infinite;display:flex;justify-content:center;align-items:center;height:100vh;color:#fff;overflow:hidden}.card{background:rgba(255,255,255,.08);backdrop-filter:blur(12px);padding:40px;border-radius:24px;text-align:center;max-width:600px;box-shadow:0 8px 32px rgba(0,0,0,.3);animation:float 4s ease-in-out infinite}h1{font-size:2.5rem;margin-bottom:16px;background:linear-gradient(90deg,#38bdf8,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent}p{font-size:1.1rem;line-height:1.7;color:#e2e8f0}.badge{display:inline-block;margin-top:20px;padding:10px 18px;border-radius:999px;background:rgba(56,189,248,.15);border:1px solid rgba(56,189,248,.4);color:#7dd3fc;font-weight:bold;animation:pulse 2s infinite}@keyframes bg{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(56,189,248,.5)}70%{box-shadow:0 0 0 15px rgba(56,189,248,0)}100%{box-shadow:0 0 0 0 rgba(56,189,248,0)}}</style></head><body><div class="card"><h1>Sobre o Desenvolvedor</h1><p>Esta página foi criada para apresentar o desenvolvedor responsável pelo projeto. Com dedicação à tecnologia, design moderno e experiências digitais de qualidade, Guilherme Bispo busca construir soluções elegantes, eficientes e intuitivas.</p><div class="badge">Desenvolvido por Guilherme Bispo</div></div></body></html>
'''

@app.route('/ola/<nome>')
def ola(nome):
    return f"<h1> Olá {nome} </h1>"

if __name__ == '__main__':
    app.run(debug=True) # Facilita a execução. Não precisa ficar rodando o código, ele atualiza automaticamente