import {Component, Input, OnInit} from '@angular/core';
import {MonsterService} from './services/monster.service';
import {PollutionService} from './services/pollution.service';
import {StationService} from './services/station.service';
import {UserService} from './services/user.service';
import {User} from './models/User';
import {switchMap, tap} from 'rxjs/operators';
import {Monster} from './models/Monster';
import {Coords} from './models/Coords';
import {MatTabChangeEvent} from '@angular/material';

class CoordGroup {
  constructor() {
    this.bike = {start: undefined, end: undefined};
    this.walk = {start: undefined, end: undefined};
    this.car = {start: undefined, end: undefined};
    this.bus = {start: undefined, end: undefined};
  }

  bike: { start: Coords; end: Coords; };
  car: { start: Coords; end: Coords; };
  bus: { start: Coords; end: Coords; };
  walk: { start: Coords; end: Coords; };
}


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [MonsterService, PollutionService, StationService, UserService],
})
export class AppComponent implements OnInit {
  title = 'web';

  user: User;
  private monster: Monster;
  transportType = 'bike';
  selectedTab: number;
  coordGroup = new CoordGroup();

  constructor(private userService: UserService,
              private monsterService: MonsterService) {

  }

  ngOnInit() {
    this.userService.getUser(1).pipe(
      tap(u => this.user = u),
      switchMap(
        u => this.monsterService.getMonster(u.current_fight.monster_id)
      )).subscribe(m => this.monster = m);
  }

  startSelected(coords: Coords, type: string) {
    this.transportType = type;
    this.coordGroup[type].start = coords;
  }

  endSelected(coords: Coords, type: string) {
    this.transportType = type;
    this.coordGroup[type].end = coords;
  }

  onSubmit() {
    const start = this.coordGroup[this.transportType].start;
    const end = this.coordGroup[this.transportType].end;
    if (start && end) {
      this.userService.registerJourney(this.user.id, start, end, this.transportType).subscribe(
        u => {
          this.user = u.user;
          this.monster = u.monster;
        }
      );
    }
  }

  onTabChange($event: MatTabChangeEvent) {
    switch ($event.index) {
      case 0:
        this.transportType = 'bike';
        break;
      case 1:
        this.transportType = 'bus';
        break;
      case 2:
        this.transportType = 'car';
        break;
      case 3:
        this.transportType = 'walk';
        break;
    }

  }
}
