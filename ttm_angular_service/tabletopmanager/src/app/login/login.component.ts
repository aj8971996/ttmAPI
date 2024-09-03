import { Component } from '@angular/core';
import { ApiService } from '../api.service';  // Ensure the correct service is imported
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private apiService: ApiService) {}  // Ensure ApiService is injected

  login() {
    this.apiService.addPlayerCharacter({ username: this.username, password: this.password })
      .subscribe({
        next: (response) => {
          console.log('Login successful', response);
        },
        error: (error) => {
          console.error('Login failed', error);
        },
      });
  }
}