import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-register',
  standalone: true,
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  imports: [FormsModule],
})
export class RegisterComponent {
  user_name: string = '';
  user_type: string = ''; // "GM" or "Player"

  constructor(private authService: AuthService) {}

  register() {
    // Validate that user_type is either "GM" or "Player"
    if (this.user_type !== 'GM' && this.user_type !== 'Player') {
      console.error('Invalid user type selected');
      return;
    }

    this.authService.register(this.user_name, this.user_type).subscribe(
      (response) => {
        console.log('Registered:', response);
        // Handle the response, e.g., store user info, navigate, etc.
      },
      (error) => {
        console.error('Registration failed:', error);
        // Handle registration failure
      }
    );
  }
}