package com.example.footballplayers;

import static androidx.core.content.ContextCompat.startActivity;

import android.content.ClipData;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.squareup.picasso.Picasso;

public class DashboardActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;
    private DatabaseReference mDatabase;
    private TextView titleText, descriptionText;
    private ImageView itemImage;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        mAuth = FirebaseAuth.getInstance();
        mDatabase = FirebaseDatabase.getInstance().getReference("items");

        titleText = findViewById(R.id.titleText);
        descriptionText = findViewById(R.id.descriptionText);
        itemImage = findViewById(R.id.itemImage);

        findViewById(R.id.logoutButton).setOnClickListener(v -> logout());

        loadRandomItem();
    }

    private void loadRandomItem() {
        mDatabase.limitToFirst(1).addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                if (snapshot.exists()) {
                    DataSnapshot itemSnapshot = snapshot.getChildren().iterator().next();

                    String title = itemSnapshot.child("nombre").getValue(String.class);
                    String description = itemSnapshot.child("descripcion").getValue(String.class);
                    String imageUrl = itemSnapshot.child("url_imagen").getValue(String.class);

                    titleText.setText(title);
                    descriptionText.setText(description);

                    // Cargar imagen usando Picasso
                    Picasso.get()
                            .load(imageUrl)
                            .into(itemImage);
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Toast.makeText(DashboardActivity.this, "Error al cargar datos",
                        Toast.LENGTH_SHORT).show();
            }
        });
    }

    private void logout() {
        mAuth.signOut();
        startActivity(new Intent(DashboardActivity.this, LoginActivity.class));
        finish();
    }
}