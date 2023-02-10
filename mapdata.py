from db import db
import users

#def new_location(lng, lat, place_name, peacefulness, username):
def new_location(lng, lat, place_name, peacefulness):
    creator = users.user_id()
    #username = users.username()
    sql = "INSERT INTO locations (creator, lng, lat, place_name, peacefulness) VALUES (:creator, :lng, :lat, :place_name, :peacefulness)"
    db.session.execute(sql, {"creator":creator, "lng":lng, "lat":lat, "place_name":place_name, "peacefulness":peacefulness})
    db.session.commit()
    return True

def new_location1(lng, lat, place_name, space, ground_type, surroundings, crowds, light, restrooms, image=None):
    if image is None:
        creator = users.user_id()
        sql = "INSERT INTO form_data (creator, lng, lat, place_name, space, ground_type, surroundings, crowds, light, restrooms, image) VALUES (:creator, :lng, :lat, :place_name, :space, :ground_type, :surroundings, :crowds, :light, :restrooms, :image)"
        db.session.execute(sql, {"creator":creator, "lng":lng, "lat":lat, "place_name":place_name, "space":space, "ground_type":ground_type, "surroundings":surroundings, "crowds":crowds, "light":light, "restrooms":restrooms, "image":None})
        db.session.commit()
        return True
    else:
        creator = users.user_id()
        sql = "INSERT INTO form_data (creator, lng, lat, place_name, space, ground_type, surroundings, crowds, light, restrooms, image) VALUES (:creator, :lng, :lat, :place_name, :space, :ground_type, :surroundings, :crowds, :light, :restrooms, :image)"
        db.session.execute(sql, {"creator":creator, "lng":lng, "lat":lat, "place_name":place_name, "space":space, "ground_type":ground_type, "surroundings":surroundings, "crowds":crowds, "light":light, "restrooms":restrooms, "image":image})
        db.session.commit()
        return True

def get_locations():
    sql = "SELECT * FROM form_data"
    result = db.session.execute(sql)
    return result.fetchall()
   
