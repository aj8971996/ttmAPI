import { bootstrapApplication } from '@angular/platform-browser';
import { provideHttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';
import { importProvidersFrom } from '@angular/core';
import { AppComponent } from './app/app.component'; // Assuming AppComponent is your root component

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),  // Ensure routing is properly provided
    provideHttpClient(),    // Ensure HttpClient is provided for the app
    importProvidersFrom(FormsModule), // Ensure FormsModule is included for form handling
  ],
}).catch((err) => console.error(err));