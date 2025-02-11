package com.example.footballplayers.adapters;

import androidx.annotation.NonNull;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.example.footballplayers.R;
import com.example.footballplayers.models.Player;

import java.util.List;

public class PlayerAdapter extends RecyclerView.Adapter<PlayerAdapter.PlayerViewHolder> {

    private List<Player> players;
    private OnItemClickListener listener;

    public PlayerAdapter(List<Player> players, OnItemClickListener listener) {
        this.players = players;
        this.listener = listener;
    }

    @NonNull
    @Override
    public PlayerViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_player, parent, false);
        return new PlayerViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull PlayerViewHolder holder, int position) {
        Player player = players.get(position);

        holder.nameTextView.setText(player.getNombre());
        holder.descriptionTextView.setText(player.getDescripcion());

        // Cargar imagen con Glide/Picasso
        Glide.with(holder.itemView.getContext())
                .load(player.getUrl_imagen())
                .into(holder.imageView);

        // Añadir descripción accesible para TalkBack
        if (player.getNombre() != null && !player.getNombre().isEmpty()) {
            holder.imageView.setContentDescription("Imagen de " + player.getNombre());
        } else {
            holder.imageView.setContentDescription("Imagen de jugador desconocido");
        }

        // Mejorar la accesibilidad de los textos asegurando contraste y legibilidad
        holder.nameTextView.setContentDescription("Nombre del jugador: " + player.getNombre());
        holder.descriptionTextView.setContentDescription("Descripción: " + player.getDescripcion());

        holder.itemView.setOnClickListener(v -> listener.onItemClick(player));
    }


    @Override
    public int getItemCount() {
        return players.size();
    }

    public class PlayerViewHolder extends RecyclerView.ViewHolder {

        private TextView nameTextView;
        private TextView descriptionTextView;
        private ImageView imageView;

        public PlayerViewHolder(View itemView) {
            super(itemView);
            nameTextView = itemView.findViewById(R.id.nameTextView);
            descriptionTextView = itemView.findViewById(R.id.descriptionTextView);
            imageView = itemView.findViewById(R.id.imageView);
        }

        public void bind(Player player) {
            nameTextView.setText(player.getNombre());
            descriptionTextView.setText(player.getDescripcion());
            Glide.with(imageView.getContext()).load(player.getUrl_imagen()).into(imageView);

            itemView.setOnClickListener(v -> listener.onItemClick(player));
        }
    }

    public interface OnItemClickListener {
        void onItemClick(Player player);
    }
    public void updatePlayers(List<Player> newPlayers) {
        this.players = newPlayers;
        notifyDataSetChanged();
    }
}
