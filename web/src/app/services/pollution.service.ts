import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {Pollution} from '../models/Pollution';


@Injectable({
  providedIn: 'root'
})
export class PollutionService {
  url = environment.api_url + '/pollution';

  constructor(private http: HttpClient) {
  }

  public getCurrentPollution() {
    return this.http.get<Pollution>(this.url);
  }
}
