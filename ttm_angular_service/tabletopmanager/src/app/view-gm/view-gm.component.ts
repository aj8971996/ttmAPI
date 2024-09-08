import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router'; // Import Router for navigation
import { CommonModule } from '@angular/common'; // Import CommonModule for *ngIf
import { SideMenuComponent } from '../side-menu/side-menu.component';

@Component({
  selector: 'app-view-gm',
  standalone: true,
  templateUrl: './view-gm.component.html',
  styleUrls: ['./view-gm.component.css'],
  imports: [FormsModule, CommonModule, SideMenuComponent], // Ensure CommonModule is included for *ngIf
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

  toggleMenu() {
    const menu = document.querySelector('.side-menu');
    const hamburger = document.querySelector('.hamburger-menu'); // Select the hamburger button
    if (menu && hamburger) {
      menu.classList.toggle('open'); // Toggle the open class on the side menu
      hamburger.classList.toggle('open'); // Toggle the open class on the hamburger menu
    } else {
      console.error("Menu or hamburger button element not found.");
    }
  }  

  // Logout and navigate back to login page
  logout() {
    this.authService.logout(); // Clear authentication
    this.router.navigate(['/login']); // Redirect to login page
  }
}