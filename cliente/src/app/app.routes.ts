import { Routes } from '@angular/router';
import { CatalogoComponent } from './components/catalogo/catalogo.component';
import { ListadolanzamientosComponent } from './components/listadolanzamientos/listadolanzamientos.component';
import { DetalleProductoComponent } from './components/detalle-producto/detalle-producto.component';
import { ContactComponent } from './contact/contact.component';

export const routes: Routes = [
    { path: '', component: ListadolanzamientosComponent },
    { path: 'catalogo', component: CatalogoComponent },
    { path: 'detalle/:id', component: DetalleProductoComponent }, 
    { path: 'lanzamientos', component: ListadolanzamientosComponent },
    { path: 'contact', component: ContactComponent },
];
