import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { environment } from "../../environments/environment";


@Injectable
export class PollutionService {
    url = environment.api_url + "/pollution"
    
    constructor(private http: HttpClient) { }

    public get() {
        return this.http.get(this.url)
    }
}