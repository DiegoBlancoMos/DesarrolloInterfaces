package com.example.footballplayers.views;

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.bumptech.glide.Glide;
import com.example.footballplayers.R;
import com.example.footballplayers.models.Player;
import com.example.footballplayers.viewmodels.FavoriteViewModel;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

public class DetailActivity extends AppCompatActivity {
    private TextView nameTextView, descriptionTextView;
    private ImageView imageView;
    private FloatingActionButton fabFavorite;
    private FavoriteViewModel favoriteViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        nameTextView = findViewById(R.id.nameTextView);
        descriptionTextView = findViewById(R.id.descriptionTextView);
        imageView = findViewById(R.id.imageView);
        fabFavorite = findViewById(R.id.fabFavorite);

        String playerName = getIntent().getStringExtra("player_name");
        String playerDescription = getIntent().getStringExtra("player_description");
        String playerImage = getIntent().getStringExtra("player_image");

        nameTextView.setText(playerName);
        descriptionTextView.setText(playerDescription);
        Glide.with(this).load(playerImage).into(imageView);

        favoriteViewModel = new ViewModelProvider(this).get(FavoriteViewModel.class);

        favoriteViewModel.getIsFavorite().observe(this, isFavorite -> {
            fabFavorite.setImageResource(isFavorite ?
                    R.drawable.ic_favorite_filled :
                    R.drawable.ic_favorite_border);
        });
        Player player = new Player(playerName, playerDescription, playerImage);

        fabFavorite.setOnClickListener(v -> {
            favoriteViewModel.toggleFavorite(player);
        });

        favoriteViewModel.checkIsFavorite(playerName);
    }
}