import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-view-player',
  templateUrl: './view-player.component.html',
  styleUrls: ['./view-player.component.css']
})
export class ViewPlayerComponent {

  constructor(private authService: AuthService, private router: Router) {}

  // Navigate to view characters (placeholder for actual functionality)
  viewCharacter() {
    // Navigate to character viewing page or feature
  }

  // Navigate to view inventory (placeholder for actual functionality)
  viewInventory() {
    // Navigate to inventory viewing page or feature
  }

  // Logout and navigate back to login page
  logout() {
    this.authService.logout(); // Clear authentication
    this.router.navigate(['/login']); // Redirect to login page
  }
}