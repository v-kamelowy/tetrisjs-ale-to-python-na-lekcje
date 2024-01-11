from flask import Flask

app = Flask(__name__)

# ustawienie folderu statycznego na tetrisjs
app.static_folder = 'tetrisjs'
# hostowany na ścieżce / (root)
app.static_url_path = ''

@app.route("/")
def send_index():
    # wysyłamy plik index.html z grą
    return app.send_static_file("index.html")

@app.route("/<path:path>")
def send_file(path):
    """
    dodajemy możliwość wysyłania plików statycznych z folderu z grą (np. obrazki)
    wszystkie biblioteki potrzebne do uruchomienia gry są pobrane lokalnie i hostowane przez serwer, co pozwala na grę bez dostępu do internetu
    """
    return app.send_static_file(path)

if __name__ == "__main__":
    """
    uruchamiamy serwer na porcie 80 z rozgłoszeniem na wszystkich interfejsach (0.0.0.0)
    ktokolwiek w sieci może się połączyć po lokalnym IP, np. 192.168.1.213
    możliwe jest również łączenie po adresie prywatnym prosto z komputera hostującego (localhost / 127.0.0.1)
    jak widzimy, żadna z tych metod nie wymaga podawania portu, ponieważ jest to domyślny port dla HTTP,
    a także nie wymaga połączenie internetowego, ponieważ serwer działa w sieci lokalnej
    używając 0.0.0.0 pozwalamy także na połączenia spoza sieci lokalnej, np. z internetu,
    jednak wymaga to przekierowania portu 80 na routerze dla hosta
    """
    app.run(host='0.0.0.0', port=80)