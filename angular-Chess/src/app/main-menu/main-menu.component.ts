import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { WebSocketService } from '../services/web-socket.service';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { User } from '../classes/User'
import { InvitePopupComponent } from '../invite-popup/invite-popup.component';

@Component({
  selector: 'app-mainMenu',
  templateUrl: './main-menu.component.html',
  styleUrls: ['./main-menu.component.css']
})

export class MainMenuComponent implements OnInit {
  localUser: User;
  selectedUser: User;
  userList: User[];
  private menuRoom = "menuRoom" // Hardcoded MenuRoom Name

  constructor(public webSocketService: WebSocketService,
    public dialog: MatDialog) { }

    ngOnInit() {
      this.localUser = new User('DefaultDan');
      this.webSocketService.joinRoom(this.menuRoom);
      this.getUsers();
      this.webSocketService.getGameInvitesObservable().subscribe(response => {
        if (response) {
          this.openGameInviteDialog(response.invitee);
        }
      },
      err => console.error('Observer for InviteReception got an error: ' + err), 
      () => console.log('Observer for InviteReception got a complete notification'));
    }

    getUsers() {
      this.webSocketService.getConnectedUsers('director').subscribe(response => {
        if (response) {
          //Response is Json, have to convert json into proper format
          /*only concievable way to convert Json data into Userobjects is add way to make 
          users with an ID input*/
          this.userList = response;
        }
      },
      //add something to find and remove localUser from the list here later
      //or maybe just have the html omit/skip it if possible
      err => console.error('Observer for getting Users got an error: ' + err),
      () => console.log('Observer for getting Users got a complete notification'));
    }
    
    requestUserForGame(invitee: User) {
      var gameInviteObject = {
        User
      }
    }

    openGameInviteDialog(user: User) {
      const dialogConfig = new MatDialogConfig();
      var dialogRef;

      dialogConfig.disableClose = true;
      dialogConfig.autoFocus = true;
      dialogConfig.width = '300px';

      dialogConfig.data = {
        name: user.name
      };
      dialogRef = this.dialog.open(InvitePopupComponent, dialogConfig);

      dialogRef.afterClosed().subscribe(response => {
        if (response) {
          if (response.acceptInvite == true) {

          } else if (response.acceptInvite == false){

          } else {
            console.error(`Error! Response object recieved from invite-popup Dialog either has 
            no "acceptInvite" property or acceptInvite property was not set`);
          }
        } else {
          console.error('Error! No response object recieved from invite-popup Dialog');
        }
      });
    }
}