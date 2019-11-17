import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PollutionComponent } from './pollution.component';

describe('PollutionComponent', () => {
  let component: PollutionComponent;
  let fixture: ComponentFixture<PollutionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PollutionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PollutionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
