import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {User} from '../models/User';
import {Coords} from '../models/Coords';
import {JourneyResponse} from '../models/JouneyResponse';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  url = environment.api_url + '/users';

  constructor(private http: HttpClient) {
  }

  public getUser(id: number) {
    return this.http.get<User>(this.url + '/' + id);
  }

  public registerJourney(id: number, start: Coords, end: Coords, type: string) {
    console.log(id, start, end, type);
    return this.http.put<JourneyResponse>(
      this.url + '/' + id,
      {type, lat_start: start.lat, lon_start: start.lon, lat_end: end.lat, lon_end: end.lon}
    );
  }
}
