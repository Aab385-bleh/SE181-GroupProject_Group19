import { Component, OnInit, Inject } from '@angular/core';
import { MatDialog, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-game-over-dialog',
  templateUrl: './game-over-dialog.component.html',
  styleUrls: ['./game-over-dialog.component.css']
})
export class GameOverDialogComponent implements OnInit {

  constructor(@Inject(MAT_DIALOG_DATA) public data: string) { }

  ngOnInit() {
  }

  // startnew: string;
  // willStartNew() {

  // }

  closeDialog() {
    // if (this.promotionForm.valid) {
      // this.dialog.close({
      //   decision: 'startnew',
      // });
    // }
  }

}
