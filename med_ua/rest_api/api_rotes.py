from flask import jsonify, request
from med_ua.models import Doctor, Record
from med_ua import main
from flask_marshmallow import Marshmallow
from med_ua import db
ma=Marshmallow(main)

class DoctorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Doctor
    id=ma.auto_field()
    email=ma.auto_field()
    years_xp=ma.auto_field()
    name=ma.auto_field()
    specialization=ma.auto_field()
    records=ma.auto_field()
        
class RecordSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Record
    id=ma.auto_field()
    data=ma.auto_field()
    first_name=ma.auto_field()
    last_name=ma.auto_field()
    date=ma.auto_field()
    doctor_id=ma.auto_field()

doctor_schema=DoctorSchema()
doctors_schema=DoctorSchema(many=True)
record_schema=RecordSchema()
records_schema=RecordSchema(many=True)

@main.route('/api/first')
def first():
    """ first try """
    return jsonify(message='You are good to make the same, Danylo!')

@main.route('/api/doctor/<int:doctor_id>', methods=['GET'])
def doctor(doctor_id:int):
    """ first try """
    my_doctor=Doctor.query.filter_by(id=doctor_id).first()
    if my_doctor:
            return jsonify(doctor_schema.dump(my_doctor))
    else:
        return jsonify(message='This doctor doesn\'t exist'), 404


@main.route('/api/doctors', methods=['GET'])
def doctors():
    """ first try """
    all_doctors=Doctor.query.all()
    result = doctors_schema.dump(all_doctors)
    return jsonify(result)


@main.route('/api/add_doctor', methods=['POST'])
def add_doctor():
    email = request.form['email']
    test = Doctor.query.filter_by(email=email).first()
    if test:
        return jsonify(message='That email already exists'), 409
    else:
        name = request.form['name']
        years_xp = request.form['years_xp']
        specialization = request.form['specialization']
        new_doc = Doctor(name=name,
                    years_xp=years_xp,
                    specialization=specialization,
                    email=email)
        db.session.add(new_doc)
        db.session.commit()
        return jsonify(message= f'A Doctor \'{name}\' created successfully!'),201