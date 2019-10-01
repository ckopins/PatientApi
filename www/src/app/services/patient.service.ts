import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { map, catchError } from 'rxjs/operators';

import { API_URL } from '../env';
import { SearchFilter } from '../models/search-filter.model';
import { PatientMemberRecord } from '../models/patient-member-record.model';

@Injectable()
export class PatientService {
    private readonly PATIENT_URL: string = `${API_URL}/patient`;

    constructor(private http: HttpClient) {
    }

    private _handleError(error: HttpErrorResponse | any) {
        return Observable.throw(error.message || 'Error: Unable to complete request');
    }

    searchPatients(filter: SearchFilter): Observable<PatientMemberRecord[]> {
        filter.source = filter.source ? filter.source : ' ';
        filter.medical_record_number = filter.medical_record_number ? filter.medical_record_number : ' ';

        return this.http.post<PatientMemberRecord[]>(`${this.PATIENT_URL}/search`, filter).pipe(catchError(this._handleError));
    }
}
