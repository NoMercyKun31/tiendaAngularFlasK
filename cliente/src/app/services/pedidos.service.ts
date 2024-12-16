import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PedidosService {
  private apiUrl = '/server/';

  constructor(private http: HttpClient) {}

  crearPedido(pedidoData: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}rest/pedidos/crear`, pedidoData);
  }

  obtenerPedidosUsuario(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}rest/pedidos/usuario`);
  }

  obtenerPedido(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}rest/pedidos/${id}`);
  }
}