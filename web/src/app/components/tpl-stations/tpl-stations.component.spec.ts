import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TplStationsComponent } from './tpl-stations.component';

describe('TplStationsComponent', () => {
  let component: TplStationsComponent;
  let fixture: ComponentFixture<TplStationsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TplStationsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TplStationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
