import { Component, OnInit, ViewChild } from '@angular/core';
import { CommonModule, NgIf } from '@angular/common';
import { ParticlesComponent } from './components/particles/particles.component';
import { CarritoService, ItemCarrito } from './services/carrito.service';
import { RouterOutlet, RouterLink, NavigationEnd, Router } from '@angular/router';
import { PedidosService } from './services/pedidos.service';
import { CheckoutModalComponent } from './components/checkout-modal/checkout-modal.component';
import { AdminModalComponent } from "./components/admin-modal/admin-modal.component";
import { SearchService } from './services/search.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  imports: [CommonModule, ParticlesComponent, RouterOutlet, RouterLink, NgIf, CheckoutModalComponent, AdminModalComponent, FormsModule],
  standalone: true,
})
export class AppComponent implements OnInit {
  @ViewChild('checkoutModal') checkoutModal!: CheckoutModalComponent;
  title = 'Lunar Games';
  isMenuOpen = false;
  isCartOpen = false;
  videojuegos: any[] = [];
  showMainSection: boolean = true;
  itemsCarrito: ItemCarrito[] = [];
  totalItems: number = 0;
  totalPrecio: number = 0;
  showAdminModal = false;
  adminPassword = '';
  adminError = '';
  searchTerm: string = '';
  showCheckoutModal = false;

  constructor(
    private router: Router,
    private carritoService: CarritoService,
    private pedidosService: PedidosService,
    private searchService: SearchService
  ) {
    this.carritoService.totalItems$.subscribe((total: number) => {
      this.totalItems = total;
    });
  }

  ngOnInit() {
    // Suscribirse a los cambios del carrito
    this.carritoService.carritoActualizado$.subscribe(() => {
      this.actualizarCarrito();
    });

    this.router.events.subscribe((event) => {
      if (event instanceof NavigationEnd) {
        this.showMainSection = !(
          event.url.includes('/catalogo') ||
          event.url.includes('/detalle') ||
          event.url.includes('/contact')
        );
        scrollTo(0, 0);
      }
    });

    // Cargar el carrito inicialmente
    this.actualizarCarrito();
  }

  actualizarCarrito() {
    this.carritoService.obtenerCarrito().subscribe(
      (items: ItemCarrito[]) => {
        this.itemsCarrito = items;
        this.calcularTotalPrecio();
      }
    );
  }

  calcularTotalPrecio() {
    this.totalPrecio = this.itemsCarrito.reduce(
      (total, item) => total + (item.precio * item.cantidad),
      0
    );
  }

  toggleMenu() {
    this.isMenuOpen = !this.isMenuOpen;
  }

  toggleCart() {
    this.isCartOpen = !this.isCartOpen;
    if (this.isCartOpen) {
      this.actualizarCarrito();
    }
  }

  closeCart() {
    this.isCartOpen = false;
  }

  openCheckoutModal() {
    this.closeCart(); // Cerrar el carrito antes de abrir el modal
    this.showCheckoutModal = true;
  }

  closeCheckoutModal() {
    this.showCheckoutModal = false;
  }

  scrollToCategories() {
    document.getElementById('categorias')?.scrollIntoView({ behavior: 'smooth' });
  }

  navigateToCatalogo() {
    this.showMainSection = false;
  }

  eliminarDelCarrito(idVideojuego: number) {
    this.carritoService.eliminarDelCarrito(idVideojuego).subscribe(
      () => {
        this.actualizarCarrito();
      },
      (error) => console.error('Error al eliminar del carrito:', error)
    );
  }

  actualizarCantidad(idVideojuego: number, cantidad: number) {
    if (cantidad > 0) {
      this.carritoService.actualizarCantidad(idVideojuego, cantidad).subscribe(
        () => {
          this.actualizarCarrito();
        },
        (error) => console.error('Error al actualizar cantidad:', error)
      );
    }
  }

  vaciarCarrito() {
    this.carritoService.vaciarCarrito().subscribe(
      () => {
        this.itemsCarrito = [];
        this.calcularTotalPrecio();
      },
      (error) => console.error('Error al vaciar el carrito:', error)
    );
  }

  realizarPedido() {
    this.checkoutModal.openModal();

    const pedidoData = {
    };
  }

  checkAdminPassword() {
    const correctPassword = 'admin123';
    
    if (this.adminPassword === correctPassword) {
      window.location.href = 'http://127.0.0.1:5000/admin/';
    } else {
      this.adminError = 'Contraseña incorrecta';
    }
  }

  openAdminModal(event: Event) {
    event.preventDefault();
    this.showAdminModal = true;
  }

  closeAdminModal() {
    this.showAdminModal = false;
  }

  onAdminAuthenticated() {
    this.showAdminModal = false;
  }

  onSearchSubmit(event: Event) {
    event.preventDefault();
    if (this.searchTerm.trim() !== '') {
      this.searchService.updateSearchTerm(this.searchTerm);
      // Si no estamos en la página de catálogo, navegamos a ella
      if (!this.router.url.includes('/catalogo')) {
        this.router.navigate(['/catalogo']);
      }
    }
  }

  onSearch(event: any) {
    const term = event.target.value;
    this.searchService.updateSearchTerm(term);
    if (!this.router.url.includes('/catalogo')) {
      this.router.navigate(['/catalogo']);
    }
  }
}
