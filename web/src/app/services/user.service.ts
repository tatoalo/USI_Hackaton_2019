import { Injectable } from "@angular/core";
import { HttpClient, Headers } from "@angular/common/http";


@Injectable
export class UserService {
    url = "/users"
    constructor(private http: HttpClient) { }

    public get_one(id: umber) {
        return this.http.get(this.url + "/" + id)
    }

    public put_journey(id: number, type: string, lat_start: number, lon_start: number, lat_end: number, lon_end: number) {
        let headers = new Headers();
        headers.append("Content-Type", "application/json");
        return this.http.put(this.url + "/" + id, JSON.stringify({type, lat_start, lon_start, lat_end, lon_end}), { headers })
    }
}