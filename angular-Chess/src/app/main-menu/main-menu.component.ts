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
          var inviter = new User(response.inviter.name, response.inviter.id);
          this.openGameInviteDialog(inviter);
        }
      },
      err => console.error('Observer for InviteReception got an error: ' + err), 
      () => console.log('Observer for InviteReception got a complete notification'));
    
    this.webSocketService.getGameInviteResponsesObservable().subscribe(response => {
        if (response) {
          /*TODO: In case of invite not being accepted, make popup for User to let them know that their
          invite to X User was rejected (or failed due to an error with the invite modal on their end)
          make method for opening a GameBoard component in a new tab and join room with roomname given in
          "response", as that while be the name of the room where the users will emit their moves for the game*/
          

        }
      },
      err => console.error('Observer for InviteResponseReception got an error: ' + err), 
      () => console.log('Observer for InviteResponseReception got a complete notification'));
  }

  getUsers() {
    this.webSocketService.getConnectedUsers('director').subscribe(response => {
      if (response) {
        //Response is Json, have to convert json into proper Object
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

  openGameInviteDialog(inviter: User) {
    const dialogConfig = new MatDialogConfig();
    var dialogRef;

    dialogConfig.disableClose = true;
    dialogConfig.autoFocus = true;
    dialogConfig.width = '300px';

    dialogConfig.data = {
      name: inviter.name
    };
    dialogRef = this.dialog.open(InvitePopupComponent, dialogConfig);

    dialogRef.afterClosed().subscribe(response => {
      //can't do just if (response.inviteAccepted) because it's a boolean so it will fail if it is fals
      if (response) {
        if (typeof response.inviteAccepted === 'boolean') {
          this.webSocketService.sendGameInviteResponse(inviter, this.localUser, response.inviteAccepted);
        } else {
          console.error(`Error! Response object recieved from invite-popup Dialog either has 
          no "inviteAccepted" property or inviteAccepted property's value was never set.`);

          //other user should stil get a response
          this.webSocketService.sendGameInviteResponse(inviter, this.localUser, false);  
        }
      } else {
        console.error('Error! No response object recieved from invite-popup Dialog');

        //other user should stil get a response
        this.webSocketService.sendGameInviteResponse(inviter, this.localUser, false);
      }
    });
  }

  //
 // reactToInviteResponse()
}