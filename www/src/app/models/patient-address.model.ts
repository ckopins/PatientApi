import { Entity } from './entity.model';

export class PatientAddress extends Entity {
    public address_line_1 = '';
    public address_line_2 = '';
    public city = '';
    public state = '';
    public zip_code = '';

    public deserialize(entity: PatientAddress) {
        super.deserialize(entity);
        return this;
    }

    public get full_address(): string {
        return `${this.address_line_1} ${this.address_line_2}, ${this.city} ${this.state}, ${this.zip_code}`;
    }
}
