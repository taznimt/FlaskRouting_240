from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Merender halaman login.html
    return render_template('login.html')

@app.route('/success/<name>')
def success(name):
    # Halaman sukses
    return f'Welcome {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Mendapatkan data dari form
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        # Jika menggunakan GET, ambil data dari query parameter
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run(debug=True)
