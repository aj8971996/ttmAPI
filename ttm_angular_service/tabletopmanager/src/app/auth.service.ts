import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private apiUrl = 'http://localhost:8000'; // Your API base URL

  constructor(private http: HttpClient) {}

  // Login service, using both username and password
  login(user_name: string, password: string): Observable<any> {
    const loginData = new URLSearchParams(); // This is to match the OAuth2 password flow in FastAPI
    loginData.set('username', user_name); // FastAPI expects 'username' field for OAuth2
    loginData.set('password', password);  // FastAPI expects 'password' field for OAuth2

    // Send login request to backend
    return this.http.post(`${this.apiUrl}/login`, loginData.toString(), {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
  }

  logout() {
    // Clear any stored authentication tokens or session data
    localStorage.removeItem('auth_token'); // Example if you store tokens in localStorage
  }  

  // Register service adjusted to include password
  register(user_name: string, password: string, user_type: string): Observable<any> {
    const payload = { user_name, password, user_type };
    return this.http.post(`${this.apiUrl}/register`, payload);
  }

  // Add this method in auth.service.ts
  isLoggedIn(): boolean {
    // Logic to check if the user is logged in
    // This could involve checking a token in local storage or session storage
    return !!localStorage.getItem('token'); // Example token check
  }
}