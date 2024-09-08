import { Component } from '@angular/core';
import { Router } from '@angular/router'; // Router to navigate to different views
import { CommonModule } from '@angular/common'; // Import CommonModule for *ngIf

@Component({
  selector: 'app-side-menu',
  standalone: true,
  templateUrl: './side-menu.component.html',
  styleUrls: ['./side-menu.component.css'],
  imports: [CommonModule], // Ensure CommonModule is included for *ngIf
})
export class SideMenuComponent {
  isGM: boolean = false; // Property to track if the user is a GM
  isPlayer: boolean = false; // Property to track if the user is a Player

  constructor(private router: Router) {}

  ngOnInit() {
    this.isGM = this.checkIfGM();
    this.isPlayer = this.checkIfPlayer();
    console.log('isGM:', this.isGM, 'isPlayer:', this.isPlayer);
  }  

  checkIfGM(): boolean {
    // Fetch the role from localStorage or fallback to 'Player'
    const currentRole = localStorage.getItem('userRole') || 'Player'; // Default to Player if null
    console.log('Current role from localStorage:', currentRole);
    return currentRole === 'GM'; // Return true if the user is a GM
  }

  checkIfPlayer(): boolean {
    // Fetch the role from localStorage or fallback to 'Player'
    const currentRole = localStorage.getItem('userRole') || 'Player'; // Default to Player if null
    return currentRole === 'Player' || currentRole === 'GM'; // GM can also access Player options
  }

  // GM Methods
  addCharacter() { this.router.navigate(['/gm/add-character']); }
  addAbility() { this.router.navigate(['/gm/add-ability']); }
  addExpertise() { this.router.navigate(['/gm/add-expertise']); }
  addJobSkill() { this.router.navigate(['/gm/add-job-skill']); }
  addSpeciesPassive() { this.router.navigate(['/gm/add-species-passive']); }
  addItem() { this.router.navigate(['/gm/add-item']); }
  addWeapon() { this.router.navigate(['/gm/add-weapon']); }
  viewCharacters() { this.router.navigate(['/gm/view-characters']); }
  viewLibraries() { this.router.navigate(['/gm/view-libraries']); }
  viewBackpacks() { this.router.navigate(['/gm/view-backpacks']); }
  viewItems() { this.router.navigate(['/gm/view-items']); }
  viewAbilities() { this.router.navigate(['/gm/view-abilities']); }
  bulkRemoveItems() { this.router.navigate(['/gm/remove-items']); }

  // Player Methods
  addPlayerCharacter() { this.router.navigate(['/player/add-character']); }
  viewPlayerCharacter() { this.router.navigate(['/player/view-character']); }
  viewPlayerBackpack() { this.router.navigate(['/player/view-backpack']); }
  viewPlayerLibrary() { this.router.navigate(['/player/view-library']); }
  getAbilityDetails() { this.router.navigate(['/player/get-ability']); }
  getJobSkillDetails() { this.router.navigate(['/player/get-job-skill']); }
  getSpeciesPassiveDetails() { this.router.navigate(['/player/get-species-passive']); }
  getExpertiseDetails() { this.router.navigate(['/player/get-expertise']); }
  getItemDetails() { this.router.navigate(['/player/get-item']); }
  getWeaponDetails() { this.router.navigate(['/player/get-weapon']); }
  levelUpCharacter() { this.router.navigate(['/player/level-up']); }
  adjustCharacterStats() { this.router.navigate(['/player/adjust-stats']); }
  addItemToBackpack() { this.router.navigate(['/player/add-item']); }
  removeItemFromBackpack() { this.router.navigate(['/player/remove-item']); }
  addWeaponToBackpack() { this.router.navigate(['/player/add-weapon']); }
  removeWeaponFromBackpack() { this.router.navigate(['/player/remove-weapon']); }
}