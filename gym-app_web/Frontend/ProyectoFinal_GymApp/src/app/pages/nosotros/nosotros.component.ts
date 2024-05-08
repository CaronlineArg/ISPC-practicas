import { Component } from '@angular/core';

@Component({
  selector: 'app-nosotros',
  templateUrl: './nosotros.component.html',
  styleUrls: ['./nosotros.component.css']
})
export class NosotrosComponent {

  colorFondo: string = '#ffffff'; // Asigna el color de fondo blanco
  colorTexto: string = '#000000'; // Asigna el color de texto negro
  colorBotones: string = '#dc3545'; // Asigna el color del botón (rojo)
  tamanioBoton: string = '24px'; // Asigna el tamaño del botón
  radioBordesBoton: string = '5px'; // Asigna el radio de los bordes del botón
  tamanoImagen: string = '250px';
}

