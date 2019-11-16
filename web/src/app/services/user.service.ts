import {Injectable} from '@angular/core';
import {HttpClient } from '@angular/common/http';
import {environment} from '../../environments/environment';
import {User} from '../models/User';

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

}
