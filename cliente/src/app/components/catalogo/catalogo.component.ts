import { Component } from '@angular/core';
import { VideojuegosService } from '../../services/videojuegos.service';
import { NgFor } from '@angular/common';
import { Router } from '@angular/router';
import { CarritoService } from '../../services/carrito.service';
import { FormsModule } from '@angular/forms';
import { SearchService } from '../../services/search.service';

@Component({
  standalone: true,
  imports: [NgFor, FormsModule],
  selector: 'app-catalogo',
  templateUrl: './catalogo.component.html',
  styleUrls: ['./catalogo.component.css']
})
export class CatalogoComponent {
  videojuegos: any[] = [];
  videojuegosFiltrados: any[] = [];
  paginaActual: number = 1;
  elementosPorPagina: number = 9;
  totalPaginas: number = 0;
  totalElementos: number = 0;
  sortDirection: 'asc' | 'desc' = 'asc';
  precioMinimo: number = 0;
  precioMaximo: number = 1000;

  constructor(
    private videojuegosService: VideojuegosService,
    private router: Router,
    private carritoService: CarritoService,
    private searchService: SearchService
  ) {
    this.searchService.searchTerm$.subscribe(term => {
      this.filtrarJuegos(term);
    });
  }

  ngOnInit() {
    this.cargarVideojuegos();
  }

  cargarVideojuegos() {
    this.videojuegosService.obtenerVideojuegosPaginados(this.paginaActual, this.elementosPorPagina).subscribe({
      next: (response: any) => {
        this.videojuegos = response.videojuegos;
        this.videojuegosFiltrados = [...this.videojuegos];
        this.totalElementos = response.total;
        this.totalPaginas = response.paginas_totales;
      },
      error: (error) => {
        console.error('Error al obtener los videojuegos', error);
      },
    });
  }

  verDetalles(id: string) {
    this.router.navigate(['/detalle', id]);
  }

  cambiarPagina(pagina: number) {
    this.paginaActual = pagina;
    this.cargarVideojuegos();
  }

  get paginas(): number[] {
    return Array.from({ length: this.totalPaginas }, (_, i) => i + 1);
  }

  agregarAlCarrito(id_videojuego: number, cantidad: number = 1) {
    this.carritoService.agregarAlCarrito(id_videojuego, cantidad).subscribe(
      (response) => {
        console.log('Producto agregado al carrito:', response);
        // Opcional: Puedes mostrar un mensaje de éxito
      },
      (error) => console.error('Error al agregar al carrito:', error)
    );
  }

  filtrarJuegos(searchTerm: string) {
    if (!searchTerm) {
      this.videojuegosFiltrados = this.videojuegos.filter(juego => {
        const precio = juego.precio;
        return precio >= this.precioMinimo && precio <= this.precioMaximo;
      });
    } else {
      this.videojuegosFiltrados = this.videojuegos.filter(juego => {
        const cumplePrecio = juego.precio >= this.precioMinimo && juego.precio <= this.precioMaximo;
        const cumpleBusqueda = juego.titulo.toLowerCase().includes(searchTerm.toLowerCase()) ||
                              juego.compania.toLowerCase().includes(searchTerm.toLowerCase());
        return cumplePrecio && cumpleBusqueda;
      });
    }
  }

  filtrarPorPrecio() {
    const currentSearchTerm = this.searchService.getCurrentSearchTerm();
    this.filtrarJuegos(currentSearchTerm);
  }

  ordenarPorNombre() {
    this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
    this.videojuegosFiltrados.sort((a, b) => {
      const comparacion = a.titulo.localeCompare(b.titulo);
      return this.sortDirection === 'asc' ? comparacion : -comparacion;
    });
  }

  ordenarPorPrecio() {
    this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
    this.videojuegosFiltrados.sort((a, b) => {
      const comparacion = a.precio - b.precio;
      return this.sortDirection === 'asc' ? comparacion : -comparacion;
    });
  }
}
