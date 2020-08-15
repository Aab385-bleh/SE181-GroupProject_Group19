import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import * as io from 'socket.io-client';
import { User } from '../classes/User';

@Injectable({
  providedIn: 'root'
})
export class WebSocketService {

  private url = 'http://localhost:8089'; //change this to whatever URl the backend will be one
  private socket: any;

  constructor() {
    this.socket = io(this.url);
  }

  joinRoom(roomName: string) {
    this.socket.emit('join_room', roomName);
  }
  
  leaveRoom(roomName: string) {
    this.socket.emit('leave_room', roomName)
  }
  
  //sends a request for list of connected Users from server adn creates and returns observable for
  //getConnectedUsersUpdate emission
  /*JSON Object emitted with "getGameInvites" should look like 
  data = {
   'users': [{
      'name': 'John',
      'id': '4337b01a-7ff8-47b9-80aa-d5b734b4ec13'
    }, 
    {
      'name': 'DefaultDan',
      'id': '9a014117-bda0-412f-9ec1-5fa4273a1257'
    }]
  }*/
  getConnectedUsers(menuRoom: string) {
    this.socket.emit('getConnectedUsers', menuRoom);
    return Observable.create((observer) => {
      this.socket.on('getConnectedUsersUpdate', (data) => {
        if (data) {
          observer.next(data);
        } else {
          observer.error('Unable To Reach Server');
        }
      });
      //cleanup logic
      return () => {
        this.socket.disconnect();
      };
    });
  }

  addOrUpdateUser(userStub: any, menuRoom: string) {
    this.socket.emit('addOrUpdateUser', userStub, menuRoom);
  }

  requestUserForGame(inviter: User, invitee: User) {
    var gameInviteObject = {
      inviter: inviter,
      invitee: invitee
    };
    //socket.emit should stringify and ensure that gameInviteObject is automatically stringifyied
    //and parsed back into JSON object
    this.socket.emit('requestUserForGame', gameInviteObject);
  }

  sendGameInviteResponse(inviter: User, invitee: User, inviteAccepted: boolean)
  {
    var gameInviteResponseObject = {
      inviter: inviter,
      invitee: invitee,
      inviteAccepted: inviteAccepted,
    };

    this.socket.emit('sendGameInviteResponse', gameInviteResponseObject);
  }

  //creates and returns observable of backend emiting event for client recieving invite requests
  /*JSON Object emitted with "getGameInvites" should look like 
  data = { 
    'inviter': { 
      'name': 'John',
      'id': '4337b01a-7ff8-47b9-80aa-d5b734b4ec13'
    },
    'invitee': {
      'name': 'DefaultDan',
      'id': '9a014117-bda0-412f-9ec1-5fa4273a1257'
    }
  } 
  */
  getGameInvitesObservable() {
    return Observable.create((observer) => {
      this.socket.on('getGameInvites', (data) => {
        if (data) {
          observer.next(data);
        } else {
          observer.error('Unable To Reach Server');
        }
      });
      //cleanup Logic
      return () => {
        this.socket.disconnect();
      };
    });
  }

  //creates and returns observable for recieving responses of invite requests
  /*Addendum: possible to use this observable for sending the new Game's roomname as well, by emitting 
  an optional string with it that will contain.*/
  /*JSON Object emitted with "getGameInviteResponses" should look like 
  data = { 
    'inviter': { 
      'name': 'John',
      'id': '4337b01a-7ff8-47b9-80aa-d5b734b4ec13'
    },
    'invitee': {
      'name': 'DefaultDan',
      'id': '9a014117-bda0-412f-9ec1-5fa4273a1257'
    },
    'inviteAccepted': 'true',
    'gameRoomName': 'whatever'
  } 
  */
  getGameInviteResponsesObservable() {
    return Observable.create((observer) => {
      this.socket.on('getGameInviteResponses', (data) => {
        if (data) {
          observer.next(data);
        } else {
          observer.error('Unable To Reach Server');
        }
      });
      //cleanup Logic
      return () => {
        this.socket.disconnect();
      };
    });
  }
}