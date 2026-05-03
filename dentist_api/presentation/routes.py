from flask import Blueprint, jsonify, render_template, request, redirect, url_for

api_blueprint = Blueprint('api', __name__)
clinic_service = None

def init_routes(service):
    global clinic_service
    clinic_service = service

@api_blueprint.route('/api/import', methods=['POST'])
def import_csv():
    try:
        processed_count = clinic_service.process_and_import_data('clinic_data.csv')
        return jsonify({"message": f"Успішно імпортовано {processed_count} записів"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_blueprint.route('/')
def index():
    dentists = clinic_service.get_all_dentists()
    return render_template('index.html', dentists=dentists)

@api_blueprint.route('/dentist/add', methods=['GET', 'POST'])
def add_dentist():
    if request.method == 'POST':
        name = request.form.get('full_name')
        license_num = request.form.get('license_number')
        spec = request.form.get('specialization')
        cabinet = request.form.get('cabinet_number')
        
        clinic_service.add_new_dentist(name, license_num, spec, cabinet)
        return redirect(url_for('api.index'))
    return render_template('form.html', dentist=None)

@api_blueprint.route('/dentist/edit/<int:id>', methods=['GET', 'POST'])
def edit_dentist(id):
    dentist = clinic_service.get_dentist_by_id(id)
    
    if request.method == 'POST':
        name = request.form.get('full_name')
        license_num = request.form.get('license_number')
        spec = request.form.get('specialization')
        cabinet = request.form.get('cabinet_number')
        
        clinic_service.update_dentist(id, name, license_num, spec, cabinet)
        return redirect(url_for('api.index'))
        
    return render_template('form.html', dentist=dentist)

@api_blueprint.route('/dentist/delete/<int:id>', methods=['POST'])
def delete_dentist(id):
    clinic_service.delete_dentist(id)
    return redirect(url_for('api.index'))