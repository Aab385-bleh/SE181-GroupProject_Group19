import { Component, OnInit } from '@angular/core';
import { WebsocketService } from '../websocket.service';
import { PawnPromotionDialogComponent } from '../pawn-promotion-dialog/pawn-promotion-dialog.component';
// import { GameOverDialogComponent } from '../game-over-dialog/game-over-dialog.component'
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-chessboard',
  templateUrl: './chessboard.component.html',
  styleUrls: ['./chessboard.component.css']
})
export class ChessboardComponent implements OnInit {

  ChessBoard: Board = new Board();
  Columns: string[] = ["A", "B", "C", "D", "E", "F", "G", "H"];
  Rows: number[] = [1, 2, 3, 4, 5, 6, 7, 8];

  whoseTurn: string;
  localUser: string;
  isWhitePlayer: boolean;
  opposingPlayer: string;

  isPieceChosen: boolean = false;
  pieceChosen: Square = null;
  isLocationChosen: boolean = false;
  locationChosen: Square = null;

  constructor(private websocketservice: WebsocketService, public promotiondialog: MatDialog, public gameoverdialog: MatDialog) { }

  ngOnInit(): void {
    //test
    // this.isWhitePlayer = true;
  }

  startGame() {
    this.whoseTurn = "White";
    this.ChessBoard.createStartBoard();
  }

  // SEND MOVE TO WEBSOCKET SERVICE
  applyMove(move: Move) {
    move = this.checkForPawnPromotion(move);
    var coords = {
      "curX": move.currentPosition.coordinates[0],
      "curY": move.currentPosition.coordinates[1],
      "newX": move.newPosition.coordinates[0],
      "newY": move.newPosition.coordinates[1],
      "promotion": move.promotedPiece
    };
    alert("attempting to move: " + move.currentPosition.coordinates[0] + move.currentPosition.coordinates[1] + move.newPosition.coordinates[0]+ move.newPosition.coordinates[1]);
    this.websocketservice.applyMove(coords);

    return true;
  }

  checkForPawnPromotion(move: Move) {
    if ((move.currentPosition.piece.toLowerCase() == 'p') && this.isWhitePlayer && (move.newPosition.coordinates[0] == 7)) {  // white pawn promotion
      // continue
    } else if ((move.currentPosition.piece.toLowerCase() == 'p') && !this.isWhitePlayer && (move.newPosition.coordinates[0] == 0)) {  // black pawn promotion
      // continue
    } else {
      return move;
    }

    const dialogRef = this.promotiondialog.open(PawnPromotionDialogComponent, {
      width: '300px',
    });
    dialogRef.afterClosed().subscribe(response => {
      if (response) {
        alert("promoting pawn to " + response.promotedPiece);
        move.promotedPiece = response.promotedPiece;
      } else {
        console.error('Error! No response object recieved from PawnPromotion Dialog!');
      }
    });

    return move;

  }

  // GET REJECTED MOVE FROM WEBSOCKET SERVICE
  getRejectedMove() {
    this.websocketservice.getRejectedMove().subscribe(response => {
      if (response) {
        alert("Move is not valid. Please try again.");
      }
    });
  }

  // GET OBSERVABLE TO GET NEW BOARD FROM WEBSOCKET SERVICE
  getUpdatedBoard() {
    var updatedBoard: string[][];
    var playerTurn: string;
    var player: string;
    var winner: string;
    this.websocketservice.getUpdatedBoard().subscribe(response => {
      if (response) {
        updatedBoard = response.data.gameBoard;
        playerTurn = response.data.playerTurn;
        player = response.data.check;
        winner = response.data.winner;
        
        if (winner) {
          alert("GAME OVER. " + winner + " has won.");
          // TODO: fix game over dialog
          // const dialoggo = this.gameoverdialog.open(GameOverDialogComponent, {data: {theWinner: winner}});
          // dialoggo.afterClosed().subscribe(response => {
          //   if (response) {
          //     if(response.decision == 'startnew') {
          //       this.ChessBoard.createStartBoard(); // RESET BOARD
          //     }
          //   }
          // });
          
        } else {
          if (playerTurn = 'w') {
            this.whoseTurn = "White";
          } else if (playerTurn = 'b') {
            this.whoseTurn = "Black";
          }
          this.ChessBoard.updateBoard(updatedBoard);    // UPDATE BOARD
        }
      }
    },
    err => console.error('Observer for getting Board got an error: ' + err),
    () => console.log('Observer for getting Board got a complete notification'));
    
  }

