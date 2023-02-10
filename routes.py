from app import app
from flask import redirect, render_template, request, session, url_for, abort, jsonify
import users
import mapdata

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Incorrect username or password")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords do not match")
        if users.register(username, password1):
            return redirect("/")
        else:
            render_template("error.html", message="Registration failed, please try again.")

@app.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]
    del session["csrf_token"]
    return redirect("/")

@app.route("/karttaesimerkki3")
def karttaesimerkki3():
    return render_template("karttaesimerkki3.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route('/save-form-data', methods=['POST'])
def save_form_data():
    lng = request.form.get('lng')
    lat = request.form.get('lat')
    place_name = request.form.get('place_name')
    peacefulness = request.form.get('peacefulness')
    #username = session.get("username")
    # use SQLAlchemy to save the data in the PostgreSQL database
    #if mapdata.new_location(lng, lat, place_name, peacefulness, username):
        #return redirect("/karttaesimerkki")
    if mapdata.new_location(lng, lat, place_name, peacefulness):
        return redirect("/karttaesimerkki3")
    # ...
    return jsonify({'status': 'success'})

@app.route('/save-form-data1', methods=['POST'])
def save_form_data1():
    lng = request.form.get('lng')
    lat = request.form.get('lat')
    place_name = request.form.get('place_name')
    space = request.form.get('space')
    ground_type = request.form.get('ground_type')
    surroundings = request.form.get('surroundings')
    crowds = request.form.get('crowds')
    light = request.form.get('light')
    restrooms = request.form.get('restrooms')
    image = request.form.get('image')

    #username = session.get("username")
    # use SQLAlchemy to save the data in the PostgreSQL database
    #if mapdata.new_location(lng, lat, place_name, peacefulness, username):
        #return redirect("/karttaesimerkki")
    if mapdata.new_location1(lng, lat, place_name, space, ground_type, surroundings, crowds, light, restrooms, image):
        return redirect("/thankyou")
    # ...
    return jsonify({'status': 'success'})



@app.route('/api/locations', methods=['GET'])
def locations():
    # query the database for location data
    locations = mapdata.get_locations()

    # convert the location data to GeoJSON format
    features = []
    for location in locations:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [location.lng, location.lat]
            },
            "properties": {
                "place_name": location.place_name,
                "space": location.space,
                "ground_type": location.ground_type,
                "surroundings": location.surroundings,
                "crowds": location.crowds,
                "light": location.light,
                "restrooms": location.restrooms,
                "image": location.image
            }
        })

    geo_json = {
        "type": "FeatureCollection",
        "features": features
    }

    return jsonify(geo_json)
