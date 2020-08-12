import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { WebSocketService } from '../services/web-socket.service';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { User } from '../classes/User'
import { InvitePopupComponent } from '../invite-popup/invite-popup.component';
import { Guid } from "guid-typescript";

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
          //Response is Json, have to convert json into proper Object
          /*Expecting Response to look something like this
          response = {'users': [{
              'name': 'John',
              'id': '4337b01a-7ff8-47b9-80aa-d5b734b4ec13'
            }, 
            {
              'name': 'default Dan',
              'id': '9a014117-bda0-412f-9ec1-5fa4273a1257'
            }]
            }*/
            var newUserList: User[] = [];
            for (var i in response.users) {
              var user = new User(response.users[i].name, Guid.parse(response.users[i].id));
              this.userList.push(user);
            }
        }
      },
      //add something to find and remove localUser from the list here later
      //or maybe just have the html omit/skip it if possible
      err => console.error('Observer for getting Users got an error: ' + err),
      () => console.log('Observer for getting Users got a complete notification'));
    }
    
    requestUserForGame(invitedUser: User) {
      this.webSocketService.requestUserForGame(this.localUser, invitedUser);
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