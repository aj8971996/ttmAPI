import { Route } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ViewGmComponent } from './view-gm/view-gm.component'; // Import GM view component
import { ViewPlayerComponent } from './view-player/view-player.component'; // Import Player view component
import { AuthGuard } from './auth/auth.guard'; // Import auth guard for route protection

export const routes: Route[] = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'view-gm', component: ViewGmComponent, canActivate: [AuthGuard] }, // GM View
  { path: 'view-player', component: ViewPlayerComponent, canActivate: [AuthGuard] }, // Player View
  { path: '**', redirectTo: '/login' }, // Catch-all route to redirect to login
];