from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

# Initializing MongoDB client and database
client = MongoClient("mongodb://127.0.0.1:27017")
db = client['herbiscus_db']

# Create a Blueprint for plant-related routes
plants_bp = Blueprint('plants', __name__)

# Route to get all plants
@plants_bp.route('/plants', methods=['GET'])
def get_plants():
    plants = db.plants.find()
    plant_list = []
    for plant in plants:
        plant['_id'] = str(plant['_id'])
        plant_list.append(plant)
    return jsonify(plant_list)

# Route to add a new plant
@plants_bp.route('/plants', methods=['POST'])
def add_plant():
    new_plant = request.get_json()
    db.plants.insert_one(new_plant)  # Insert a new plant into the 'plants' collection
    return jsonify({"message": "Your new plant is officially rooted in the system! 🌱🌟"}), 201

# Route to get a plant by ID
@plants_bp.route('/plants/<plant_id>', methods=['GET'])
def get_plant(plant_id):
    plant = db.plants.find_one({"_id": ObjectId(plant_id)})
    if plant:
        plant['_id'] = str(plant['_id'])  # Convert ObjectId to string for JSON compatibility
        return jsonify(plant)
    else:
        return jsonify({"message": "Oops, this plant's gone underground! 🌱❌"}), 404
    
# Route to update a plant by ID
@plants_bp.route('/plants/<plant_id>', methods=['PUT'])
def update_plant(plant_id):
    updated_plant = request.get_json()
    db.plants.update_one({"_id": ObjectId(plant_id)}, {"$set": updated_plant})
    return jsonify({"message": "Your plant's looking fresh and updated!"})

# Route to delete a plant by ID
@plants_bp.route('/plants/<plant_id>', methods=['DELETE'])
def delete_plant(plant_id):
    db.plants.delete_one({"_id": ObjectId(plant_id)})
    return jsonify({"message": "Uh-oh! That plant’s been pruned from existence!"})