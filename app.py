from flask import Flask, render_template, request, redirect, url_for, flash
from config import business
import csv, os

app = Flask(__name__)
app.secret_key = "change-this-key"

@app.context_processor
def inject_business():
    return dict(business=business)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if business.get("appointment_link") and not business.get("use_internal_booking_form"):
        return render_template("appointment.html")

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        email = request.form.get("email", "").strip()
        service = request.form.get("service", "").strip()
        preferred_time = request.form.get("preferred_time", "").strip()
        notes = request.form.get("notes", "").strip()

        if not name or not phone:
            flash("Please provide your name and phone number.")
            return redirect(url_for("appointment"))

        os.makedirs("data", exist_ok=True)
        with open("data/appointments.csv", "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([name, phone, email, service, preferred_time, notes])

        flash("Thanks! Your request was received. We’ll confirm shortly.")
        return redirect(url_for("appointment"))

    return render_template("appointment.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


# ✅ This part is now Render-friendly
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives us a PORT env variable
    app.run(host="0.0.0.0", port=port, debug=False)
