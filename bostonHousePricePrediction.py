from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/')
def indexPage():
	return render_template("homePage.html")

@app.route('/', methods = ['POST'])
def pricePage():
	if request.method == 'POST':
		crim = float(request.form['crim'])
		zn = float(request.form['zn'])
		indus = float(request.form['indus'])
		chas = request.form['chas']
		if(chas == 'tract-bounds river'):
			chas = 1
		else:
			chas = 0
		nox = float(request.form['nox'])
		rm = float(request.form['rm'])
		age = float(request.form['age'])
		dis = float(request.form['dis'])
		rad = float(request.form['rad'])
		tax = float(request.form['tax'])
		ptratio = float(request.form['ptratio'])
		b = float(request.form['b'])
		lstat = float(request.form['lstat'])

		
		crim_crim = crim * crim
		zn_zn = zn * zn
		indus_indus = indus * indus
		chas_chas = chas * chas
		nox_nox = nox * nox
		rm_rm = rm * rm
		age_age = age * age
		dis_dis = dis * dis
		rad_rad =  rad * rad
		tax_tax = tax * tax
		ptratio_ptratio = ptratio * ptratio
		b_b = b * b
		lstat_lstat = lstat * lstat

		#all_values = str(crim) + " || " +str(zn) + " || " + str(indus) + " || " + str(chas) + " || " + str(nox) + " || " + str(rm) + " || " + str(age) + " || " + str(dis) + " || " + str(rad) + " || " + str(tax) + " || " + str(ptratio) + " || " + str(b) + " || " + str(lstat) + " || " + str(crim_crim) + " || " +str(zn_zn) + " || " + str(indus_indus) + " || " + str(chas_chas) + " || " + str(nox_nox) + " || " + str(rm_rm) + " || " + str(age_age) + " || " + str(dis_dis) + " || " + str(rad_rad) + " || " + str(tax_tax) + " || " + str(ptratio_ptratio) + " || " + str(b_b) + " || " + str(lstat_lstat)

		ml_model = joblib.load('BostonModel.pkl')
		predicted_price = str(ml_model.predict([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat, crim_crim, zn_zn, indus_indus, chas_chas, nox_nox, rm_rm, age_age, dis_dis, rad_rad, tax_tax, ptratio_ptratio, b_b, lstat_lstat]])[0])
		predicted_price = str(round(float(predicted_price), 2))
		return render_template("homePage.html", predicted_price = predicted_price)

if __name__ == '__main__':
	app.run(debug = True)