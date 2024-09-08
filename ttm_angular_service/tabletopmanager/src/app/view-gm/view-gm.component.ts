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

  // Navigate to add character
  addCharacter() {
    this.router.navigate(['/gm/add-character']);
  }

  // Navigate to add ability
  addAbility() {
    this.router.navigate(['/gm/add-ability']);
  }

  // Navigate to add expertise
  addExpertise() {
    this.router.navigate(['/gm/add-expertise']);
  }

  // Navigate to add job skill
  addJobSkill() {
    this.router.navigate(['/gm/add-job-skill']);
  }

  // Navigate to add species passive
  addSpeciesPassive() {
    this.router.navigate(['/gm/add-species-passive']);
  }

  // Navigate to add item
  addItem() {
    this.router.navigate(['/gm/add-item']);
  }

  // Navigate to add weapon
  addWeapon() {
    this.router.navigate(['/gm/add-weapon']);
  }

  // Navigate to view all characters
  viewCharacters() {
    this.router.navigate(['/gm/view-characters']);
  }

  // Navigate to view all libraries
  viewLibraries() {
    this.router.navigate(['/gm/view-libraries']);
  }

  // Navigate to view all backpacks
  viewBackpacks() {
    this.router.navigate(['/gm/view-backpacks']);
  }

  // Navigate to view item inventory
  viewItems() {
    this.router.navigate(['/gm/view-items']);
  }

  // Navigate to view all abilities
  viewAbilities() {
    this.router.navigate(['/gm/view-abilities']);
  }

  // Navigate to bulk remove items
  bulkRemoveItems() {
    this.router.navigate(['/gm/remove-items']);
  }

  // Toggle the side menu
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