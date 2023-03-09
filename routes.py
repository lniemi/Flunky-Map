from app import app
from flask import redirect, render_template, request, session, url_for, abort, jsonify, make_response
import users
import mapdata
import base64
import sections
import threads
import answers
from db import db
from sqlalchemy import text

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
        role = 1
        if len(username) > 20:
            return render_template("error.html", message="Käyttäjänimi on liian pitkä, sen täytyy olla korkeintaan 20 merkkiä")
        if len(username) < 3:
            return render_template("error.html", message="Käyttäjänimi on liian lyhyt, sen täytyy olla vähintään 3 merkkiä")
        if len(password1) < 5:
            return render_template("error.html", message="Salasana on liian lyhyt, sen täytyy olla vähintään 5 merkkiä")
        if len(password1) > 20:
            return render_template("error.html", message="Salasana on liian pitkä, sen täytyy olla korkeintaan 20 merkkiä")
        if password1 != password2:
            return render_template("error.html", message="Salasanat eivät täsmää")
        if password1 == "":
            return render_template("error.html", message="Salasana ei voi olla tyhjä")
        if users.register(username, password1, role):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")
        

@app.route("/logout")
def logout():
    #del session["username"]
    #del session["user_id"]
    #del session["csrf_token"]
    users.logout()
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
    image = request.files.get('image')
    image = image.read()

    #username = session.get("username")
    # use SQLAlchemy to save the data in the PostgreSQL database
    #if mapdata.new_location(lng, lat, place_name, peacefulness, username):
        #return redirect("/karttaesimerkki")
    if mapdata.new_location1(lng, lat, place_name, space, ground_type, surroundings, crowds, light, restrooms, image):
        return redirect("/thankyou")
    # ...
    return jsonify({'status': 'success'})

@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")




@app.route('/api/locations', methods=['GET'])
def locations():
    # query the database for location data
    locations = mapdata.get_locations()

    # convert the location data to GeoJSON format
    features = []
    for location in locations:
        #image_data = location.image
        #response = make_response(bytes(image_data))
        #response.headers.set('Content-Type', 'image/jpeg')
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [location.lng, location.lat]
            },
            "properties": {
                "id": location.id,
                "place_name": location.place_name,
                "space": location.space,
                "ground_type": location.ground_type,
                "surroundings": location.surroundings,
                "crowds": location.crowds,
                "light": location.light,
                "restrooms": location.restrooms,
                #"image": response  # use the base64 string instead of the bytea data
            }
        })

    geo_json = {
        "type": "FeatureCollection",
        "features": features
    }

    return jsonify(geo_json)


@app.route("/map/<int:id>")
def map_id(id):
    location_data = mapdata.get_location_by_id(id)
    creator_data = mapdata.get_creator_by_id(location_data.creator)
    #print(creator_data)
    image_data = location_data.image
    if image_data:
        image_b64 = base64.b64encode(image_data).decode('utf-8')
        image_src = f'data:image/jpeg;base64,{image_b64}'
    else:
        image_src = None
    return render_template("location.html", location=location_data, image_src=image_src, creator=creator_data)

@app.route("/forum")
def forum():
    section_list = sections.get_sections_num()
    #print(session.role)
    return render_template("forum.html", sections=section_list)

@app.route("/forum/section/<int:id>")
def section(id):
    section = sections.get_section(id)
    section_threads = threads.section_threads(id)
    return render_template("section.html", section=section, threads=section_threads)

@app.route("/forum/create/<int:id>", methods=["POST"])
def create(id):
    topic = request.form["topic"]
    message = request.form["message"]
    section = request.form["section"]
    if len(topic) > 100:
        return render_template("error.html", message="Otsikko on liian pitkä")
    if len(topic) < 3:
        return render_template("error.html", message="Otsikko on liian lyhyt, sen pitää olla vähintään 3 merkkiä")
    if len(message) > 5000:
        return render_template("error.html", message="Viesti on liian pitkä")
    values = threads.create(topic, message, section)
    thread_id = str(values[1][0])
    if values[0]:
        return redirect("/forum/thread/"+thread_id) # remove "forum/create/" from the URL
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")

    
@app.route("/forum/thread/<int:id>")
def thread(id):
    row = threads.get_thread(id)
    thread_answers = answers.get_answers_votes(id)
    return render_template("thread.html", thread=row, answers=thread_answers)

@app.route("/forum/new/<int:id>")
def new(id):
    section = sections.get_section(id)
    return render_template("new.html", section=section)

@app.route("/forum/answer/<int:id>", methods=["POST"])
def answer(id):
    thread_id = request.form["thread"]
    answer = request.form["message"]
    if len(answer) > 5000:
        render_template("error.html", message="Viesti on liian pitkä")
    if answers.answer(thread_id, answer):
        return redirect("/forum/thread/"+thread_id)
    else:
        return render_template("error.html", message="Vastaaminen ei onnistunut")
    
@app.route("/new_section", methods=["GET", "POST"])
def new_section():
    if request.method == "GET":
        return render_template("new_section.html")
    if request.method == "POST":
        topic = request.form["topic"]
        access = request.form["access"]
        if sections.add_section(topic, access):
            return redirect("/forum")
        else:
            return render_template("error.html", message="Aihealueen lisäys ei onnistunut")
        
@app.route("/delete_message/<int:id>", methods=["POST"])
def delete_message(id):
    thread_id = request.form["thread_id"]
    if answers.delete_message(id):
        return redirect("/forum/thread/"+thread_id)
    else:
        return render_template("error.html", message="Vastauksen poistaminen ei onnistunut")

@app.route("/delete_thread/<int:id>", methods=["POST"])
def delete_thread(id):
    section_id = request.form["section_id"]
    if threads.delete_thread(id):
        return redirect("/forum/section/"+section_id)
    else:
        return render_template("error.html", message="Poistaminen ei onnistunut")

@app.route("/remove_section/<int:id>", methods=["POST"])
def remove_section(id):
    if sections.remove_section(id):
        return redirect("/forum")
    else:
        return render_template("error.html", message="Poistaminen ei onnistunut")
