package com.example.footballplayers.repositories;

import androidx.annotation.NonNull;
import com.example.footballplayers.models.Player;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.*;
import java.util.ArrayList;
import java.util.List;

public class FavoriteRepository {
    private final DatabaseReference userFavoritesRef;
    private final String userId;

    public FavoriteRepository() {
        userId = FirebaseAuth.getInstance().getCurrentUser().getUid();
        userFavoritesRef = FirebaseDatabase.getInstance().getReference("users").child(userId).child("favoritos");
    }

    public void getFavorites(FavoriteCallback callback) {
        userFavoritesRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                List<Player> favoritePlayers = new ArrayList<>();
                for (DataSnapshot favoriteSnapshot : snapshot.getChildren()) {
                    Player player = favoriteSnapshot.getValue(Player.class);
                    if (player != null) {
                        favoritePlayers.add(player);
                    }
                }
                callback.onSuccess(favoritePlayers);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                callback.onFailure(error.toException());
            }
        });
    }

    public void toggleFavorite(Player player, ToggleFavoriteCallback callback) {
        userFavoritesRef.child(player.getNombre()).addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                if (snapshot.exists()) {
                    // Remove from favorites
                    snapshot.getRef().removeValue()
                            .addOnSuccessListener(aVoid -> callback.onSuccess(false))
                            .addOnFailureListener(callback::onFailure);
                } else {
                    // Add to favorites
                    snapshot.getRef().setValue(player)
                            .addOnSuccessListener(aVoid -> callback.onSuccess(true))
                            .addOnFailureListener(callback::onFailure);
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                callback.onFailure(error.toException());
            }
        });
    }

    public void isFavorite(String playerId, IsFavoriteCallback callback) {
        userFavoritesRef.child(playerId).addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                callback.onSuccess(snapshot.exists());
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                callback.onFailure(error.toException());
            }
        });
    }

    public interface FavoriteCallback {
        void onSuccess(List<Player> favoritePlayers);
        void onFailure(Exception e);
    }

    public interface ToggleFavoriteCallback {
        void onSuccess(boolean isFavorite);
        void onFailure(Exception e);
    }

    public interface IsFavoriteCallback {
        void onSuccess(boolean isFavorite);
        void onFailure(Exception e);
    }
}
