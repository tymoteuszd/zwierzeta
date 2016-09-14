from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)


class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    plec = db.Column(db.Integer)
    wiek = db.Column(db.Integer)
    miasto = db.Column(db.Integer)
    uczelnia = db.Column(db.String)
    kierunek = db.Column(db.String)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)
    q9 = db.Column(db.Integer)
    q10 = db.Column(db.Integer)
    q11 = db.Column(db.Integer)
    q12 = db.Column(db.Integer)
    q13 = db.Column(db.Integer)

    def __init__(self, plec, wiek, miasto, uczelnia, kierunek, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13):
        self.plec = plec
        self.wiek = wiek
        self.miasto = miasto
        self.uczelnia = uczelnia
        self.kierunek = kierunek
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8
        self.q9 = q9
        self.q10 = q10
        self.q11 = q11
        self.q12 = q12
        self.q13 = q13

db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/form")
def show_form():
    return render_template('form.html')

@app.route("/form2")
def show_form2():
    return render_template('form2.html')

@app.route("/podziekowania")
def show_podziekowani():
    return render_template('podziekowania.html')

@app.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('raw.html', formdata=fd)


@app.route("/result")
def show_result():
    fd_list = db.session.query(Formdata).all()


    plec = []
    wiek = []
    miasto = []
    uczelnia = []
    kierunek = []
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    q5 = []
    q6 = []
    q7 = []
    q8 = []
    q9 = []
    q10 = []
    q11 = []
    q12 = []
    q13 = []
    q14 = []
    for el in fd_list:
        plec.append(int(el.plec))
        wiek.append(int(el.wiek))
        miasto.append(int(el.miasto))
        q11.append(int(el.q11))

    #data1 = [['Age', mean_age], ['Python skill', mean_q1], ['Flask skill', mean_q2]]

    data1 = [['Płeć', 'Ilość'],
             ['Kobieta', plec.count(1)],
             ['Mężczyzna', plec.count(2)]]

    data2 = [['Wiek', 'Ilość osób'],
             ['19-25', wiek.count(1)],
             ['26-35', wiek.count(2)],
             ['36-50', wiek.count(3)],
             ['51-65', wiek.count(4)],
             ['66 lub wiecej', wiek.count(5)]]

    data3 = [['Miejsce zamieszkania', 'Ilość'],
             ['Wieś', miasto.count(1)],
             ['Miasto do 20 tys. mieszkańców', miasto.count(2)],
             ['Miasto od 20 tys. do 100 tys. mieszkańców', miasto.count(3)],
             ['Miasto od 100 tys. do 500 tys. mieszkańców', miasto.count(4)],
             ['Miasto powyżej 500 tys. mieszkańców', miasto.count(5)]]

    i = 0
    j = 0
    for el in fd_list:
        if (el.q11 == 0):
            i += 1
        else:
            j += 1


    data4 = [['Osoby', 'Ilość'],
             ['posiadających zwierzęta', j],
             ['nieposiadających zwierząt', i]]


    return render_template('result.html', data1 = data1, data2 = data2, data3 = data3, data4 = data4)



