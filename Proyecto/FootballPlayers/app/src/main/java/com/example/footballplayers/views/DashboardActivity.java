package com.example.footballplayers.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.footballplayers.R;
import com.example.footballplayers.adapters.PlayerAdapter;
import com.example.footballplayers.models.Player;
import com.example.footballplayers.viewmodels.DashboardViewModel;
import com.google.firebase.auth.FirebaseAuth;

import java.util.ArrayList;

public class DashboardActivity extends AppCompatActivity {

    private RecyclerView recyclerView;
    private PlayerAdapter playerAdapter;
    private DashboardViewModel viewModel;
    private FirebaseAuth mAuth;
    private Button logoutButton;
    private Button favoriteButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        mAuth = FirebaseAuth.getInstance();

        // Inicializar vistas
        recyclerView = findViewById(R.id.recyclerView);
        logoutButton = findViewById(R.id.logoutButton);
        favoriteButton = findViewById(R.id.favoriteButton);

        // Configurar RecyclerView
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        // Crear el adaptador
        playerAdapter = new PlayerAdapter(new ArrayList<>(), this::openDetailActivity);
        recyclerView.setAdapter(playerAdapter);

        // Configurar ViewModel
        viewModel = new ViewModelProvider(this).get(DashboardViewModel.class);

        // Observar cambios
        viewModel.getPlayers().observe(this, players -> {
            if (players != null) {
                playerAdapter.updatePlayers(players);
            }
        });

        // Cargar los datos
        viewModel.fetchPlayers();

        // Configurar el botón de favoritos
        favoriteButton.setOnClickListener(v -> {
            startActivity(new Intent(DashboardActivity.this, FavoritesActivity.class));
        });

        // Configurar logout
        logoutButton.setOnClickListener(v -> {
            mAuth.signOut();
            startActivity(new Intent(DashboardActivity.this, LoginActivity.class));
            finish();
        });
    }

    private void openDetailActivity(Player player) {
        Intent intent = new Intent(DashboardActivity.this, DetailActivity.class);
        intent.putExtra("player_name", player.getNombre());
        intent.putExtra("player_description", player.getDescripcion());
        intent.putExtra("player_image", player.getUrl_imagen());
        startActivity(intent);
    }

}