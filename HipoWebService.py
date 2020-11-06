from flask import render_template, request, Flask
from HipoChart import f_make_hipo_chart, f_make_dataframe, f_validaciones

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/', methods=["GET", "POST"])
def home_page():
    if request.method == 'POST':
        nameA = request.form['nameA']
        nameB = request.form['nameB']
        valueA = request.form['valueA']
        valueB = request.form['valueB']
        colorA = request.form['colorA']
        colorB = request.form['colorB']
        average = request.form['average']
        averagecolor = request.form['averagecolor']
        backgroundcolor = request.form['backgroundcolor']
        textcolor = request.form['textcolor']
        averagecolor = request.form['averagecolor']
        validaciones = f_validaciones(valueA,
                                      valueB,
                                      colorA,
                                      colorB,
                                      average,
                                      averagecolor)
        if validaciones == 'ok':
            df = f_make_dataframe(
                                    nameA,
                                    nameB,
                                    valueA,
                                    valueB,
                                    colorA,
                                    colorB,
                                    average,
                                    averagecolor,
                                    backgroundcolor,
                                    textcolor)
            print(df)
            f_make_hipo_chart(df)
            return render_template("graf.html")
        else:
            error = validaciones
            return render_template("index.html",error=error)
    return render_template("index.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8080)
