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

  constructor(private authService: AuthService, private router: Router) {} // Inject Router

  register() {
    this.authService.register(this.user_name, this.user_type).subscribe(response => {
      console.log('Registered:', response);
      // Handle the response, e.g., navigate back to login
      this.router.navigate(['/login']); // Redirect to login
    });
  }
}