import { Component, OnInit } from '@angular/core';
import { TypeService } from 'src/app/services/type.service';

@Component({
  selector: 'app-add-type',
  templateUrl: './add-type.component.html',
  styleUrls: ['./add-type.component.css']
})
export class AddTypeComponent implements OnInit {
  type = {
    TYPEID: '',
    TYPEDISCRIPTION: ''
  };
  submitted = false;

  constructor(private typeService: TypeService) { }

  ngOnInit() {
  }

  saveType() {
    const data = {
      TYPEID: this.type.TYPEID,
      TYPEDISCRIPTION: this.type.TYPEDISCRIPTION
    };

    this.typeService.create(data)
      .subscribe(
        response => {
          console.log(response);
          this.submitted = true;
        },
        error => {
          console.log(error);
        });
  }

  newType() {
    this.submitted = false;
    this.type = {
      TYPEID: '',
      TYPEDISCRIPTION: ''
    };
  }
}


