import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true, // This allows the component to work without a module
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: [FormsModule], // Ensure FormsModule is imported here
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  login() {
    console.log('Username:', this.username);
    console.log('Password:', this.password);
    // Add login logic here (e.g., API call to authenticate)
  }
}
