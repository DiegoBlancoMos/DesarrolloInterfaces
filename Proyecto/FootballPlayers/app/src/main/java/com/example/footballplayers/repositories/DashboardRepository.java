package com.example.footballplayers.repositories;

import androidx.annotation.NonNull;

import com.example.footballplayers.models.Player;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class DashboardRepository {

    private DatabaseReference databaseRef;

    public DashboardRepository() {
        this.databaseRef = FirebaseDatabase.getInstance().getReference("jugadores");
    }

    public void getPlayers(Callback callback) {
        databaseRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                List<Player> players = new ArrayList<>();
                for (DataSnapshot snapshot : dataSnapshot.getChildren()) {
                    Player player = snapshot.getValue(Player.class);
                    players.add(player);
                }
                callback.onSuccess(players);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {
                callback.onFailure(databaseError.toException());
            }
        });
    }

    public interface Callback {
        void onSuccess(List<Player> players);
        void onFailure(Exception e);
    }
}
