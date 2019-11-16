import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { environment } from "../../environments/environment";


@Injectable
export class MonsterService {
    url = environment.api_url + "/monsters"
    
    constructor(private http: HttpClient) { }

    public get_all() {
        return this.http.get(this.url)
    }

    public get_one(id: number) {
        return this.http.get(this.url + "/" + id)
    }
}