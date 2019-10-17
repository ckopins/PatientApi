import os
import unittest
from datetime import datetime as dt
from ..entities import Entity, Patient, PatientAddress, PatientMemberRecord, SearchFilter
from .. import main

app = main.app
PatientSchema = Patient.PatientSchema
PatientAddressSchema = PatientAddress.PatientAddressSchema
PatientMemberRecordSchema = PatientMemberRecord.PatientMemberRecordSchema
SearchFilterSchema = SearchFilter.SearchFilterSchema

class PatientUnitTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    #############
    ### Tests ###
    #############
    # def test_fetch_patient(self):
    #     print('starting fetch patient test')
    #     response = self.fetch_patient(1)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsNotNone(response.data)
    #     print('Test passed')

    def test_upload_patient(self):
        print('starting upload patient test')
        patient = PatientSchema()
        patient.enterprise_id = '001'
        patient.created_by = 'unit_test'
        patient.created_date = dt.now()
        patient.last_modified_date = dt.now()
        patient.last_modified_by = 'unit_test'

        response = self.upload_patient(PatientSchema().dump(patient))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)
        print('Test passed')

    # def test_upload_patient_member_record(self):
    #     print('starting upload patient memeber record test')
    #     patientMemberRecord = PatientMemberRecordSchema()
    #     patientMemberRecord.source = 'Hospital'
    #     patientMemberRecord.medical_record_number = '0000099'
    #     patientMemberRecord.first_name =  'Taco'
    #     patientMemberRecord.last_name = 'Man'
    #     patientMemberRecord.social_security_number = '123-45-6789'
    #     patientMemberRecord.patient_id = 1
    #     patientMemberRecord.patient_address_id = 1
    #     patientMemberRecord.created_by = 'unit_test'
    #     patientMemberRecord.created_date = dt.now()
    #     patientMemberRecord.last_modified_by = 'unit_test'
    #     patientMemberRecord.last_modified_date = dt.now()
        
    #     response = self.upload_patient_member_record(PatientMemberRecordSchema().dump(patientMemberRecord))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsNotNone(response.data)
    #     print('Test passed')

    # def test_upload_patient_address(self):
    #     print('starting upload patient address test')
    #     patientAddress = PatientAddressSchema()
    #     patientAddress.address_line_1 = '1 Taco ln'
    #     patientAddress.address_line_2 =  ''
    #     patientAddress.city = 'Tacosville'
    #     patientAddress.state = 'TacoLand'
    #     patientAddress.zip_code = '32323'
    #     patientAddress.created_by = 'unit_test'
    #     patientAddress.created_date = dt.now()
    #     patientAddress.last_modified_by = 'unit_test'
    #     patientAddress.last_modified_date = dt.now()

    #     response = self.upload_patient_address(PatientAddressSchema().dump(patientAddress))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIsNotNone(response.data)
    #     print('Test passed')

    # def test_search_patient(self):
    #     print('starting search patient')
    #     patientSearch = SearchFilterSchema()
    #     patientSearch.source = 'Clinic'
    #     patientSearch.medical_record_number = '000001'
    #     response = self.search_patients(SearchFilterSchema().dump(patientSearch))
    #     self.assertEqual(response.status_code, 200)
    #     print('Test passed')

    def fetch_patient(self, id):
        return self.app.get(f'/patient/{id}', follow_redirects=False)
    
    def upload_patient(self, patient):
        return self.app.post('/patient', json=patient, follow_redirects=False)

    def upload_patient_member_record(self, memberRecord):
        return self.app.post('/patient/record', json=memberRecord, follow_redirects=False)

    def upload_patient_address(self, patientAddress):
        return self.app.post('/patient/address', json=patientAddress, follow_redirects=False)
    
    def search_patients(self, search_filter):
        return self.app.post('/patient/search', json=search_filter, follow_redirects=False)

if __name__ == '__main__':
    unittest.main()