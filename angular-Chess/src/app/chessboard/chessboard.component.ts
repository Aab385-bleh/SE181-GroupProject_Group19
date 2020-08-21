import { Component, OnInit } from '@angular/core';
import { User } from '../classes/User';
import { WebSocketService } from '../services/web-socket.service';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';

@Component({
  selector: 'app-chessboard',
  templateUrl: './chessboard.component.html',
  styleUrls: ['./chessboard.component.css']
})
export class ChessboardComponent implements OnInit {
  ChessBoard: Board = new Board();
  asdf: Square = new Square();
  // Rows: string[] = ["1", "2", "3", "4", "5", "6", "7", "8"];
  Columns: string[] = ["a", "b", "c", "d", "e", "f", "g", "h"];
  Rows: number[] = [1, 2, 3, 4, 5, 6, 7, 8];
  whitePieces: string[] = ["k", "q", "r", "b", "n", "p"];
  blackPieces: string[] = ["K", "Q", "R", "B", "N", "P"];
  message: string;
  localUser: User; /*get name from gameroom which should emit
  something telling the user whether they are the first or second user*/
  otherUser: User; //have them get this from gameroom
  private menuRoom = "gameRoom" // Hardcoded GameRoom Name, change if neccesary

  constructor(public webSocketService: WebSocketService,
    public dialog: MatDialog) { }

  ngOnInit(): void { }

  startGame() {
    this.ChessBoard.createStartBoard();
  }

  getIcon(piece: string) {
    var icon: string = null;
    switch(piece) { 
      case "k": { 
         icon = "assets/Chess_klt45.svg";
         break; 
      } case "K": { 
        icon = "assets/Chess_kdt45.svg";
         break; 
      } case "q": { 
        icon = "assets/Chess_qlt45.svg";
         break; 
      } case "Q": { 
        icon = "assets/Chess_qdt45.svg";
         break; 
      } case "r": { 
        icon = "assets/Chess_rlt45.svg";
         break; 
      } case "R": { 
        icon = "assets/Chess_rdt45.svg";
         break; 
      } case "b": { 
        icon = "assets/Chess_blt45.svg";
         break; 
      } case "B": { 
        icon = "assets/Chess_bdt45.svg";
         break; 
      } case "n": { 
        icon = "assets/Chess_nlt45.svg";
         break; 
      } case "N": { 
        icon = "assets/Chess_ndt45.svg";
         break; 
      } case "p": { 
        icon = "assets/Chess_plt45.svg";
         break; 
      } case "P": { 
        icon = "assets/Chess_pdt45.svg";
         break; 
      }
      default: { 
        icon = "assets/BLANK_ICON.png";
         break; 
      } 
   }
   return icon;
  }

