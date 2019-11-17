import {Component, Input, OnInit} from '@angular/core';
import {Monster} from '../../models/Monster';
import {Fight} from '../../models/User';
import {MonsterService} from '../../services/monster.service';

@Component({
  selector: 'app-cars',
  templateUrl: './cars.component.html',
  styleUrls: ['./cars.component.css']
})
export class CarsComponent implements OnInit {

  constructor() {
  }

  ngOnInit() {
  }

  mapOnClick(event: MouseEvent) {
    console.log(event)
  }

}
