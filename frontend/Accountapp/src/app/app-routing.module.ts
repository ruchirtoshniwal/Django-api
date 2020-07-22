import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { AddTypeComponent } from './components/add-type/add-type.component';
import { TypeDetailsComponent } from './components/type-details/type-details.component';
import { TypeListComponent } from './components/type-list/type-list.component';

const routes: Routes = [
  { path: '', redirectTo: '', pathMatch: 'full' },
  { path: 'type', component: TypeListComponent },
  { path: 'type/add', component: AddTypeComponent },
  { path: 'type/:id', component: TypeDetailsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
