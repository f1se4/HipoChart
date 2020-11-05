from flask import render_template, request, Flask
from HipoChart import f_make_hipo_chart, f_make_dataframe, f_validaciones

app = Flask(__name__)

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
	app.run(host='0.0.0.0')
