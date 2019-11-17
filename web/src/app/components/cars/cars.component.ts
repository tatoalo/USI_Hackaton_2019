import {Component, OnInit, EventEmitter, Output} from '@angular/core';
import {Monster} from '../../models/Monster';
import {Fight} from '../../models/User';
import {MonsterService} from '../../services/monster.service';
import { Coords } from 'src/app/models/Coords';

@Component({
  selector: 'app-cars',
  templateUrl: './cars.component.html',
  styleUrls: ['./cars.component.css']
})
export class CarsComponent implements OnInit {

  private startPoint: Coords;
  private endPoint: Coords;

  @Output() startSelected: EventEmitter<Coords> = new EventEmitter();
  @Output() endSelected: EventEmitter<Coords> = new EventEmitter();

  constructor() {
  }

  ngOnInit() {
  }

  mapOnClick(event: MouseEvent) {
    if (!this.startPoint) {
      this.startPoint = new Coords(event["coords"]["lat"], event["coords"]["lng"]);
      this.startSelected.emit(this.startPoint);
    } else {
      this.endPoint = new Coords(event["coords"]["lat"], event["coords"]["lng"]);
      this.endSelected.emit(this.endPoint);
    }
  }

  onSubmit() {
    this.startPoint = null;
    this.endPoint = null;
  }

}
