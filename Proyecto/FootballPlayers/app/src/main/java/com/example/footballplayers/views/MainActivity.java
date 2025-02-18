package com.example.footballplayers.views;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.MenuItem;

import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.databinding.DataBindingUtil;
import androidx.fragment.app.Fragment;
import com.example.footballplayers.R;
import com.example.footballplayers.databinding.ActivityMainBinding;
import com.google.firebase.auth.FirebaseAuth;

public class MainActivity extends AppCompatActivity {

    private ActivityMainBinding binding;  // DataBinding
    private ActionBarDrawerToggle toggle;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        SharedPreferences sharedPref = getSharedPreferences("AppConfig", Context.MODE_PRIVATE);
        boolean isDarkMode = sharedPref.getBoolean("darkMode", false);

        // Aplicar el tema
        if (isDarkMode) {
            setTheme(R.style.ThemeOscuro);
        } else {
            setTheme(R.style.ThemeClaro);
        }

        super.onCreate(savedInstanceState);
        getWindow().setBackgroundDrawableResource(isDarkMode ? R.color.dark_background : R.color.light_background);

        binding = DataBindingUtil.setContentView(this, R.layout.activity_main);

        toggle = new ActionBarDrawerToggle(
                this,
                binding.drawerLayout,
                R.string.navigation_drawer_open,
                R.string.navigation_drawer_close
        );
        binding.drawerLayout.addDrawerListener(toggle);
        toggle.syncState();

        // Habilitar el botón de navegación en la ActionBar
        if (getSupportActionBar() != null) {
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        }
        binding.navigationView.setNavigationItemSelectedListener(item -> {
            int itemId = item.getItemId();

            if (itemId == R.id.nav_dashboard) {
                openFragment(new DashboardFragment());
            } else if (itemId == R.id.nav_favourites) {
                openFragment(new FavoritesFragment());
            } else if (itemId == R.id.nav_profile) {
                openFragment(new ProfileFragment());
            } else if (itemId == R.id.nav_logout) {
                logoutUser();
            }

            binding.drawerLayout.closeDrawers();
            return true;
        });

        if (savedInstanceState == null) {
            openFragment(new DashboardFragment());
        }
    }

    private void openFragment(Fragment fragment) {
        getSupportFragmentManager()
                .beginTransaction()
                .replace(R.id.fragmentContainer, fragment)
                .commit();
    }

    private void logoutUser() {
        FirebaseAuth.getInstance().signOut();
        Intent intent = new Intent(this, LoginActivity.class);
        startActivity(intent);
        finish();
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        if (toggle.onOptionsItemSelected(item)) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}