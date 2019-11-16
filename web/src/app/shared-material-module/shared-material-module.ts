import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  MatButtonModule,
  MatCheckboxModule, MatChipsModule,
  MatDialogModule, MatFormFieldModule, MatIconModule, MatInputModule,
  MatProgressSpinnerModule,
  MatRippleModule, MatSnackBarModule, MatToolbarModule,
  MatTooltipModule
} from '@angular/material';
import {FormsModule} from '@angular/forms';



@NgModule({
  declarations: [],
  exports: [
    CommonModule,
    MatRippleModule,
    MatButtonModule,
    MatInputModule,
    MatChipsModule,
    FormsModule,
    MatIconModule,
    MatToolbarModule,
    MatFormFieldModule,
    MatSnackBarModule,
    MatProgressSpinnerModule,
    // FlexLayoutModule,
    MatCheckboxModule,
    MatTooltipModule,
    MatDialogModule,
  ]
})
export class SharedMaterialModule { }
