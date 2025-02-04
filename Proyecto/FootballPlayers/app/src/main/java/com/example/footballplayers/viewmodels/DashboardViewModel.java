package com.example.footballplayers.viewmodels;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;

import com.example.footballplayers.models.Player;
import com.example.footballplayers.repositories.DashboardRepository;

import java.util.List;

public class DashboardViewModel extends ViewModel {
    private MutableLiveData<List<Player>> playersLiveData = new MutableLiveData<>();
    private MutableLiveData<String> errorLiveData = new MutableLiveData<>();
    private DashboardRepository repository;

    public DashboardViewModel() {
        repository = new DashboardRepository();
    }

    public LiveData<List<Player>> getPlayers() {
        return playersLiveData;
    }

    public LiveData<String> getError() {
        return errorLiveData;
    }

    public void fetchPlayers() {
        repository.getPlayers(new DashboardRepository.Callback() {
            @Override
            public void onSuccess(List<Player> players) {
                playersLiveData.postValue(players);
            }

            @Override
            public void onFailure(Exception e) {
                errorLiveData.postValue(e.getMessage());
            }
        });
    }
}