package com.example.footballplayers.views;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import com.bumptech.glide.Glide;
import com.example.footballplayers.R;
import com.example.footballplayers.models.Player;
import com.example.footballplayers.viewmodels.FavoriteViewModel;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

public class DetailFragment extends Fragment {
    private TextView nameTextView, descriptionTextView;
    private ImageView imageView;
    private FloatingActionButton fabFavorite;
    private FavoriteViewModel favoriteViewModel;

    public DetailFragment() {}

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_detail, container, false);

        nameTextView = view.findViewById(R.id.nameTextView);
        descriptionTextView = view.findViewById(R.id.descriptionTextView);
        imageView = view.findViewById(R.id.imageView);
        fabFavorite = view.findViewById(R.id.fabFavorite);

        Bundle args = getArguments();
        if (args != null) {
            String playerName = args.getString("player_name");
            String playerDescription = args.getString("player_description");
            String playerImage = args.getString("player_image");

            nameTextView.setText(playerName);
            descriptionTextView.setText(playerDescription);
            if (getContext() != null) {
                Glide.with(getContext()).load(playerImage).into(imageView);
            }

            favoriteViewModel = new ViewModelProvider(this).get(FavoriteViewModel.class);

            favoriteViewModel.getIsFavorite().observe(getViewLifecycleOwner(), isFavorite -> {
                fabFavorite.setImageResource(isFavorite ?
                        R.drawable.ic_favorite_filled :
                        R.drawable.ic_favorite_border);
            });

            Player player = new Player(playerName, playerDescription, playerImage);

            fabFavorite.setOnClickListener(v -> favoriteViewModel.toggleFavorite(player));

            favoriteViewModel.checkIsFavorite(playerName);
        }

        return view;
    }
}