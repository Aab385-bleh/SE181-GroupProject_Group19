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
  acceptInvite: boolean;
  senderName: string;

  constructor(public dialogRef: MatDialogRef<InvitePopupComponent>,
    @Inject(MAT_DIALOG_DATA) data) {
      this.senderName = data.name;
  }

  ngOnInit() { }

  respondToInvite(value: string) {
    if (value == 'true') {
      this.acceptInvite = true;
    } else {
      this.acceptInvite = false;
    }
    this.closeDialog();
  }

  closeDialog() {
    if (this.acceptInvite != null) {
      this.dialogRef.close({
        acceptInvite: this.acceptInvite,
      });
    }
  }

}