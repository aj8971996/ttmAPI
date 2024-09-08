import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router'; // Import Router for navigation

@Component({
  selector: 'app-register',
  standalone: true,
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  imports: [FormsModule],
})
export class RegisterComponent {
  user_name: string = '';
  user_type: string = ''; // You can define whether they are GM or Player here
  password: string = '';
  confirm_password: string = ''; // Add confirm password field
  passwordsMatch: boolean = true; // A flag to track if passwords match

  constructor(private authService: AuthService, private router: Router) {} // Inject Router

  // Method to check if passwords match
  checkPasswordsMatch() {
    this.passwordsMatch = this.password === this.confirm_password;
  }

  register() {
    if (this.passwordsMatch) {
      // Call the registration service only if passwords match
      this.authService.register(this.user_name, this.password, this.user_type).subscribe((response) => {
        console.log('Registered:', response);
        // Handle the response, e.g., navigate back to login
        this.router.navigate(['/login']); // Redirect to login
      });
    } else {
      alert('Passwords do not match!'); // Display alert if passwords don't match
    }
  }
}