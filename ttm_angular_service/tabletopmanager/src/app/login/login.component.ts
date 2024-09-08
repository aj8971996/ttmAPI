import { Component } from '@angular/core';
import { Router } from '@angular/router'; // Router for navigation
import { FormsModule } from '@angular/forms';
import { AuthService } from '../auth.service'; // Import AuthService
import { CommonModule } from '@angular/common'; // Import CommonModule for ngIf and other common directives

@Component({
  selector: 'app-login',
  standalone: true,
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [FormsModule, CommonModule], // Ensure CommonModule is imported
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  errorMessage: string = ''; // To show error messages

  constructor(private authService: AuthService, private router: Router) {} // Inject Router and AuthService

  login() {
    if (!this.username || !this.password) {
      this.errorMessage = 'Username and password are required';
      return;
    }

    this.authService.login(this.username, this.password).subscribe(
      (response) => {
        // Handle the login response
        const userType = response.user_type; // Assuming response contains user_type
        const token = response.access_token; // Assuming response contains access_token

        if (token) {
          // Store the token for authentication persistence
          localStorage.setItem('token', token);
          
          // Navigate based on user type
          if (userType === 'GM') {
            this.router.navigate(['/view-gm']);
          } else if (userType === 'Player') {
            this.router.navigate(['/view-player']);
          }
        }
      },
      (error) => {
        console.error('Login failed:', error);
        this.errorMessage = 'Login failed. Please check your credentials.';
      }
    );
  }

  goToRegister() {
    this.router.navigate(['/register']); // Navigate to the registration page
  }
}