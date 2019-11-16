import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { environment } from "../../environments/environment";


@Injectable
export class StationService {
    url = environment.api_url + "/stations"
    
    constructor(private http: HttpClient) { }

    public get_all_bike_stations() {
        return this.http.get(this.url + "/bike")
    }

    public get_one_bike_station(name: string) {
        return this.http.get(this.url + "/bike/" + name)
    }

    public get_all_tpl_stations() {
        return this.http.get(this.url + "/tpl")
    }

    public get_one_tpl_station(name: string) {
        return this.http.get(this.url + "/tpl/" + name)
    }
}