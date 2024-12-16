import { NgIf } from '@angular/common';
import { Component, EventEmitter, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-admin-modal',
  standalone: true,
  templateUrl: './admin-modal.component.html',
  imports: [FormsModule, NgIf],
})
export class AdminModalComponent {
  @Output() close = new EventEmitter<void>();
  @Output() authenticated = new EventEmitter<void>();
  
  password: string = '';
  errorMessage: string = '';

  checkPassword() {
    // Contraseña hardcodeada para demostración - en producción debería validarse contra el backend
    if (this.password === 'admin123') {
      this.authenticated.emit();
      window.location.href = 'http://127.0.0.1:5000/admin/';
    } else {
      this.errorMessage = 'Contraseña incorrecta';
    }
  }

  closeModal() {
    this.close.emit();
  }
}
