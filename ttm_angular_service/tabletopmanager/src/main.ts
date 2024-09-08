import { bootstrapApplication } from '@angular/platform-browser';
import { provideHttpClient, withFetch } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';
import { importProvidersFrom } from '@angular/core';
import { AppComponent } from './app/app.component'; // Assuming AppComponent is your root component

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),  // This will handle the routing between login, register, etc.
    provideHttpClient(withFetch()),  // Ensure HttpClient is provided
    importProvidersFrom(FormsModule) // Ensure FormsModule is included for forms
  ],
}).catch((err) => console.error(err));