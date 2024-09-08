import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router'; // Import Router for navigation
import { CommonModule } from '@angular/common'; // Import CommonModule for *ngIf

@Component({
  selector: 'app-view-player',
  standalone: true,
  templateUrl: './view-player.component.html',
  styleUrls: ['./view-player.component.css'],
  imports: [FormsModule, CommonModule], // Ensure CommonModule is included for *ngIf
})
export class ViewPlayerComponent {

  constructor(private authService: AuthService, private router: Router) {}

  // Placeholder for navigating to view characters
  viewCharacter() {
    console.log('Navigating to view character');
    // Implement functionality to navigate or display character-related features
  }

  // Placeholder for navigating to view inventory
  viewInventory() {
    console.log('Navigating to view inventory');
    // Implement functionality to navigate or display inventory-related features
  }

  // Logout functionality
  logout() {
    this.authService.logout(); // Clear authentication
    this.router.navigate(['/login']); // Redirect to login page
  }
}