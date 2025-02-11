package com.example.footballplayers.views;

import android.content.Intent;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import com.example.footballplayers.R;
import com.example.footballplayers.adapters.PlayerAdapter;
import com.example.footballplayers.models.Player;
import com.example.footballplayers.viewmodels.FavoriteViewModel;
import java.util.ArrayList;

public class FavoritesActivity extends AppCompatActivity {
    private RecyclerView recyclerView;
    private PlayerAdapter playerAdapter;
    private FavoriteViewModel viewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_favorites);

        recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        playerAdapter = new PlayerAdapter(new ArrayList<>(), this::openDetailActivity);
        recyclerView.setAdapter(playerAdapter);

        viewModel = new ViewModelProvider(this).get(FavoriteViewModel.class);

        // Observar los jugadores favoritos
        viewModel.getFavoritePlayers().observe(this, players -> {
            if (players != null) {
                playerAdapter.updatePlayers(players);
            }
        });

        // Iniciar la carga de favoritos
        viewModel.fetchFavorites();
    }

    private void openDetailActivity(Player player) {
        Intent intent = new Intent(FavoritesActivity.this, DetailActivity.class);
        intent.putExtra("player_name", player.getNombre());
        intent.putExtra("player_description", player.getDescripcion());
        intent.putExtra("player_image", player.getUrl_imagen());
        startActivity(intent);
    }
}
