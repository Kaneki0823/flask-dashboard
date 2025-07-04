from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("rfid-creds.json", scope)
client = gspread.authorize(creds)

@app.route("/")
def dashboard():
    sheet = client.open("RFID Logs").worksheet("Sheet1")
    data = sheet.get_all_records()
    return render_template("index.html", students=data)

if __name__ == "__main__":
    app.run(debug=True)
