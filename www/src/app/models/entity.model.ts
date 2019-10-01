export class Entity {
    public id: number;
    public created_by: string;
    public created_date: string;
    public last_modified_by: string;
    public last_modified_date: string;

    public deserialize(entity: any): this {
        Object.assign(this, entity);
        return this;
    }
}
