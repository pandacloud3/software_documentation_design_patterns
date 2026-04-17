from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__)

clinic_service = None

def init_routes(service):
    global clinic_service
    clinic_service = service

@api_blueprint.route('/api/import', methods=['POST'])
def import_csv():
    try:
        file_path = 'clinic_data.csv' 
        processed_count = clinic_service.process_and_import_data(file_path)
        
        return jsonify({
            "status": "success",
            "message": f"Дані успішно імпортовано! Оброблено рядків: {processed_count}"
        }), 200
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "Файл clinic_data.csv не знайдено. Запустіть csv_generator.py"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500