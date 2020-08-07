import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import * as io from 'socket.io-client';

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
      return () => {
        this.socket.disconnect();
      };
    });
  }

  
  addOrUpdateUser(userStub: any, menuRoom: string) {
    this.socket.emit('addOrUpdateUser', userStub, menuRoom);
  }




}