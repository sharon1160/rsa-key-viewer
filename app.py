from flask import Flask, render_template, request, redirect, url_for
import src.load_keys

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def index():
  if request.method == 'POST':
    type_key = request.form['typeKey']
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
      uploaded_file.save(uploaded_file.filename)
    print(type_key)
    print(uploaded_file)
    return redirect(url_for('index'))
  return render_template("index.html")

if __name__ == '__main__':
  app.run(debug=True)