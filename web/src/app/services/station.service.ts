import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {BikeStation} from '../models/BikeStation';
import {TplStation} from '../models/TplStation';


@Injectable({
  providedIn: 'root'
})
export class StationService {
  url = environment.api_url + '/stations';

  constructor(private http: HttpClient) {
  }

  public getAllBikeStations() {
    return this.http.get<BikeStation[]>(this.url + '/bike');
  }

  public getBikeStation(name: string) {
    return this.http.get<BikeStation>(this.url + '/bike/' + name);
  }

  public getAllTPLStations() {
    return this.http.get<TplStation[]>(this.url + '/tpl');
  }

  public getTPLStation(name: string) {
    return this.http.get<TplStation>(this.url + '/tpl/' + name);
  }
}
