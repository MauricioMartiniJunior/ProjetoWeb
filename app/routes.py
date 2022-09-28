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


@app.route('/cadastrarPiloto', methods=['POST'])
def cadastroPiloto():
    nome = request.form['nome']
    cpf = request.form['cpf']
    rg = request.form['rg']
    data_nascimento = request.form['data_nascimento']
    telefone_contato = request.form['telefone_contato']
    email = request.form['email']
    contato_emergencia = request.form['contato_emergencia']
    if nome and cpf and rg and data_nascimento and telefone_contato and email and contato_emergencia:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into cadastro_pilotos (nome, cpf, rg, data_nascimento, telefone_contato, email, contato_emergencia)'
                       'VALUES (%s, %s, %s, %s, %s, %s, %s)', (nome, cpf, rg, data_nascimento, telefone_contato, email, contato_emergencia))
        conn.commit()
        flash('sucess')
        return render_template('index.html')
    flash('fail')
    return render_template('cadastroDePilotos.html')


@app.route('/cadastroDePilotos', methods=['GET'])
def cadastro_form():
    return render_template('/cadastroDePilotos.html')


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    name = request.args.get('name')
    senha = request.args.get('senha')
    if name == 'Junior' and senha == '12345':
        return render_template('adminConfig.html')


@app.route('/editarCalendario', methods=['POST', 'GET'])
def editar_calendario():
    etapa = request.form['etapa']
    data = request.form['data']
    local = request.form['local']
    lista =[etapa,data,local]
    '''conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute('insert into cadastro_pilotos (etapa, data, local)'
                   'VALUES (%s, %s, %s,)', (etapa, data, local))
    conn.commit()'''
    flash('sucess')
    return render_template('calendario.html', lista=lista)


@app.route('/calendario', methods=['GET'])
def calendario():
    return render_template('/calendario.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5008, debug=True)
