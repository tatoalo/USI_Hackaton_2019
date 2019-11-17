import {Component, OnInit, EventEmitter, Output, Input, OnChanges, SimpleChanges} from '@angular/core';
import {Coords} from 'src/app/models/Coords';

@Component({
  selector: 'app-walks',
  templateUrl: './walks.component.html',
  styleUrls: ['./walks.component.css']
})
export class WalksComponent implements OnInit, OnChanges {

  @Input() dirty;
  private startPoint: Coords;
  private endPoint: Coords;

  @Output() startSelected: EventEmitter<Coords> = new EventEmitter();
  @Output() endSelected: EventEmitter<Coords> = new EventEmitter();

  constructor() {
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes.dirty.previousValue && !changes.dirty.currentValue) {
      this.onSubmit();
    }
  }

  ngOnInit() {
  }

  mapOnClick(event: MouseEvent) {
    if (!this.startPoint) {
      this.startPoint = new Coords(event['coords']['lat'], event['coords']['lng']);
      this.startSelected.emit(this.startPoint);
    } else {
      this.endPoint = new Coords(event['coords']['lat'], event['coords']['lng']);
      this.endSelected.emit(this.endPoint);
    }
  }

  onSubmit() {
    this.startPoint = null;
    this.endPoint = null;
  }

}
