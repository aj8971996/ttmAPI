import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-view-gm',
  templateUrl: './view-gm.component.html',
  styleUrls: ['./view-gm.component.css']
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