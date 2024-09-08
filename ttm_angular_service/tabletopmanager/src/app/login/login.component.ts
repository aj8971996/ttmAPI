import { Component } from '@angular/core';
import { Router } from '@angular/router'; // Import the Router for navigation
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [FormsModule],
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private router: Router) {} // Inject the Router

  login() {
    console.log('Username:', this.username);
    console.log('Password:', this.password);
    // Add login logic here
  }

  goToRegister() {
    this.router.navigate(['/register']); // Navigate to the registration page
  }
}