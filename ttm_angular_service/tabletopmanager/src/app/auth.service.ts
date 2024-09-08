import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private apiUrl = 'http://localhost:8000'; // Your API base URL

  constructor(private http: HttpClient) {}

  // Adjust login to use only user_name for now
  login(user_name: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/login`, { user_name });
  }

  // Register service adjusted to match new user structure
  register(user_name: string, user_type: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/register`, { user_name, user_type });
  }
}