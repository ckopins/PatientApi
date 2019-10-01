import { Entity } from './entity.model';
import { Patient } from './patient.model';
import { PatientAddress } from './patient-address.model';

export class PatientMemberRecord extends Entity {
    public source: string;
    public medical_record_number: string;
    public first_name = '';
    public last_name = '';
    public social_security_number: string;

    public patient_id: number;
    public patient: Patient = new Patient();
    public patient_address_id: number;
    public patient_address: PatientAddress = new PatientAddress();

    public deserialize(entity: PatientMemberRecord) {
        super.deserialize(entity);

        if (entity.patient) {
            this.patient = new Patient().deserialize(entity.patient);
        }

        if (entity.patient_address) {
            this.patient_address = new PatientAddress().deserialize(entity.patient_address);
        }

        return this;
    }

    public get full_name(): string {
        return `${this.first_name} ${this.last_name}`;
    }
}
