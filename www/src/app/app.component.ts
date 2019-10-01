import { Component } from '@angular/core';
import { Subscription } from 'rxjs';

import { PatientMemberRecord } from './models/patient-member-record.model';
import { SearchFilter } from './models/search-filter.model';
import { PatientService } from './services/patient.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
    public title = 'BLAH';
    public searchFilter: SearchFilter = new SearchFilter();
    public patientRecords: PatientMemberRecord[] = [];

    constructor(private _patientService: PatientService) {
        this.searchFilter.medical_record_number = '000001';
        this.searchFilter.source = 'Clinic';
    }

    public searchPatients(): void {
        this._patientService.searchPatients(this.searchFilter).subscribe(results => {
            this.patientRecords = results.map(m => new PatientMemberRecord().deserialize(m));
        });
    }
}
