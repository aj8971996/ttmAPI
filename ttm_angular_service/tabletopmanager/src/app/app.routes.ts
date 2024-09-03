import { Route } from '@angular/router';
import { LoginComponent } from './login/login.component';

export const routes: Route[] = [
  { path: '', redirectTo: '/login', pathMatch: 'full' }, // Redirect to login
  { path: 'login', component: LoginComponent }, // Route for login component
  // Add more routes here as needed
];
