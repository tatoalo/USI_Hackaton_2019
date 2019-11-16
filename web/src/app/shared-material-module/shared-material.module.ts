import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  MatButtonModule,
  MatCheckboxModule, MatChipsModule,
  MatDialogModule, MatDividerModule, MatFormFieldModule, MatIconModule, MatInputModule, MatProgressBarModule,
  MatProgressSpinnerModule,
  MatRippleModule, MatSelectModule, MatSnackBarModule, MatTabsModule, MatToolbarModule,
  MatTooltipModule
} from '@angular/material';
import {FormsModule} from '@angular/forms';



@NgModule({
  declarations: [],
  exports: [
    CommonModule,
    MatRippleModule,
    MatButtonModule,
    MatSelectModule,
    MatInputModule,
    MatChipsModule,
    FormsModule,
    MatProgressBarModule,
    MatIconModule,
    MatToolbarModule,
    MatFormFieldModule,
    MatDividerModule,
    MatSnackBarModule,
    MatProgressSpinnerModule,
    MatTabsModule,
    // FlexLayoutModule,
    MatCheckboxModule,
    MatTooltipModule,
    MatDialogModule,
  ]
})
export class SharedMaterialModule { }
