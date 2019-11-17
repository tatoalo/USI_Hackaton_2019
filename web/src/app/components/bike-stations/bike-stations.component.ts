import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {BikeStation} from '../../models/BikeStation';
import {StationService} from '../../services/station.service';
import {Coords} from '../../models/Coords';

@Component({
  selector: 'app-bike-stations',
  templateUrl: './bike-stations.component.html',
  styleUrls: ['./bike-stations.component.css']
})
export class BikeStationsComponent implements OnInit {
  bikeStations: BikeStation[];
  selectedStart: BikeStation;
  selectedEnd: BikeStation;

  @Output() startSelected: EventEmitter<Coords> = new EventEmitter();
  @Output() endSelected: EventEmitter<Coords> = new EventEmitter();

  constructor(private stationService: StationService) {
  }

  ngOnInit() {
    this.stationService.getAllBikeStations().subscribe(b => this.bikeStations = b);
  }

  onStartSelect(selection: BikeStation) {
    if (selection) {
      this.startSelected.emit(selection.coords);
    }
  }

  onEndSelect(selection: BikeStation) {
    if (selection) {
      this.endSelected.emit(selection.coords);
    }
  }
}
