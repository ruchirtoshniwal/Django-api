import { Component, OnInit } from '@angular/core';

import { TypeService } from 'src/app/services/type.service';

@Component({
  selector: 'app-type-list',
  templateUrl: './type-list.component.html',
  styleUrls: ['./type-list.component.css']
})
export class TypeListComponent implements OnInit {

  type: any;
  currentType = null;
  currentIndex = -1;
  TYPEID = '';

  constructor(private typeService: TypeService) { }

  ngOnInit() {
    this.retrieveType();
  }
   retrieveType() {
    this.typeService.getAll()
      .subscribe(
        data => {
          this.type = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  refreshList() {
    this.retrieveType();
    this.currentType = null;
    this.currentIndex = -1;
  }

  setActiveType(type, index) {
    this.currentType = type;
    this.currentIndex = index;
  }

  removeAllType() {
    this.typeService.deleteAll()
      .subscribe(
        response => {
          console.log(response);
          this.retrieveType();
        },
        error => {
          console.log(error);
        });
  }
}



