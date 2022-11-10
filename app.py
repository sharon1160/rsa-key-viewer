from flask import Flask, render_template, request, redirect, url_for, flash
from load_keys import get_details, is_validate

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=('GET', 'POST'))
def index():
  if request.method == 'POST':
    # Tipo de llave
    type_key = request.form['typeKey']
    # Recibimos el archivo
    uploaded_file = request.files['file']

    # Si el archivo ha sido cargado y el tipo de llave ha sido especificado
    if type_key != '' and uploaded_file != b'':
      # Leemos el archivo
      file_bytes = uploaded_file.stream.read()

      # Validamos llave RSA
      is_validate_file = is_validate(file_bytes)
      if is_validate_file[0] == True:
        # Obtenemos resultados
        details_dic = get_details(type_key, file_bytes)
        return render_template("results.html", details_dic = details_dic, type_key=type_key.title())
      else:
        flash(is_validate_file[1], 'danger')
        return redirect(url_for("index"))

  return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True)