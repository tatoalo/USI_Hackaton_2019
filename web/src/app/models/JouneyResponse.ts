/* tslint:disable:variable-name */
import {User} from './User';
import {Monster} from './Monster';

export class JourneyResponse {
  user: User;
  monster: Monster;
  distance: number;
  fuel_saved: number;
}
