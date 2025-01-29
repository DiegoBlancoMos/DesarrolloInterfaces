package com.example.footballplayers.models;

public class Player {
    private String nombre;
    private String descripcion;
    private String url_imagen;

    // Constructores, uno vacío y otro lleno.
    public Player(){}

    public Player(String nombre, String descripcion, String url_imagen) {
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.url_imagen = url_imagen;
    }

    // Getters y Setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public String getUrl_imagen() {
        return url_imagen;
    }

    public void setUrl_imagen(String url_imagen) {
        this.url_imagen = url_imagen;
    }
}
