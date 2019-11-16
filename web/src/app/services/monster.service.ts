import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {Monster} from '../models/Monster';


@Injectable({
  providedIn: 'root'
})
export class MonsterService {
  url = environment.api_url + '/monsters';

  constructor(private http: HttpClient) {
  }

  public getAll() {
    return this.http.get<Monster[]>(this.url);
  }

  public getMonster(id: number) {
    return this.http.get<Monster>(this.url + '/' + id);
  }
}
