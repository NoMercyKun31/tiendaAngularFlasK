import { Component } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { VideojuegosService } from '../../services/videojuegos.service';
import { NgFor } from '@angular/common';
import { CarritoService } from '../../services/carrito.service';

@Component({
  selector: 'app-detalle-producto',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './detalle-producto.component.html',
  styleUrls: ['./detalle-producto.component.css']
})
export class DetalleProductoComponent {
  videojuego: any;

  constructor(
    private route: ActivatedRoute, 
    private videojuegosService: VideojuegosService,
    private carritoService: CarritoService) {}

  ngOnInit() {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.videojuegosService.obtenerVideojuegoPorId(+id).subscribe({
        next: (data) => {
          this.videojuego = data;
        },
        error: (error) => {
          console.error('Error al obtener los detalles del videojuego', error);
        },
      });
    }
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
}
