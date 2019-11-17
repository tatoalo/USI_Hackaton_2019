import {Component, OnInit} from '@angular/core';
import {Pollution} from '../../models/Pollution';
import {PollutionService} from '../../services/pollution.service';

const COLORS = {
  very_poor: '#F44336',
  poor: '#FF5722',
  moderate: '#FFC107',
  good: '#8BC34A',
};

const THRESHOLDS = {
  NO: {
    very_poor: 401,
    poor: 135,
    moderate: 68,
  },
  NO2: {
    very_poor: 401,
    poor: 135,
    moderate: 68,
  },
  O3: {
    very_poor: 161,
    poor: 67,
    moderate: 34,
  },
  PM10: {
    very_poor: 76,
    poor: 34,
    moderate: 17,
  }
};

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

  getColor(val: number, type: string) {
    if (val > THRESHOLDS[type].very_poor) {
      return COLORS.very_poor;
    } else if (val > THRESHOLDS[type].poor) {
      return COLORS.poor;
    } else if (val > THRESHOLDS[type].moderate) {
      return COLORS.moderate;
    } else {
      return COLORS.good;
    }
  }
}
