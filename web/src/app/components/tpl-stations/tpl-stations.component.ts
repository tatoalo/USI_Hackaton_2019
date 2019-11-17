import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import {BikeStation} from '../../models/BikeStation';
import {Coords} from '../../models/Coords';
import {StationService} from '../../services/station.service';
import {TplStation} from '../../models/TplStation';

@Component({
  selector: 'app-tpl-stations',
  templateUrl: './tpl-stations.component.html',
  styleUrls: ['./tpl-stations.component.css']
})
export class TplStationsComponent implements OnInit {

  tplStations: TplStation[];
  selectedStart: TplStation;
  selectedEnd: TplStation;

  @Output() startSelected: EventEmitter<Coords> = new EventEmitter();
  @Output() endSelected: EventEmitter<Coords> = new EventEmitter();

  constructor(private stationService: StationService) {
  }

  ngOnInit() {
    this.stationService.getAllTPLStations().subscribe(b => this.tplStations = b);
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
