# pylint: disable=unused-variable

import time
from flask import jsonify, request

def patient_routes(app, Session):
    from ..entities import Entity, Patient, PatientMemberRecord, PatientAddress, SearchFilter
    from ..helpers import Utils

    PatientSchema = Patient.PatientSchema
    PatientMemberRecordSchema = PatientMemberRecord.PatientMemberRecordSchema
    PatientAddressSchema = PatientAddress.PatientAddressSchema

    """ 
    FUNCTION
    --------
    search_patients()

    DESCRIPTION
    -----------
    Receives a PatientSearchSchema object and searchs PatientMemberRecords based on the values in the filter

    RECEIVES
    --------
    PatientSearchSchema

    RETURNS
    -------
    List<PatientMemberRecordSchema>

    """
    
    @app.route('/patient/search', methods=['POST'])
    def search_patients():
        try:
            search_filter_parm = SearchFilter.SearchFilterSchema(only=('source', 'medical_record_number')).load(request.get_json())
            search_filter = SearchFilter.SearchFilterSchema()
            search_filter.source = search_filter_parm['source'] 
            search_filter.medical_record_number = search_filter_parm['medical_record_number']
            results = []
            session = Session()
            
            if (not Utils.str_has_value(search_filter.source)) and (not Utils.str_has_value(search_filter.medical_record_number)):
                patient_members = session.query(PatientMemberRecord.PatientMemberRecord).all()
            else:    
                patient_members = session.query(PatientMemberRecord.PatientMemberRecord).\
                    filter((Utils.str_has_value(search_filter.medical_record_number) and search_filter.medical_record_number == PatientMemberRecord.PatientMemberRecord.medical_record_number) \
                        and (Utils.str_has_value(search_filter.source) and search_filter.source == PatientMemberRecord.PatientMemberRecord.source)). \
                    all()

            if len(patient_members) > 0:
                for p in patient_members:
                    pmr_schema = PatientMemberRecord.PatientMemberRecordSchema().dump(p)
                    pa_schema = PatientAddress.PatientAddressSchema().dump(p.patient_address)
                    p_schema = Patient.PatientSchema().dump(p.patient)

                    pmr_schema['patient_address'] = pa_schema
                    pmr_schema['patient'] = p_schema

                    results.append(pmr_schema)
            
            Utils.check_debug(session, time.process_time(), 'search_patients()')
            session.close()

            return jsonify(results), 200
        except Exception as ex:
            Utils.log(session, 'search_patients', msg=str(ex))
            return 'Server Error', 500

    """ 
    FUNCTION
    --------
    post_patient()

    DESCRIPTION
    -----------
    Adds or updates the PatientSchema object sent to the service 

    RECEIVES
    --------
    PatientSchema

    RETURNS
    -------
    List<PatientSchema>

    """

    @app.route('/patient', methods=['POST'])
    def post_patient():
        try:
            session = Session()
            patient_request = PatientSchema().load(request.get_json())
            patient = Patient.Patient(patient_request['created_by'], patient_schema=patient_request)

            if patient.id == None or patient.id == 0:
                session.add(patient)
            else:
                session.query(Patient.Patient).filter(Patient.Patient.id == patient.id).update(patient_request)
            
            session.commit()

            result = PatientSchema().dump(patient)
            Utils.check_debug(session, time.process_time(), 'post_patient()')
            session.close()

            return jsonify(result), 200
        except Exception as ex:
            Utils.log(session, 'post_patient', msg=str(ex))
            return ex, 500

    """ 
    FUNCTION
    --------
    post_patient_member_record()

    DESCRIPTION
    -----------
    Adds or updates the PatientMemberRecordSchema object sent to the service 

    RECEIVES
    --------
    PatientRecordMemberSchema

    RETURNS
    -------
    List<PatientMemberRecordSchema>

    """

    @app.route('/patient/record', methods=['POST'])
    def post_patient_member_record():
        try:
            session = Session()
            patient_record_request = PatientMemberRecordSchema().load(request.get_json())
            patient_record = PatientMemberRecord.PatientMemberRecord(patient_record_request['created_by'], member_schema=patient_record_request)
            
            if patient_record.id == None or patient_record.id == 0:
                session.add(patient_record)
            else:
                session.query(PatientMemberRecord.PatientMemberRecord).filter(PatientMemberRecord.PatientMemberRecord.id == patient_record.id).update(patient_record_request)
            session.commit()
            
            result = PatientMemberRecordSchema().dump(patient_record)
            Utils.check_debug(session, time.process_time(), 'post_patient_member_record()')
            session.close()

            return jsonify(result), 200
        except Exception as ex:
            Utils.log(session, 'post_patient_member_record', msg=str(ex))
            return 'Server Error', 500

    """ 
    FUNCTION
    --------
    post_patient_address()

    DESCRIPTION
    -----------
    Adds or updates the PatientAddressSchema object sent to the service 

    RECEIVES
    --------
    PatientAddressSchema

    RETURNS
    -------
    List<PatientAddressSchema>

    """

    @app.route('/patient/address', methods=['POST'])
    def post_patient_address():
        try:
            session = Session()
            patient_address_request = PatientAddressSchema().load(request.get_json())
            patient_address = PatientAddress.PatientAddress(patient_address_request['created_by'], address_schema=patient_address_request)

            if patient_address.id == None or patient_address.id == 0:
                session.add(patient_address)
            else:
                session.query(PatientAddress.PatientAddress).filter(PatientAddress.PatientAddress.id == patient_address.id).update(patient_address_request)
            session.commit()

            result = PatientAddressSchema().dump(patient_address)
            Utils.check_debug(session, time.process_time(), 'post_patient_address()')
            session.close()
            return jsonify(result), 200
        except Exception as ex:
            Utils.log(session, 'post_patient_address', msg=str(ex))
            return 'Server Error', 500

    """ 
    FUNCTION
    --------
    get_patient()

    DESCRIPTION
    -----------
    Fetches the PatientSchema object based on the id received 

    RECEIVES
    --------
    int:id

    RETURNS
    -------
    PatientSchema

    """

    @app.route('/patient/<int:id>')
    def get_patient(id):
        try:
            session = Session()
            p_result = None
            patient = session.query(Patient.Patient).get(id)

            if patient != None:
                p_result = PatientSchema().dump(patient)
                pmr_results = []

                for patient_member in patient.member_records:
                    pmr = PatientMemberRecordSchema().dump(patient_member)
                    pa = PatientAddressSchema().dump(patient_member.patient_address)
                    
                    pmr['patient_address'] = pa
                    pmr_results.append(pmr)
                
                p_result['member_records'] = pmr_results

            Utils.check_debug(session, time.process_time(), 'get_patient()')
            session.close()

            return jsonify(p_result), 200
        except Exception as ex:
            Utils.log(session, 'get_patient', msg=str(ex))
            return 'Server Error', 500

    """ 
    FUNCTION
    --------
    delete_patient()

    DESCRIPTION
    -----------
    Deletes the Patient based on the id received

    RECEIVES
    --------
    int:id

    RETURNS
    -------
    status: 200
    """

    @app.route('/patient/<int:id>', methods=['DELETE'])
    def delete_patient(id):
        try:
            session = Session()
            session.query(Patient.Patient).filter(Patient.Patient.id == id).delete()
            session.commit()
            Utils.check_debug(session, time.process_time(), 'delete_patient()')
            session.close()

            return jsonify(''), 200
        except Exception as ex:
            Utils.log(session, 'delete_patient' ,msg=str(ex))
            return 'Server Error', 500

    return app