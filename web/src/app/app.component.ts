import { Component } from '@angular/core';
import { MonsterService } from "./services/monster.service";
import { PollutionService } from "./services/pollution.service";
import { StationService } from "./services/station.service";
import { UserService } from "./services/user.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [MonsterService, PollutionService, StationService, UserService],
})
export class AppComponent {
  title = 'web';
}
