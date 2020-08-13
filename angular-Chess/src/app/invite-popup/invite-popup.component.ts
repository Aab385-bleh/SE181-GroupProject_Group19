import { Component, OnInit, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { FormControl, Validators, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-invite-popup',
  templateUrl: './invite-popup.component.html',
  styleUrls: ['./invite-popup.component.css']
})
export class InvitePopupComponent implements OnInit {

  inviteResponseForm: FormGroup;
  inviteAccepted: boolean;
  senderName: string;

  constructor(public dialogRef: MatDialogRef<InvitePopupComponent>,
    @Inject(MAT_DIALOG_DATA) data) {
      this.senderName = data.name;
  }

  ngOnInit() { }

  respondToInvite(value: string) {
    if (value == 'true') {
      this.inviteAccepted = true;
    } else {
      this.inviteAccepted = false;
    }
    this.closeDialog();
  }

  closeDialog() {
    if (this.inviteAccepted != null) {
      this.dialogRef.close({
        inviteAccepted: this.inviteAccepted,
      });
    }
  }

}