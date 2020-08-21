import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ChessboardComponent } from './chessboard/chessboard.component';


const routes: Routes = [
  { path: '', redirectTo: '/chessboard', pathMatch: 'full'},
  { path: 'chessboard', component: ChessboardComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
