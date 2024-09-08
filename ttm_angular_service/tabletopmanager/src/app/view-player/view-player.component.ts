import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router'; // Import Router for navigation
import { CommonModule } from '@angular/common'; // Import CommonModule for *ngIf
import { SideMenuComponent } from '../side-menu/side-menu.component';

@Component({
  selector: 'app-view-player',
  standalone: true,
  templateUrl: './view-player.component.html',
  styleUrls: ['./view-player.component.css'],
  imports: [FormsModule, CommonModule, SideMenuComponent], // Ensure CommonModule is included for *ngIf
})
export class ViewPlayerComponent {

  constructor(private authService: AuthService, private router: Router) {}

  // Player Methods for routing
  viewCharacter() {
    this.router.navigate(['/player/view-character']);
  }

  viewBackpack() {
    this.router.navigate(['/player/view-backpack']);
  }

  viewLibrary() {
    this.router.navigate(['/player/view-library']);
  }

  getAbilityDetails() {
    this.router.navigate(['/player/get-ability']);
  }

  getJobSkillDetails() {
    this.router.navigate(['/player/get-job-skill']);
  }

  getSpeciesPassiveDetails() {
    this.router.navigate(['/player/get-species-passive']);
  }

  getItemDetails() {
    this.router.navigate(['/player/get-item']);
  }

  getWeaponDetails() {
    this.router.navigate(['/player/get-weapon']);
  }

  levelUpCharacter() {
    this.router.navigate(['/player/level-up']);
  }

  adjustCharacterStats() {
    this.router.navigate(['/player/adjust-stats']);
  }

  addItemToBackpack() {
    this.router.navigate(['/player/add-item']);
  }

  removeItemFromBackpack() {
    this.router.navigate(['/player/remove-item']);
  }

  addWeaponToBackpack() {
    this.router.navigate(['/player/add-weapon']);
  }

  removeWeaponFromBackpack() {
    this.router.navigate(['/player/remove-weapon']);
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