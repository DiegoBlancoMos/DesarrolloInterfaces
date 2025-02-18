package com.example.footballplayers.views;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import com.example.footballplayers.R;
import com.example.footballplayers.adapters.PlayerAdapter;
import com.example.footballplayers.models.Player;
import com.example.footballplayers.viewmodels.DashboardViewModel;
import java.util.ArrayList;

public class DashboardFragment extends Fragment {
    private RecyclerView recyclerView;
    private PlayerAdapter playerAdapter;
    private DashboardViewModel viewModel;

    public DashboardFragment() {}

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_dashboard, container, false);

        recyclerView = view.findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));

        playerAdapter = new PlayerAdapter(new ArrayList<>(), this::openDetailFragment);
        recyclerView.setAdapter(playerAdapter);

        viewModel = new ViewModelProvider(this).get(DashboardViewModel.class);

        viewModel.getPlayers().observe(getViewLifecycleOwner(), players -> {
            if (players != null) {
                playerAdapter.updatePlayers(players);
            }
        });

        viewModel.fetchPlayers();

        return view;
    }

    private void openDetailFragment(Player player) {
        DetailFragment detailFragment = new DetailFragment();
        Bundle args = new Bundle();
        args.putString("player_name", player.getNombre());
        args.putString("player_description", player.getDescripcion());
        args.putString("player_image", player.getUrl_imagen());
        detailFragment.setArguments(args);

        getParentFragmentManager()
                .beginTransaction()
                .replace(R.id.fragmentContainer, detailFragment)
                .addToBackStack(null)
                .commit();
    }
}