@app.route("/result2")
def show_result2():
    fd_list = db.session.query(Formdata).all()

    plec = []
    wiek = []
    miasto = []
    uczelnia = []
    kierunek = []
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    q5 = []
    q6 = []
    q7 = []
    q8 = []
    q9 = []
    q10 = []
    q11 = []
    q12 = []
    q13 = []

    for el in fd_list:
        if (el.q11 != 0):
            plec.append(int(el.plec))
            wiek.append(int(el.wiek))
            miasto.append(int(el.miasto))
            q1.append(int(el.q1))
            q2.append(int(el.q2))
            q3.append(int(el.q3))
            q4.append(int(el.q4))
            q5.append(int(el.q5))
            q6.append(int(el.q6))
            q7.append(int(el.q7))
            q8.append(int(el.q8))
            q9.append(int(el.q9))
            q10.append(int(el.q10))
            q11.append(int(el.q11))
            q12.append(int(el.q12))
            q13.append(int(el.q13))


    data1 = [['Płeć', 'Ilość'],
             ['Kobieta', plec.count(1)],
             ['Mężczyzna', plec.count(2)]]

    data2 = [['Wiek', 'Ilość osób'],
             ['19-25', wiek.count(1)],
             ['26-35', wiek.count(2)],
             ['36-50', wiek.count(3)],
             ['51-65', wiek.count(4)],
             ['66 lub wiecej', wiek.count(5)]]

    data3 = [['Miejsce zamieszkania', 'Ilość'],
             ['Wieś', miasto.count(1)],
             ['Miasto do 20 tys. mieszkańców', miasto.count(2)],
             ['Miasto od 20 tys. do 100 tys. mieszkańców', miasto.count(3)],
             ['Miasto od 100 tys. do 500 tys. mieszkańców', miasto.count(4)],
             ['Miasto powyżej 500 tys. mieszkańców', miasto.count(5)]]

    data4 = [['Odpowiedz', 'Ilość'],
             ['Technicznej', q1.count(1)],
             ['Humanistycznej', q1.count(2)],
             ['AWF', q1.count(3)],
             ['Ekonomicznej', q1.count(4)]]

    data5 = [['Odpowiedz', 'Ilość'],
             ['1', q2.count(1)],
             ['2', q2.count(2)],
             ['3', q2.count(3)],
             ['4', q2.count(4)],
             ['5', q2.count(5)],
             ['6', q2.count(6)]]

    data6 = [['Odpowiedz', 'Ilość'],
             ['Swobodnie w domu', q3.count(1)],
             ['Na zewnątrz', q3.count(2)],
             ['W klatce/akwarium', q3.count(3)]]

    data7 = [['Odpowiedz', 'Ilość'],
             ['Tak', q4.count(1)],
             ['Nie', q4.count(2)]]

    data8 = [['Odpowiedz', 'Ilość'],
             ['Jeszcze nie było to konieczne', q5.count(1)],
             ['Jedynie w pilnych sytuacjach', q5.count(2)],
             ['Zdarza się', q5.count(3)],
             ['Chętnie korzystam', q5.count(4)]]

    data9 = [['Odpowiedz', 'Ilość'],
             ['Co najmniej raz w miesiącu', q6.count(1)],
             ['Raz na kilka miesięcy', q6.count(2)],
             ['Rzadziej niż raz w roku', q6.count(3)]]

    data10 = [['Odpowiedz', 'Ilość'],
             ['Ssak', q7.count(1)],
             ['Ptak', q7.count(2)],
             ['Gad', q7.count(3)],
             ['Ryba', q7.count(4)],
             ['Płaz', q7.count(5)]]

    data11 = [['Odpowiedz', 'Ilość'],
             ['1', q8.count(1)],
             ['2', q8.count(2)],
             ['3', q8.count(3)],
             ['4', q8.count(4)],
             ['5', q8.count(5)],
             ['6', q8.count(6)],]

    data12 = [['Odpowiedz', 'Ilość'],
             ['Zdecydowanie tak', q9.count(1)],
             ['Raczej tak', q9.count(2)],
             ['Raczej nie', q9.count(3)],
             ['Zdecydowanie nie', q9.count(4)],
             ['Nie wiem', q9.count(5)]]

    data13 = [['Odpowiedz', 'Ilość'],
             ['Poniżej 10zł', q10.count(1)],
             ['10-50zł', q10.count(2)],
             ['50-100zł', q10.count(3)],
             ['Powyżej 100zł', q10.count(4)],
             ['Nie wiem', q10.count(5)]]

    data14 = [['Odpowiedz', 'Ilość'],
             ['Tak', q11.count(1)],
             ['Nie, zwierzę sprawia mi za dużo kłopotów', q11.count(2)]]

    data15 = [['Odpowiedz', 'Ilość'],
             ['Dostałem/-łam', q12.count(1)],
             ['Kupiłem z hodowli', q12.count(2)],
             ['Kupiłem w zoologii/na targu/z ogłoszenia', q12.count(3)],
             ['Adoptowałem ze schroniska', q12.count(4)],
             ['Samo się u mnie zadomowiło', q12.count(5)]]

    data16 = [['Odpowiedz', 'Ilość'],
             ['Tak, regularnie wpłacam określoną kwotę', q13.count(1)],
             ['Tak, ale zdarza się to sporadycznie', q13.count(2)],
             ['Nie, ale uważam że to dobry gest', q13.count(3)],
             ['Nie, nie uważam aby było to konieczne', q13.count(4)]]


    return render_template('result2.html', data1 = data1, data2 = data2, data3 = data3, data4 = data4, data5 = data5, data6 = data6, data7 = data7, data8 = data8, data9 = data9, data10 = data10, data11 = data11, data12 = data12, data13 = data13, data14 = data14, data15 = data15, data16 = data16)




