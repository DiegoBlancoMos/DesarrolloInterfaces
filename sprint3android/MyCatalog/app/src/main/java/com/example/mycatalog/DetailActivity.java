package com.example.mycatalog;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_detail);
        Button btnMeGusta = findViewById(R.id.btnMeGusta);

        ImageView imageView = findViewById(R.id.imageView);
        imageView.setImageResource(R.drawable.yeremay);
        btnMeGusta.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Muestra un mensaje Toast al hacer clic en el botón
                Toast.makeText(DetailActivity.this, "ME GUSTA", Toast.LENGTH_SHORT).show();

                // Aquí puedes agregar la lógica para navegar a una nueva actividad (detalle)
                // Por ejemplo, si tienes una actividad llamada DetailActivity:
                Intent intent = new Intent(DetailActivity.this, DetailActivity.class);
                startActivity(intent);
            }
        });
    }
}