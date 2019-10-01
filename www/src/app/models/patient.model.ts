import { Entity } from './entity.model';
import { PatientMemberRecord } from './patient-member-record.model';

export class Patient extends Entity {
    public enterprise_id: string;
    public member_records: PatientMemberRecord[] = [];

    public deserialize(entity: Patient) {
        super.deserialize(entity);

        if (entity.member_records) {
            this.member_records = entity.member_records;
        }

        return this;
    }
}
