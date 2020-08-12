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
  
  //sends a req
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
    //socket.emit should stringify and ensure that gameinviteobject is automatically stringifyied
    //and parsed back into JSON object
    this.socket.emit('requestUserForGame', gameInviteObject);
  }

  //creates and returns observable of backend emiting event for client recieving invite requests
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
  /*this observable will also have to be subscribed to for the duration of the main menu unless
  user is limited to one active invite (as in an invite that they haven't received a response for) at a
  time */
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