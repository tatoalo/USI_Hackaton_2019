import {Component, Input, OnInit} from '@angular/core';
import {MonsterService} from './services/monster.service';
import {PollutionService} from './services/pollution.service';
import {StationService} from './services/station.service';
import {UserService} from './services/user.service';
import {Observable} from 'rxjs';
import {User} from './models/User';
import {switchMap} from 'rxjs/operators';
import {Monster} from './models/Monster';
import {Coords} from './models/Coords';
import {MatTabChangeEvent} from '@angular/material';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [MonsterService, PollutionService, StationService, UserService],
})
export class AppComponent implements OnInit {
  title = 'web';

  user$: Observable<User>;
  private monster$: Observable<Monster>;
  selectedTab: number;
  start: Coords;
  end: Coords;

  constructor(private userService: UserService,
              private monsterService: MonsterService) {

  }

  ngOnInit() {
    this.user$ = this.userService.getUser(1);
    this.monster$ = this.user$.pipe(switchMap(
      u => this.monsterService.getMonster(u.current_fight.monster_id)
    ));
  }

  startSelected(coords: Coords) {
    this.start = coords;
  }

  endSelected(coords: Coords) {
    this.end = coords;
  }

  onSubmit() {

  }

  onTabChange($event: MatTabChangeEvent) {
    // switch ($event.index) {
    //   case 0: 'bike';
    //
    // }

  }
}
