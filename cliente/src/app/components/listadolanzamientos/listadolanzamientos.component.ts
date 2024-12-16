import { Component, OnInit } from '@angular/core';
import { VideojuegosService } from '../../services/videojuegos.service';
import { NgFor } from '@angular/common';
import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { CarritoService } from '../../services/carrito.service';

@Component({
  selector: 'app-listadolanzamientos',
  standalone: true,
  imports: [NgFor, RouterLink],
  templateUrl: './listadolanzamientos.component.html',
  styleUrls: ['./listadolanzamientos.component.css'],
})
export class ListadolanzamientosComponent implements OnInit {
  videojuegos: any[] = [];

  constructor(private videojuegosService: VideojuegosService,private route: ActivatedRoute, private router: Router, private carritoService: CarritoService) {}

  ngOnInit() {
    this.cargarVideojuegosNuevos();
  }

  cargarVideojuegosNuevos() {
    this.videojuegosService.obtenerVideojuegosNuevos().subscribe({
      next: (data) => {
        this.videojuegos = data;
      },
      error: (error) => {
        console.error('Error al obtener los videojuegos nuevos', error);
      },
    });
  }

  verDetalles(id: string) {
    this.router.navigate(['/detalle', id]);
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
