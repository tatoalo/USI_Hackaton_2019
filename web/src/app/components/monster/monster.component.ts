import {Component, Input, OnInit} from '@angular/core';
import {Monster} from '../../models/Monster';
import {MonsterService} from '../../services/monster.service';

@Component({
  selector: 'app-monster',
  templateUrl: './monster.component.html',
  styleUrls: ['./monster.component.css']
})
export class MonsterComponent implements OnInit {

  @Input() monster: Monster;

  constructor() {
  }

  ngOnInit() {
  }

}
