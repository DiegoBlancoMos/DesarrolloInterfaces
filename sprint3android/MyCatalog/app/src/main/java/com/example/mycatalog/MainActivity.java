package com.example.mycatalog;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.navigation.fragment.NavHostFragment;
import androidx.navigation.ui.NavigationUI;

import com.example.mycatalog.R;
import com.google.android.material.bottomnavigation.BottomNavigationView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setupNavegacion();
    }

    private void setupNavegacion() {
        BottomNavigationView bottomNavigationView=findViewById(R.id.bottomNavigationView);
        NavHostFragment navHostFragment= (NavHostFragment) getSupportFragmentManager().findFragmentById(R.id.nav_hostfragment);
        NavigationUI.setupWithNavController(
                bottomNavigationView,
                navHostFragment.getNavController()
        );
    }
}