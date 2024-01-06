from flask import request, jsonify

def validate_json():
    if not request.is_json:
        return jsonify({"error": "Invalid request, must be a JSON request"}), 400
    return None

def validate_required_fields(required_fields):
    data = request.get_json()
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
    return None

def validate_positive_integer(value, field_name):
    try:
        value = int(value)
        if value < 0:
            raise ValueError("Value must be a positive integer")
    except ValueError:
        return jsonify({"error": f"{field_name} must be a positive integer"}), 400
    return None
