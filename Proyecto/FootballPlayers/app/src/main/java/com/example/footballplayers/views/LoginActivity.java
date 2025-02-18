package com.example.footballplayers.views;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.Observer;

import com.example.footballplayers.R;
import com.example.footballplayers.viewmodels.LoginViewModel;
import com.google.firebase.auth.FirebaseAuth;

public class LoginActivity extends AppCompatActivity {

    private EditText emailInput, passwordInput;
    private LoginViewModel loginViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        SharedPreferences sharedPref = getSharedPreferences("AppConfig", Context.MODE_PRIVATE);
        boolean isDarkMode = sharedPref.getBoolean("darkMode", false);
        // Aplicar el tema antes de cargar la interfaz
        setTheme(isDarkMode ? R.style.ThemeOscuro : R.style.ThemeClaro);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        // Inicializar vistas
        emailInput = findViewById(R.id.emailInput);
        passwordInput = findViewById(R.id.passwordInput);

        // Crear o obtener el ViewModel
        loginViewModel = new LoginViewModel(getApplication());

        // Observar cambios en el mensaje de error o éxito
        loginViewModel.getErrorMessage().observe(this, new Observer<String>() {
            @Override
            public void onChanged(String message) {
                if (message != null) {
                    Toast.makeText(LoginActivity.this, message, Toast.LENGTH_SHORT).show();
                    if (message.equals("Inicio de sesión exitoso")) {
                        startActivity(new Intent(LoginActivity.this, MainActivity.class));
                        finish();
                    }
                }
            }
        });
        loginViewModel.getNavigateToDashboard().observe(this, shouldNavigate -> {
            if (shouldNavigate) {
                startActivity(new Intent(LoginActivity.this, MainActivity.class));
                finish();
            }
        });

        // Configurar los botones
        findViewById(R.id.loginButton).setOnClickListener(v -> {
            String email = emailInput.getText().toString();
            String password = passwordInput.getText().toString();

            if (loginViewModel.validateInputs(email, password)) {
                loginViewModel.loginUser(email, password);
            }
        });

        findViewById(R.id.goToRegisterButton).setOnClickListener(v ->
                startActivity(new Intent(LoginActivity.this, RegisterActivity.class)));
    }

    @Override
    protected void onStart() {
        super.onStart();
        // Verificar si el usuario ya está logueado
        if (FirebaseAuth.getInstance().getCurrentUser() != null) {
            startActivity(new Intent(this, MainActivity.class));
            finish();
        }
    }
}
