import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BikeStationsComponent } from './bike-stations.component';

describe('BikeStationsComponent', () => {
  let component: BikeStationsComponent;
  let fixture: ComponentFixture<BikeStationsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BikeStationsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BikeStationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
