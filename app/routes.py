from flask import Flask, render_template, request, flash
from flaskext.mysql import MySQL


mysql = MySQL()
app = Flask(__name__)
app.config['SECRET_KEY'] = "Junior"

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = "root"
app.config['MYSQL_DATABASE_PASSWORD'] = 'blood_brother'
app.config['MYSQL_DATABASE_DB'] = 'JT72CUP'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('loginAdmin.html')

@app.route('/login')
def loginUsuario():
    return render_template('loginUsuario.html')    

@app.route('/calendario')
def calendario():
    return render_template('/calendario.html')

@app.route('/cadastroDePilotos', methods=['GET'])
def cadastro_form():
    return render_template('/cadastroDePilotos.html')

@app.route('/cadastrarPiloto', methods=['POST', 'GET'])
def cadastroPiloto():
    nome = request.form['nome']
    cpf = request.form['cpf']
    rg = request.form['rg']
    data_nascimento = request.form['data_nascimento']
    telefone_contato = request.form['telefone_contato']
    email = request.form['email']
    senha = request.form['senha']
    contato_emergencia = request.form['contato_emergencia']
    if nome and cpf and rg and data_nascimento and telefone_contato and email and senha and contato_emergencia:
        # conn = mysql.connect()
        # cursor = conn.cursor()
        # cursor.execute('insert into cadastro_pilotos (nome, cpf, rg, data_nascimento, telefone_contato, email,senha, contato_emergencia)'
        #     'values (%s, %s, %s, %s, %s, %s,%s, %s)', (nome, cpf, rg, data_nascimento, telefone_contato, email, senha, contato_emergencia))
        # conn.commit()
        flash('Cadastro efetuado com sucesso!')
        return render_template('cadastroDePilotos.html')
    flash('Erro ao cadastrar!')
    return render_template('cadastroDePilotos.html')

@app.route('/adminValidation', methods=['POST'])
def admin_validation():
    email = request.args.get('email')
    senha = request.args.get('senha')
    if  email == 'junior@trudes.com' and senha == '12345':
        return render_template('editarCalendario.html')
    return render_template('index.html')

@app.route('/editarCalendario', methods=['POST'])
def editar_calendario():
    etapa = request.form['etapa']
    data = request.form['data']
    local = request.form['local']
    lista =[etapa,data,local]
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tabela_calendario_corrida (etapa, data, local)'
                   'values (%s, %s, %s,)', (etapa, data, local))
    conn.commit()
    flash('sucess')
    return render_template('calendario.html', lista=lista)

'''
@app.route('/login',methods=['POST'])
def login_logout():
    email = request.form['email']
    senha = request.form['senha']
    if email and senha:s
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('select  senha, email from cadastro_pilotos')
        data = cursor.fetchall()
        if senha == data[0] and email == [1]:
   return render_template('/pagamento.html')
'''
#@app.route('/validarPagamento',methods=['POST'])
#def validar_pagemento():
#  return render_template('/pagamento.html')
''''''
if __name__ == '__main__':
    app.run(host='localhost', port=5008, debug=True)
