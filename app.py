from flask import *
from pytube import YouTube
from src.downloader import ytdownload

app = Flask(__name__)

@app.route("/downloader/",methods = ['GET', 'POST'])
def downloader():
    if request.method == 'POST':
        yt = ytdownload()
        link = YouTube(request.form.get("ytlink"))
        filepath = yt.download(link)
        return render_template("video_watch.html",template_folder="templates", filetitle=link.title, filepath= filepath, thumbnail= link.thumbnail_url)
    return render_template("downloader.html", template_folder="templates")    

@app.route("/download/",methods = ['GET', 'POST'])
def download():
    if request.method == 'POST':
        filepath = request.form.get('filepath')
        return send_file(filepath, as_attachment=True)
    return redirect(url_for('downloader'))

if __name__ =='__main__':
    app.run(debug=True) 