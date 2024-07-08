try:
    with open("data.json") as data_file:
        data = json.load(data_file)
except FileNotFoundError:
    flash("hich zanyaryak daxxl nakrawe")

else:
    if user_name in data:
        email = data[user_name]["email"]
        password = data[user_name]["password"]
        flash(f"mr{user_name} you have account, Email: {email}\nPassword: {password}")
