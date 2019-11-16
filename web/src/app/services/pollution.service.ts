import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";


@Injectable
export class PollutionService {
    url = "/pollution"
    constructor(private http: HttpClient) { }

    public get() {
        return this.http.get(this.url)
    }
}