import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router'; // Import Router for navigation
import { CommonModule } from '@angular/common'; // Import CommonModule for *ngIf

@Component({
  selector: 'app-view-gm',
  standalone: true,
  templateUrl: './view-gm.component.html',
  styleUrls: ['./view-gm.component.css'],
  imports: [FormsModule, CommonModule], // Ensure CommonModule is included for *ngIf
})
export class ViewGmComponent {

  constructor(private authService: AuthService, private router: Router) {}

  // Navigate to manage characters (placeholder for actual functionality)
  manageCharacters() {
    // Navigate to character management page or feature
  }

  // Navigate to manage abilities (placeholder for actual functionality)
  manageAbilities() {
    // Navigate to ability management page or feature
  }

  // Logout and navigate back to login page
  logout() {
    this.authService.logout(); // Clear authentication
    this.router.navigate(['/login']); // Redirect to login page
  }
}