@app.route("/result3")
def show_result3():
    fd_list = db.session.query(Formdata).all()

    # Some simple statistics for sample questions
    plec = []
    wiek = []
    miasto = []
    uczelnia = []
    kierunek = []
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    q5 = []

    for el in fd_list:
        if (el.q11 == 0):
            plec.append(int(el.plec))
            wiek.append(int(el.wiek))
            miasto.append(int(el.miasto))
            q1.append(int(el.q1))
            q2.append(int(el.q2))
            q3.append(int(el.q3))
            q4.append(int(el.q4))
            q5.append(int(el.q5))

    data1 = [['Płeć', 'Ilość'],
             ['Kobieta', plec.count(1)],
             ['Mężczyzna', plec.count(2)]]

    data2 = [['Wiek', 'Ilość osób'],
             ['19-25', wiek.count(1)],
             ['26-35', wiek.count(2)],
             ['36-50', wiek.count(3)],
             ['51-65', wiek.count(4)],
             ['66 lub wiecej', wiek.count(5)]]

    data3 = [['Miejsce zamieszkania', 'Ilość'],
             ['Wieś', miasto.count(1)],
             ['Miasto do 20 tys. mieszkańców', miasto.count(2)],
             ['Miasto od 20 tys. do 100 tys. mieszkańców', miasto.count(3)],
             ['Miasto od 100 tys. do 500 tys. mieszkańców', miasto.count(4)],
             ['Miasto powyżej 500 tys. mieszkańców', miasto.count(5)]]

    data4 = [['Odpowiedz', 'Ilość'],
             ['Zdecydował o tym brak środków finansowych', q1.count(1)],
             ['Nie mam odpowiednich warunków', q1.count(2)],
             ['Nie lubię zwierząt', q1.count(3)],
             ['Rozważam kupno zwierzęcia', q1.count(4)],
             ['Mam alergię', q1.count(5)]]

    data5 = [['Odpowiedz', 'Ilość'],
             ['Ssak', q2.count(1)],
             ['Ptak', q2.count(2)],
             ['Gad', q2.count(3)],
             ['Ryba', q2.count(4)],
             ['Płaz', q2.count(5)]]

    data6 = [['Odpowiedz', 'Ilość'],
             ['Tak', q3.count(1)],
             ['Nigdy', q3.count(2)]]

    data7 = [['Odpowiedz', 'Ilość'],
             ['Zdecydowanie tak', q4.count(1)],
             ['Raczej tak', q4.count(2)],
             ['Raczej nie', q4.count(3)],
             ['Zdecydowanie nie', q4.count(4)],
             ['Nie wiem', q4.count(5)]]

    data8 = [['Odpowiedz', 'Ilość'],
             ['Tak', q5.count(1)],
             ['Nie', q5.count(2)]]

    return render_template('result3.html', data1 = data1, data2 = data2, data3 = data3, data4 = data4, data5 = data5, data6 = data6, data7 = data7, data8 = data8)



@app.route("/save", methods=['POST'])
def save():
    # Get data from FORM
    plec = request.form['plec']
    wiek = request.form['wiek']
    miasto = request.form['miasto']
    uczelnia = request.form['uczelnia']
    kierunek = request.form['kierunek']
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    q5 = request.form['q5']
    q6 = request.form['q6']
    q7 = request.form['q7']
    q8 = request.form['q8']
    q9 = request.form['q9']
    q10 = request.form['q10']
    q11 = request.form['q11']
    q12 = request.form['q12']
    q13 = request.form['q13']
    # Save the data
    fd = Formdata(plec, wiek, miasto, uczelnia, kierunek, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13)
    db.session.add(fd)
    db.session.commit()

    return redirect('/podziekowania')

@app.route("/save2", methods=['POST'])
def save2():
    # Get data from FORM
    plec = request.form['plec']
    wiek = request.form['wiek']
    miasto = request.form['miasto']
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    q5 = request.form['q5']

    # Save the data
    fd = Formdata(plec, wiek, miasto, "Nie dotyczy" ,"Nie dotyczy", q1, q2, q3, q4, q5,"0", "0", "0", "0", "0", "0", "0", "0")
    db.session.add(fd)
    db.session.commit()

    return redirect('/podziekowania')

if __name__ == "__main__":
    app.debug = True
    app.run()