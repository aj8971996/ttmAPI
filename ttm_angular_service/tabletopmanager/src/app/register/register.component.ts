import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router'; // Import Router for navigation
import { CommonModule } from '@angular/common'; // Import CommonModule for *ngIf

@Component({
  selector: 'app-register',
  standalone: true,
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  imports: [FormsModule, CommonModule], // Ensure CommonModule is included for *ngIf
})
export class RegisterComponent {
  user_name: string = '';
  user_type: string = ''; // You can define whether they are GM or Player here
  password: string = '';
  confirm_password: string = ''; // Add confirm password field
  passwordsMatch: boolean = true; // A flag to track if passwords match
  errorMessage: string = ''; // Error message

  constructor(private authService: AuthService, private router: Router) {} // Inject Router

  // Method to check if passwords match
  checkPasswordsMatch() {
    this.passwordsMatch = this.password === this.confirm_password;
  }

  register() {
    if (this.passwordsMatch) {
      // Call the registration service only if passwords match
      this.authService.register(this.user_name, this.password, this.user_type).subscribe(
        (response) => {
          console.log('Registered:', response);
          // Handle the response, e.g., navigate back to login
          this.router.navigate(['/login']); // Redirect to login
        },
        (error) => {
          console.error('Registration failed:', error);
          this.errorMessage = 'Registration failed. Please try again.';
        }
      );
    } else {
      this.errorMessage = 'Passwords do not match!';
    }
  }
}