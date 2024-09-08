import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http'; // Ensure this is correct
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root', // This ensures it's globally provided
})
export class AuthService {
  private apiUrl = 'http://localhost:8000'; // Your API base URL

  constructor(private http: HttpClient) {}

  // Login service, using both username and password
  login(user_name: string, password: string): Observable<any> {
    // Use HttpParams for URL-encoded data
    const loginData = new HttpParams()
      .set('username', user_name)
      .set('password', password);

    return this.http.post(`${this.apiUrl}/login`, loginData.toString(), {
      headers: new HttpHeaders({
        'Content-Type': 'application/x-www-form-urlencoded'
      })
    });
  }

  logout() {
    // Clear any stored authentication tokens or session data
    localStorage.removeItem('auth_token'); // Example if you store tokens in localStorage
  }  

  // Register service adjusted to include password
  register(user_name: string, password: string, user_type: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/register`, { user_name, password, user_type });
  }

  // Add this method in auth.service.ts
  isLoggedIn(): boolean {
    // Logic to check if the user is logged in
    return !!localStorage.getItem('token'); // Example token check
  }
}