  /* TESTING ONLY */
  testBoard: string[][] = [
    ['.', 'n', 'b', 'q', 'k', '.', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'Q', '.', '.', '.', 'P', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', 'N'],
    ['.', '.', '.', '.', '.', '.', 'r', '.'],
    ['P', 'P', 'P', 'b', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', '.', 'K', 'B', '.', 'R']
  ];
  testUpdateBoard() { // testing only
    this.ChessBoard.updateBoard(this.testBoard);
  }
  /* END TESTING ONLY */

  isPieceChosen: boolean = false;
  pieceChosen: Square = null;
  isLocationChosen: boolean = false;
  locationChosen: Square = null;

  selectSquare(sq: Square) {
    if (!this.isPieceChosen) {
      if (sq.isOccupied) {
        this.isPieceChosen = true;
        sq.isSelected = true;
        this.pieceChosen = sq;
        // alert("Moving piece has been chosen.");
      } else {
        alert("Choose a square that's occupied.");
      }
    } else if (this.isPieceChosen) {
      if(sq.isOccupied && (this.pieceChosen == sq)) {
        // deselect
        this.pieceChosen.isSelected = false;
        this.isPieceChosen = false;
        this.pieceChosen = null;
        this.locationChosen.isSelected = false;
        this.isLocationChosen = false;
        this.locationChosen = null;
      }else if (sq.isOccupied && (this.pieceChosen != sq)) {
        if ((sq.Piece == sq.Piece.toLowerCase()) && (this.pieceChosen.Piece == this.pieceChosen.Piece.toLowerCase())) {
          alert("Invalid. Both selected squares contain pieces on the same team. (lower)");
        } else if ((sq.Piece == sq.Piece.toUpperCase()) && (this.pieceChosen.Piece == this.pieceChosen.Piece.toUpperCase())) {
          alert("Invalid. Both selected squares contain pieces on the same team. (upper)");
        } else {
          sq.isSelected = true;
          this.isLocationChosen = true;
          this.locationChosen = sq;
          // alert("move... 2");
          var newMove: Move = new Move(this.pieceChosen, this.locationChosen);
          this.attemptMove(newMove);
          // deselecting
          this.pieceChosen.isSelected = false;
          this.isPieceChosen = false;
          this.pieceChosen = null;
          this.locationChosen.isSelected = false;
          this.isLocationChosen = false;
          this.locationChosen = null;
        }
      } else {
        sq.isSelected = true;
        this.isLocationChosen = true;
        this.locationChosen = sq;
        // alert("move .. 3");
        var newMove: Move = new Move(this.pieceChosen, this.locationChosen);
        this.attemptMove(newMove);
        // deselecting
        this.pieceChosen.isSelected = false;
        this.isPieceChosen = false;
        this.pieceChosen = null;
        this.locationChosen.isSelected = false;
        this.isLocationChosen = false;
        this.locationChosen = null;
      }
    }
  }

  attemptMove(move: Move) {
    // alert("Attempting move...");

    var isMoveValid: boolean = this.validateMove(move); // validate

    if(isMoveValid) {
      move.newPosition.Piece = move.currentPosition.Piece;
      move.newPosition.isOccupied = true;
      
      move.currentPosition.Piece = '.';
      move.currentPosition.isOccupied = false;
    } else {
      alert("Move is not valid.");
    }

  }

  validateMove(move: Move) {
    // alert("Validating move...");
    // call python back end here ****************************
    // send Move object to back end *******************
    alert("Move is valid");
    return true;
  }

}

class Square {
  coordinates = "";
  IsWhite: boolean = true;
  Piece: string = null;
  isOccupied: boolean = false;
  isSelected: boolean = false;
}

class Move {
  currentPosition: Square = null;
  newPosition: Square = null;

  constructor(currpos: Square, newpos: Square) {
    this.currentPosition = currpos;
    this.newPosition = newpos;
  }

}

class Board {
  Rows = ["1", "2", "3", "4", "5", "6", "7", "8"];
  Columns = ["a", "b", "c", "d", "e", "f", "g", "h"];
  BoardMatrix: Square[][] = EmptyBoard.createEmptyBoard(this.Rows, this.Columns);
  
  createStartBoard() {
    var startBoard: string[][] = [
      ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
      ['.', '.', '.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.', '.', '.'],
      ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
      ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ];
    for (let i = 0; i < 8; i++) {
      for (let j = 0; j < 8; j++) {
        if (startBoard[i][j] != this.BoardMatrix[i][j].Piece) {
          this.BoardMatrix[i][j].Piece = startBoard[i][j];
          if(startBoard[i][j] != '.') {
            this.BoardMatrix[i][j].isOccupied = true;
          }
        }
      }
    }
  }

  updateBoard(newBoard: string[][]) {
    for (let i = 0; i < 8; i++) {
      for (let j = 0; j < 8; j++) {
        if (newBoard[i][j] != this.BoardMatrix[i][j].Piece) {
          this.BoardMatrix[i][j].Piece = newBoard[i][j];
          if(newBoard[i][j] != '.') {
            this.BoardMatrix[i][j].isOccupied = true;
          }
        }
      }
    }
  }
  
}

class EmptyBoard {
  static createEmptyBoard(rows: string[], columns: string[]) {
    var Squares: Square[][] = new Array<Square[]>(8);
    var isWhite: boolean = false;
    for (let i = 0; i < 8; i++) {
      Squares[i] = new Array<Square>(8);
      for (let j = 0; j < 8; j++) {
        Squares[i][j] = {
          coordinates: rows[i] + columns[j],
          IsWhite: isWhite,
          Piece: '.',
          isOccupied: false,
          isSelected: false
        };
        isWhite = !isWhite;
      }
      isWhite = !isWhite;
    }
    return Squares;
  }
}