  // GET USERNAME FROM WEBSOCKET SERVICE 
  getUserName() {
    this.websocketservice.getUserName().subscribe(response => {
      if (response) {
        this.localUser = response.userName;
        this.isWhitePlayer = response.isWhite;
        if (response.userName == 'Player 1') {
          this.opposingPlayer = 'Player 2';
        } else {
          this.opposingPlayer = 'Player 1';
        }
      }
    },
    err => console.error('Observer for getting Username got an error: ' + err),
    () => console.log('Observer for getting Username got a complete notification'));

  }

  // GET ICONS FOR PIECE
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



  // MAKING A MOVE
  selectSquare(sq: Square) {

    if (!this.isWhitePlayer && (this.whoseTurn == "White")) {
      alert("It is not your turn. Please wait.");
      return;
    } else if (this.isWhitePlayer && (this.whoseTurn == "Black")) {
      alert("It is not your turn. Please wait.");
      return;
    }

    if (!this.isPieceChosen) {
      if (sq.isOccupied) {
        this.isPieceChosen = true;
        sq.isSelected = true;
        this.pieceChosen = sq;
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
        if ((sq.piece == sq.piece.toLowerCase()) && (this.pieceChosen.piece == this.pieceChosen.piece.toLowerCase())) {
          alert("Invalid. Both selected squares contain pieces on the same team. (lower)");
        } else if ((sq.piece == sq.piece.toUpperCase()) && (this.pieceChosen.piece == this.pieceChosen.piece.toUpperCase())) {
          alert("Invalid. Both selected squares contain pieces on the same team. (upper)");
        } else {
          sq.isSelected = true;
          this.isLocationChosen = true;
          this.locationChosen = sq;

          var newMove: Move = new Move(this.pieceChosen, this.locationChosen, "none");
          this.applyMove(newMove);      // APPLY MOVE ***

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

        var newMove: Move = new Move(this.pieceChosen, this.locationChosen, "none");
        this.applyMove(newMove); // APPLY MOVE ***

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

}

class Square {
  coordinates: number[] = null;
  oddSquare: boolean = true;
  piece: string = null;
  isOccupied: boolean = false;
  isSelected: boolean = false;
}

class Move {
  currentPosition: Square = null;
  newPosition: Square = null;
  promotedPiece: string;

  constructor(currpos: Square, newpos: Square, promoted: string) {
    this.currentPosition = currpos;
    this.newPosition = newpos;
    this.promotedPiece = promoted;
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
        if (startBoard[i][j] != this.BoardMatrix[i][j].piece) {
          this.BoardMatrix[i][j].piece = startBoard[i][j];
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
        if (newBoard[i][j] != this.BoardMatrix[i][j].piece) {
          this.BoardMatrix[i][j].piece = newBoard[i][j];
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
    var isOddSquare: boolean = false;
    for (let i = 0; i < 8; i++) {
      Squares[i] = new Array<Square>(8);
      for (let j = 0; j < 8; j++) {
        Squares[i][j] = {
          // coordinates: rows[i] + columns[j],
          coordinates: [i, j],
          oddSquare: isOddSquare,
          piece: '.',
          isOccupied: false,
          isSelected: false
        };
        isOddSquare = !isOddSquare;
      }
      isOddSquare = !isOddSquare;
    }
    return Squares;
  }
}