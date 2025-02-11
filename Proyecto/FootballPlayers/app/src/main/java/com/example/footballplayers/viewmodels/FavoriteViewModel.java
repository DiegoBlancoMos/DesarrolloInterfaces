package com.example.footballplayers.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.footballplayers.models.Player;
import com.example.footballplayers.repositories.FavoriteRepository;
import java.util.List;

public class FavoriteViewModel extends ViewModel {
    private final FavoriteRepository favoriteRepository;
    private final MutableLiveData<List<Player>> favoritePlayersLiveData = new MutableLiveData<>();
    private final MutableLiveData<Boolean> isLoadingLiveData = new MutableLiveData<>();
    private final MutableLiveData<String> errorLiveData = new MutableLiveData<>();
    private final MutableLiveData<Boolean> isFavoriteLiveData = new MutableLiveData<>();

    public FavoriteViewModel() {
        favoriteRepository = new FavoriteRepository();
    }

    public void fetchFavorites() {
        isLoadingLiveData.setValue(true);
        favoriteRepository.getFavorites(new FavoriteRepository.FavoriteCallback() {
            @Override
            public void onSuccess(List<Player> favoritePlayers) {
                favoritePlayersLiveData.setValue(favoritePlayers);
                isLoadingLiveData.setValue(false);
            }

            @Override
            public void onFailure(Exception e) {
                errorLiveData.setValue(e.getMessage());
                isLoadingLiveData.setValue(false);
            }
        });
    }

    public void toggleFavorite(Player player) {
        isLoadingLiveData.setValue(true);
        favoriteRepository.toggleFavorite(player, new FavoriteRepository.ToggleFavoriteCallback() {
            @Override
            public void onSuccess(boolean isFavorite) {
                isFavoriteLiveData.setValue(isFavorite);
                isLoadingLiveData.setValue(false);
                fetchFavorites(); // Actualizar la lista después de toggle
            }

            @Override
            public void onFailure(Exception e) {
                errorLiveData.setValue(e.getMessage());
                isLoadingLiveData.setValue(false);
            }
        });
    }

    public void checkIsFavorite(String playerId) {
        favoriteRepository.isFavorite(playerId, new FavoriteRepository.IsFavoriteCallback() {
            @Override
            public void onSuccess(boolean isFavorite) {
                isFavoriteLiveData.setValue(isFavorite);
            }

            @Override
            public void onFailure(Exception e) {
                errorLiveData.setValue(e.getMessage());
            }
        });
    }

    public LiveData<List<Player>> getFavoritePlayers() {
        return favoritePlayersLiveData;
    }

    public LiveData<Boolean> getIsLoading() {
        return isLoadingLiveData;
    }

    public LiveData<String> getError() {
        return errorLiveData;
    }

    public LiveData<Boolean> getIsFavorite() {
        return isFavoriteLiveData;
    }
}
