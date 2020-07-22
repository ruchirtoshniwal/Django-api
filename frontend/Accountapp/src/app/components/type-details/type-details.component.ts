import { Component, OnInit } from '@angular/core';
import { TypeService } from 'src/app/services/type.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-type-details',
  templateUrl: './type-details.component.html',
  styleUrls: ['./type-details.component.css']
})
export class TypeDetailsComponent implements OnInit {
  currentType = null;
  message = '';

  constructor(
    private typeService: TypeService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit() {
    this.message = '';
    this.getType(this.route.snapshot.paramMap.get('id'));
  }

  getType(id) {
    this.typeService.get(id)
      .subscribe(
        data => {
          this.currentType = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  updateType() {
    this.typeService.update(this.currentType.TYPEID, this.currentType)
      .subscribe(
        response => {
          console.log(response);
          this.message = 'The type was updated successfully!';
        },
        error => {
          console.log(error);
        });
  }

  deleteType() {
    this.typeService.delete(this.currentType.TYPEID)
      .subscribe(
        response => {
          console.log(response);
          this.router.navigate(['/type']);
        },
        error => {
          console.log(error);
        });
  }
}
