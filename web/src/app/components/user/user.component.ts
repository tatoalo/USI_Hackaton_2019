import {Component, Input, OnInit} from '@angular/core';
import {Observable, of} from 'rxjs';
import {User} from '../../models/User';
import {UserService} from '../../services/user.service';


@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.css']
})
export class UserComponent implements OnInit {

  constructor() {
  }

  @Input() user: User;

  ngOnInit() {
  }

}
