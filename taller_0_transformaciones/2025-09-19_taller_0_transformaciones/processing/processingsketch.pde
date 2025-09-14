import gifAnimation.*;

GifMaker generadorDeAnimacion;

float angulo;
float coordenada_x;
float coordenada_y;
float factor_escala;
boolean capturando = true;

void setup() {
  size(800, 600); 
  rectMode(CENTER);

  generadorDeAnimacion = new GifMaker(this, "animacion_final.gif");
  

  generadorDeAnimacion.setQuality(10);
  
 
  generadorDeAnimacion.setRepeat(0); 
  
  
  generadorDeAnimacion.setDelay(1000/60); 
}

void draw() {

  if (capturando) {
  
    background(0, 255, 0); 
    translate(width/2, height/2);

 
    angulo = radians(frameCount * 2.0);
    coordenada_x = map(sin(frameCount * 0.03), -1, 1, -180, 180);
    coordenada_y = map(cos(frameCount * 0.035), -1, 1, -180, 180);
    factor_escala = map(sin(frameCount * 0.05), -1, 1, 0.7, 1.8);

    pushMatrix();
    translate(coordenada_x, coordenada_y);
    rotate(angulo);
    scale(factor_escala);
    fill(255, 255, 0); 
    rect(0, 0, 120, 120);
    popMatrix();

    fill(255, 100, 0);
    ellipse(0, 0, 40, 40);
    

    generadorDeAnimacion.addFrame();
  }
  

  if (frameCount > 150 && capturando) { 
    generadorDeAnimacion.finish(); 
    capturando = false; 
    println("¡El archivo GIF se ha completado! Búscalo en la carpeta del proyecto.");
    noLoop(); 
  }
}
