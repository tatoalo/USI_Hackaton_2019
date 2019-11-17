import {Component, OnInit} from '@angular/core';
import {Pollution} from '../../models/Pollution';
import {PollutionService} from '../../services/pollution.service';

@Component({
  selector: 'app-pollution',
  templateUrl: './pollution.component.html',
  styleUrls: ['./pollution.component.css']
})
export class PollutionComponent implements OnInit {
  pollution: Pollution;

  constructor(private pollutionService: PollutionService) {
  }

  ngOnInit() {
    this.pollutionService.getCurrentPollution().subscribe(p => this.pollution = p);
  }

}
