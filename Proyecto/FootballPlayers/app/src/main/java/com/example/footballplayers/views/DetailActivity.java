package com.example.footballplayers.views;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.example.footballplayers.R;

public class DetailActivity extends AppCompatActivity {

    private TextView nameTextView, descriptionTextView;
    private ImageView imageView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        // Inicializamos las vistas
        nameTextView = findViewById(R.id.nameTextView);
        descriptionTextView = findViewById(R.id.descriptionTextView);
        imageView = findViewById(R.id.imageView);

        // Obtener los datos pasados desde DashboardActivity
        String playerName = getIntent().getStringExtra("player_name");
        String playerDescription = getIntent().getStringExtra("player_description");
        String playerImage = getIntent().getStringExtra("player_image");

        // Mostrar los datos en los TextViews e ImageView
        nameTextView.setText(playerName);
        descriptionTextView.setText(playerDescription);
        Glide.with(this).load(playerImage).into(imageView);
    }
}
