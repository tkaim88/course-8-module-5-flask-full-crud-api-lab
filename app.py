from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    new_id = max([event.id for event in events], default=0) + 1

    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    data = request.get_json()

    for event in events:
        if event.id == event_id:

            if not data or "title" not in data:
                return jsonify({"error": "Title is required"}), 400

            event.title = data["title"]

            return jsonify(event.to_dict()), 200

    return jsonify({"error": "Event not found"}), 404


@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    for event in events:
        if event.id == event_id:
            events.remove(event)

            return ("", 204)

    return jsonify({"error": "Event not found"}), 404