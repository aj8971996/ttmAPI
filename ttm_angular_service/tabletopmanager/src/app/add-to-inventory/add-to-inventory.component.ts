import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule, NgForm } from '@angular/forms'; // Import FormsModule and NgForm
import { CommonModule } from '@angular/common'; // Import CommonModule
import { SideMenuComponent } from '../side-menu/side-menu.component'; // Import SideMenuComponent

@Component({
  selector: 'app-add-to-inventory',
  standalone: true,
  templateUrl: './add-to-inventory.component.html',
  styleUrls: ['./add-to-inventory.component.css'],
  imports: [FormsModule, CommonModule, SideMenuComponent], // Ensure CommonModule is included for *ngIf
})
export class AddToInventoryComponent {
  selectedType: string = ''; // Holds selected type (item or weapon)
  inventoryData: any = {}; // Stores form data

  constructor(private router: Router) {}

  // Handle form submission
  onSubmit(inventoryForm: NgForm) {
    if (inventoryForm.invalid) {
      return;
    }

    if (this.selectedType === 'item') {
      // Handle adding an item
      console.log('Adding Item:', this.inventoryData);
      // Send item data to the server
    } else if (this.selectedType === 'weapon') {
      // Handle adding a weapon
      console.log('Adding Weapon:', this.inventoryData);
      // Send weapon data to the server
    }
  }
}