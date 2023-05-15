import { Component, Input, OnInit, Output,EventEmitter } from '@angular/core';

@Component({
  selector: 'app-todo-item',
  templateUrl: './todo-item.component.html',
  styleUrls: ['./todo-item.component.css']
})
export class TodoItemComponent implements OnInit {
  @Input() todo:task | null = null
  @Output() todoDelete : EventEmitter<task | null> = new EventEmitter()
  constructor() {  }

  ngOnInit(): void {
  }
  onClick(todo:task | null ){
    this.todoDelete.emit(todo)
    console.log('onClick has been triggered');
  }
}
