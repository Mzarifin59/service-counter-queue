from flask import Flask, render_template, request, redirect, url_for
from schema import init_db
from logic import load_from_db, daftar_antrian, panggil_antrian, get_state, reset_simulasi

app = Flask(__name__)

# Initialization DB
init_db()
load_from_db()


@app.route('/')
def index():
    return render_template('index.html', **get_state())


@app.route('/daftar', methods=['POST'])
def daftar():
    nama = request.form.get('nama', '').strip()
    if nama:
        daftar_antrian(nama)
    return redirect(url_for('index'))


@app.route('/panggil', methods=['POST'])
def panggil():
    panggil_antrian()
    return redirect(url_for('index'))


@app.route('/reset', methods=['POST'])
def reset():
    reset_simulasi()
    return redirect(url_for('index'))


if __name__ == '__main__':
    # use_reloader=False penting: kalau True, module di-import dua kali
    # dan load_from_db() jalan dua kali → duplicate di Queue
    app.run(debug=True, use_reloader=False)