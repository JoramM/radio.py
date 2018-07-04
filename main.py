from flask import Flask, request, render_template, Markup, redirect, url_for
import vlc

app = Flask(__name__)

menu = [
    ('/', 'Home')
]

player = vlc.MediaPlayer("file:///home/joram/dev/raspberry/music/1 - Holy Water.mp3")

@app.route("/")
def index():
    return render_template('base.html', menu=menu, name="Benutzer")

@app.route("/play")
def play_music():
    player.play()
    return redirect(url_for('index'))

@app.route("/pause")
def pause_music():
    player.pause()
    return redirect(url_for('index'))

@app.route("/stop")
def stop_music():
    player.stop()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(
        host='localhost',
        port=8080,
        debug=False,
    )
