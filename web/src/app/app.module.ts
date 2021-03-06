import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AgmCoreModule } from '@agm/core'; 

import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import {SharedMaterialModule} from './shared-material-module/shared-material.module';
import { UserComponent } from './components/user/user.component';
import { MonsterComponent } from './components/monster/monster.component';
import {MatTabsModule} from '@angular/material';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { BikeStationsComponent } from './components/bike-stations/bike-stations.component';
import { CarsComponent } from './components/cars/cars.component';
import { WalksComponent } from './components/walks/walks.component';
import {FormsModule} from '@angular/forms';
import { TplStationsComponent } from './components/tpl-stations/tpl-stations.component';
import { PollutionComponent } from './components/pollution/pollution.component';

@NgModule({
  declarations: [
    AppComponent,
    UserComponent,
    MonsterComponent,
    BikeStationsComponent,
    CarsComponent,
    TplStationsComponent,
    PollutionComponent,
    WalksComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    SharedMaterialModule,
    AgmCoreModule.forRoot({apiKey: 'AIzaSyAXhPJlnQqYaN1kYyBF3bTEEesQKQ9Qhfg'})
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
