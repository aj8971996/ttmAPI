# Tabletopmanager

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 18.2.2.

## Features

- **Registration with Password Validation:**
   - Real-time password confirmation validation is added to ensure users input matching passwords before submitting the registration form.
   - The registration form includes a password field, a confirm password field, and a drop-down to select user type (Game Master or Player).

- **Login and Registration:**
   - The application allows users to register and log in using their username and password.
   - The backend API supports user management for both Game Masters (GMs) and Players.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Password Confirmation Validation

In the registration form, real-time validation is applied to ensure the password and confirm password fields match. If the passwords do not match, the user will see a real-time error message, and the registration button will be disabled until the passwords match.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Further help

To get more help on the Angular CLI, use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.dev/tools/cli) page.